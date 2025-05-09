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

# Create the RAG chain using LCEL with prompt printing and streaming output
rag_chain = (
    {"input": RunnablePassthrough()}
    | prompt
    | llm
)

# file path
input_directory = "/home/abi/nfs/work_space/minutes/script"
output_directory = "/home/abi/nfs/work_space/minutes/res"

# Get the input files from the input-dir
input_files = os.listdir(input_directory)

# Remove existing files from the output directory
for filename in os.listdir(output_directory):
    file_path = os.path.join(output_directory, filename)
    os.remove(file_path)

# Loop over the input files
for input_file in input_files:
    # Get the input text from the file
    with open(f"{input_directory}/{input_file}", "r") as f:
        input = f.read()

    # Save the response text to output_directory
    with open(f"{output_directory}/{input_file}", "w", encoding="utf-8") as file:
        for chunk in rag_chain.stream(input):
            file.write(chunk)