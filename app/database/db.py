import psycopg2
import os 
from dotenv import load_dotenv
from app.utils.logger import logger

load_dotenv()


class Database:

    connection = None

    @staticmethod
    def get_connection():

        if Database.connection is None:

            try:

                Database.connection = psycopg2.connect(
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                    database=os.getenv("DB_NAME"),
                    user=os.getenv("DB_USER"),
                    password=os.getenv("DB_PASSWORD")
                )

                logger.info("Database connected successfully.")

            except Exception as ex:

                logger.exception(ex)
                raise ex

        return Database.connection