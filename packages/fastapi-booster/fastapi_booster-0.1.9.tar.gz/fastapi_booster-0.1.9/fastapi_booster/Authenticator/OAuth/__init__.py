import os
import secrets
from typing import Any, Dict, Optional
from urllib.parse import urlencode

import httpx
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse

from fastapi_booster.Module import Module


class OAuthAuthenticator(Module):
    _instance = None
    _oauth2_scheme = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(
        self,
        app: FastAPI,
        auth_url: str,
        token_url: str,
        client_id: str,
        user_info_url: str,
        client_secret: str,
        scope: Optional[dict] = {
            "openid": "OpenID Connect scope",
            "profile": "User profile information",
            "email": "User email address",
        },
    ):
        super().__init__(
            name="OAuthAuthenticator",
            description="OAuth authentication module for FastAPI Booster.",
        )
        self._auth_url = auth_url
        self._token_url = token_url
        self._user_info_url = user_info_url
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope
        self.__class__._oauth2_scheme = OAuth2AuthorizationCodeBearer(
            authorizationUrl=self._auth_url,
            tokenUrl=self._token_url,
            scopes=self._scope,
        )
        app.swagger_ui_init_oauth = {
            "clientId": self._client_id,
            "clientSecret": self._client_secret,
        }
        app.add_middleware(SessionMiddleware, secret_key=os.getenv("SECRET_KEY", secrets.token_hex(32)))

        @self.router.get("/login")
        async def login(request: Request):
            # Generate a state parameter and store it in the session
            state = secrets.token_hex(16)
            request.session["state"] = state

            # Construct the authorization URL
            params = {
                "response_type": "code",
                "client_id": self._client_id,
                "redirect_uri": str(request.url_for("auth")),
                "scope": self._scope,
                "state": state,
            }
            authorization_url = f"{self._auth_url}?{urlencode(params)}"
            return RedirectResponse(authorization_url)

        @self.router.get("/auth")
        async def auth(request: Request, code: str, state: str):
            # Validate the state to prevent CSRF attacks
            if state != request.session.get("state"):
                return JSONResponse(
                    status_code=400, content={"detail": "Invalid state"}
                )

            try:
                # Exchange the authorization code for an access token
                async with httpx.AsyncClient() as client:
                    token_response = await client.post(
                        self._token_url,
                        data={
                            "grant_type": "authorization_code",
                            "code": code,
                            "redirect_uri": str(request.url_for("auth")),
                            "client_id": self._client_id,
                            "client_secret": self._client_secret,
                        },
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                    )
                    token_response.raise_for_status()
                    token_data = token_response.json()

                # Store access token and user info in the session
                request.session["access_token"] = token_data["access_token"]

            except httpx.HTTPStatusError:
                return JSONResponse(
                    status_code=400, content={"detail": "OAuth2 token exchange failed"}
                )

            return {"access_token": token_data["access_token"], "token_type": "bearer"}

    async def __call__(self, token: str = Depends(_oauth2_scheme)) -> Dict[str, Any]:
        """Dependency to validate access token with Authentik."""

        # Verify the access token with Authentik's user info endpoint
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    self._user_info_url,
                    headers={"Authorization": f"Bearer {token}"},
                )
                response.raise_for_status()
                user_info = response.json()

            return user_info  # Return user info for further use in routes

        except httpx.HTTPStatusError:
            raise HTTPException(
                status_code=401, detail="Invalid or expired access token"
            )
