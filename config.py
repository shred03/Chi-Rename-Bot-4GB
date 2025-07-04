import os
from dotenv import load_dotenv

load_dotenv();

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN = int(os.environ.get("ADMIN"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", -1002728630709)
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1002547512665))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://jpcdn.it/img/small/469daf5c808c9fa434b286e9d90573bd.jpg")
