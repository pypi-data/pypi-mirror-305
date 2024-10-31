from datetime import datetime
from typing import Any

from injection.testing import test_singleton

from hundred.services.authenticator import JWTAuthenticator, StatelessAuthenticator


@test_singleton(on=StatelessAuthenticator, inject=False, mode="fallback")
class TestJWTAuthenticator(StatelessAuthenticator):
    __slots__ = ("__jwt",)

    def __init__(self) -> None:
        self.__jwt = JWTAuthenticator("TEST_SECRET_KEY")

    def generate_token(
        self,
        data: dict[str, Any],
        expiration: datetime | None = None,
    ) -> str:
        return self.__jwt.generate_token(data, expiration)

    def authenticate(self, token: str) -> dict[str, Any]:
        return self.__jwt.authenticate(token, ignores_expiration=True)
