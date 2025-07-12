from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    invoices_dir: str
    template_path: str

    class Config:
        env_file = "../.env"


settings = Settings()
