from fastapi import FastAPI
import nest_asyncio
# Use a pipeline as a high-level helper
from transformers import pipeline

sentiment_model = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment-latest")


app = FastAPI()

@app.get('/')
async def home():

  return "Welcome to Our FastAPI Endpoints"

@app.get('/sentiment/{text}')
async def sentiment(text):

  return str(sentiment_model(text))

@app.get('/atom')
async def atom():

  return "This is our 2nd endpoint"

@app.get('/inpt/{variable}')
async def inpt(variable):

  return "Wecome to our session " + variable
