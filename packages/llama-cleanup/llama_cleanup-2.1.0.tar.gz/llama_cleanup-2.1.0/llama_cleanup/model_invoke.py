import re
import json
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI

def initialize_model(remote, llama_model, remote_api_base=None, remote_api_key=None):
    try:
        if not remote:
            return OllamaLLM(model=llama_model)
        elif remote and remote_api_base:
            return ChatOpenAI(
                openai_api_base=remote_api_base,
                openai_api_key=remote_api_key or 'NA',
                model_name=llama_model
            )
        else:
            raise ValueError("For remote model, 'remote_api_base' and 'llama_model' must be provided.")
    except Exception as e:
        return None

def invoke_model(llm, prompt):
    try:
        response = llm.invoke(prompt) if hasattr(llm, 'invoke') else llm({"prompt": prompt})
        
        # Extract JSON object from the response
        json_match = re.search(r'\{.*?\}', response, re.DOTALL) if response else None
        
        if json_match:
            json_text = json_match.group(0)
            return json.loads(json_text)
        else:
            return None

    except Exception as e:
        return None

