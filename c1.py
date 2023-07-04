from langchain.llms import OpenAI
import configparser
import os

# Create environment variable for OpenAI API key
configparser = configparser.ConfigParser()
configparser.read("config.ini")
os.environ["OPENAI_API_KEY"] = configparser["keys"]["openai"]

llm = OpenAI(model="text-davinci-003", temperature=0.9)

text = "Suggest a personalized workout routine for someone looking to improve cardiovascular endurance and prefers outdoor activities."
print(llm(text))
