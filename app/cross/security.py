# type: ignore
from typing import List, Dict, Optional

import requests

from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from starlette.status import HTTP_403_FORBIDDEN
from typing import Any

from app.settings.globals import COGNITO_POOL_ID, COGNITO_REGION
from jose import jwt, jwk, JWTError
from jose.utils import base64url_decode
from starlette.requests import Request

from app.db.session import Session
from app.cross.db import get_db
from app.repositories.user import user_repo
from app.models.orm.user import User


JWK = Dict[str, str]


class JWKS(BaseModel):
    keys: List[JWK]


json_web_key_set = JWKS.parse_obj(
    requests.get(
        f"https://cognito-idp.{COGNITO_REGION}.amazonaws.com/"
        f"{COGNITO_POOL_ID}/.well-known/jwks.json"
    ).json()
)


class JWTAuthorizationCredentials(BaseModel):
    jwt_token: str
    header: Dict[str, str]
    claims: Dict[str, Any]
    signature: str
    message: str


class JWTBearer(HTTPBearer):
    def __init__(self, jwks: JWKS, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

        self.kid_to_jwk = {jwk["kid"]: jwk for jwk in jwks.keys}

    def verify_jwk_token(self, jwt_credentials: JWTAuthorizationCredentials) -> bool:
        try:
            public_key = self.kid_to_jwk[jwt_credentials.header["kid"]]
        except KeyError:
            raise HTTPException(
                status_code=HTTP_403_FORBIDDEN, detail="JWK public key not found"
            )

        key = jwk.construct(public_key)
        decoded_signature = base64url_decode(jwt_credentials.signature.encode())

        return key.verify(jwt_credentials.message.encode(), decoded_signature)

    async def __call__(self, request: Request) -> Optional[JWTAuthorizationCredentials]:
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Wrong authentication method"
                )

            jwt_token = credentials.credentials

            message, signature = jwt_token.rsplit(".", 1)

            try:
                jwt_credentials = JWTAuthorizationCredentials(
                    jwt_token=jwt_token,
                    header=jwt.get_unverified_header(jwt_token),
                    claims=jwt.get_unverified_claims(jwt_token),
                    signature=signature,
                    message=message,
                )
            except JWTError:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="JWK invalid"
                )

            if not self.verify_jwk_token(jwt_credentials):
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="JWK invalid"
                )

            return jwt_credentials


auth = JWTBearer(json_web_key_set)


async def get_auth_user_id(
    credentials: JWTAuthorizationCredentials = Depends(auth),
    db: Session = Depends(get_db),
) -> str:
    try:
        user_id = credentials.claims["sub"]
        username = credentials.claims["username"]
        user = user_repo.find(db=db, model_id=user_id)
        if not user:
            user = User(id=user_id, username=username)
            db.add(user)
            db.commit()

        return user_id
    except KeyError:
        HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Username missing")
