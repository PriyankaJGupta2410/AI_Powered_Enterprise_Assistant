import os

import psycopg2
from dotenv import load_dotenv

from app.utils.logger import logger

load_dotenv()


class DatabaseConnection:

    @staticmethod
    def get_connection():

        try:

            connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )

            return connection

        except Exception as e:

            logger.error(f"Database Connection Error : {e}")

            raise