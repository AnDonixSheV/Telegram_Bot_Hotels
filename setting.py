
import os
from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr, StrictStr

load_dotenv()


class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv('SITE_API', None)
    api_host: StrictStr = os.getenv('HOST_API', None)
    token_key: SecretStr = os.getenv('TOKEN_TG', None)
