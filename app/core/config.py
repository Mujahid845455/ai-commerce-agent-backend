from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str = "sqlite:///./sql_app.db"

    JWT_SECRET: str = "agentpay-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"

    RAZORPAY_KEY_ID: str = ""
    RAZORPAY_KEY_SECRET: str = ""

    GEMINI_API_KEY: str = ""

    APP_ENV: str = "development"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()