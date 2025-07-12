from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    invoices_dir: str

    class Config:
        env_file = "../.env"
