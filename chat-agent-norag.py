import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from datasets import load_dataset


os.environ["GOOGLE_API_KEY"] = "AIzaSyB7nA1LwaELV-C7kiRMDDq4t1-QGuV2bCU"

#dataset = load_dataset("text", data_dir="data/books")

# OpenAI Key: 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
chat = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
response = chat.invoke(
    [
        SystemMessage(content="Answer only in japanese"),
        HumanMessage(content="Is apple a fruit?"),
    ]
)

#print(dataset[0])
print(response.content)