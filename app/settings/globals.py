from pathlib import Path

from starlette.config import Config

from app.utils import _TESTING


p: Path
if _TESTING:
    p = Path(__file__).parents[2] / ".env.test"
else:
    p = Path(__file__).parents[2] / ".env"

config: Config
if p.exists():
    config = Config(str(p))
else:
    config = Config()

DATABASE_URL: str = config(
    "DATABASE_URL",
    cast=str,
    default="postgresql+psycopg2://postgres:postgres@localhost/challenge",
)
# fmt: off
COGNITO_POOL_ID: str = config("COGNITO_POOL_ID", cast=str, default="us-east-1_NozQxDzdH")
# fmt: on
COGNITO_REGION: str = config("COGNITO_REGION", cast=str, default="us-east-1")
