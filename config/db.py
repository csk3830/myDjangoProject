import json
import os
import psycopg2

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "setting.json")
with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
    config = json.load(f)

def get_db_connection():
    conn = psycopg2.connect(
        dbname=config["DB"]["DBName"],
        user=config["DB"]["DBUser"],
        password=config["DB"]["DBPwd"],
        host=config["DB"]["DBHost"],
        port=config["DB"]["DBPort"]
    )
    return conn