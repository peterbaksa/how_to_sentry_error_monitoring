import os
from fastapi import FastAPI
import sentry_sdk
from dotenv import load_dotenv
from src.common.file_handler import get_cwd


_CWD = get_cwd("how_to_sentry_error_monitoring")
load_dotenv(dotenv_path=_CWD + "/.env")

sentry_public_key = os.getenv("SENTRY_PUBLIC_KEY")
sentry_company_id = os.getenv("SENTRY_COMPANY_ID")
sentry_project_id = os.getenv("SENTRY_PROJECT_ID")

sentry_sdk.init(
    dsn=f"https://{sentry_public_key}@{sentry_company_id}.ingest.de.sentry.io/{sentry_project_id}",
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/error")
def error():
    1/0  # Error (not handled exception)





