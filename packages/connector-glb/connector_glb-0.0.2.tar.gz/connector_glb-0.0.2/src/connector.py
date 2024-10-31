# pip install psycopg2 pymysql sqlalchemy python-dotenv
from sqlalchemy import create_engine
from os import getenv
from pandas import read_sql
from dotenv import load_dotenv

class Connector:
    def __init__(self, arquivo_env):

        load_dotenv(arquivo_env, override=True)
        
        self.db_host = getenv("DB_HOST")
        self.db_port = getenv("DB_PORT")
        self.db_name = getenv("DB_NAME")
        self.db_user = getenv("DB_USER")
        self.db_pass = getenv("DB_PASS")

        self.string_connection = f"{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"

        self.db_engine = self.build_engine()
    
    def build_engine(self):
        return create_engine(f"postgresql://{self.string_connection}")

    def perform_select(self, query: str):
        df = read_sql(query, con=self.db_engine)
        return df
