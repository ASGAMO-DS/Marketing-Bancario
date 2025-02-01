from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine

def valores_duplicados(df):
    for columna in df.columns:
        suma = df[columna].duplicated().sum()
        print(f'en la columna {columna} hay {suma} valores duplicados')
    