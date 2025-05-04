from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/assessments")
def get_assessments():
    df = pd.read_pickle("assessment_data.pkl")
    return df.to_dict(orient="records")
