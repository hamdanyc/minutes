from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
import os

# Create Ollama language model - Gemma 2
local_llm = 'gemma2:2b'

llm = ChatOllama(model=local_llm,
                 keep_alive="3h", 
                 max_tokens=1500,  
                 temperature=0.6)

f = open("/home/abi/nfs/work_space/minutes/shred/2a.txt", "r")
text = f.read()
with open("/home/abi/nfs/work_space/minutes/out/ollama.txt", "w", encoding="utf-8") as file:
    # Run the Llama model
    ai_msg = llm.invoke([(
        "system", "You are a secretary to a departmental meeting. Your task is to write a discussion\
            notes that highlighting important discussions, facts and decision.\
            Tabulate facts and figure where possible.",
            ),
            ("human", text),
        ])
    file.write(ai_msg)