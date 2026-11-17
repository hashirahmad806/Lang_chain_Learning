import os
from dotenv import load_dotenv #  from outside of the this directory
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("Google_Gemini_API_KEY")

prompt =PromptTemplate.from_template("Write  a Detail note on the {subject} Topic. {style} language")
prompt_2 = PromptTemplate.from_template("Write  a short summaries of the {note}")

model = ChatGoogleGenerativeAI(model = "gemini-3.8-flash",api_key=api_key)

output_parser = StrOutputParser()

chain = prompt | model | output_parser | prompt_2 | model | output_parser 

result = chain.invoke({"subject" : "AI", "style": "Simple"})

print(result)


chain.get_graph().print_ascii()