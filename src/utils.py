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

def optimización_hiperparametros_Reg_logistica():
  
  from sklearn.model_selection import GridSearchCV
hyperparams = {
    "C": [0.001, 0.01, 0.1, 1, 10, 100, 1000],
    "penalty": ["l1", "l2", "elasticnet", None],
    "solver": ["newton-cg", "lbfgs", "liblinear", "sag", "saga"]
}

grid = GridSearchCV(model,hyperparams,scoring='accuracy',cv=5)
}

grid = GridSearchCV(model,hyperparams,scoring='accuracy',cv=5)