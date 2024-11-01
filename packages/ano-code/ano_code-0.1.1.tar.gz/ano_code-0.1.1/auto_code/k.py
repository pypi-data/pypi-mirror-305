from langchain_community.document_loaders import DirectoryLoader
from ai_assistant.llm_cli import openai_client
from ai_assistant.prompt_llm import AIAssistant
from ai_assistant.consts import COMMANDS
DATA_PATH = "./documents"



def generate_data_store():
    code = get_code()
    result = prompt(code)
    return result


def get_code():
    documents = load_documents()
    document_content = []
    for document_index, document in enumerate(documents):
        document_content.append(document.page_content)
    
    data = " ".join(document_content)
    return data

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents


def prompt(code: str):
    assistant = AIAssistant(openai_client)
    result = assistant.run_assistant(code, COMMANDS["w_doc"])
    return result


