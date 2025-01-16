from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['HUGGINGFACEHUB_API_TOKEN'] = os.getenv('HUGGINGFACEHUB_API_TOKEN')

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    task="text-generation",
    max_new_tokens=500,
    temperature=0.5,
    do_sample=False,
)

# Create prompt template
template = """You are a secretary to a departmental meeting. Your task is to write a discussion\
            notes that highlighting important discussions, facts and decision.\
            Tabulate facts and figure where possible."

INPUT: {input}

NOTE:"""

prompt = ChatPromptTemplate.from_template(template)

f = open("/home/abi/nfs/work_space/minutes/shred/2a.txt", "r")
input = f.read()

# Create the RAG chain using LCEL with prompt printing and streaming output
rag_chain = (
    {"input": RunnablePassthrough()}
    | prompt
    | llm
)

with open("/home/abi/nfs/work_space/minutes/out/ollama.txt", "w", encoding="utf-8") as file:
    # Run the Llama model
    for chunk in rag_chain.stream(input):
        file.write(chunk)