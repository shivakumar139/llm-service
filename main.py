from fastapi import FastAPI
from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_google_genai import ChatGoogleGenerativeAI
import os


os.environ["GOOGLE_API_KEY"] = "AIzaSyDLx6ZV79xqe7IttVYxI2ceYOIf-_Vd1Xk"

app = FastAPI()


@app.get("/")
def root():

    db = SQLDatabase.from_uri("mysql+mysqlconnector://root:root@127.0.0.1:8083/test")
    print("dia", db.dialect)
    print(db.get_usable_table_names())

    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    chain = create_sql_query_chain(llm, db)
    response = chain.invoke({"question": "How many movies are there"})
   
    return {"message": response}


