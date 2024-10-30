import json
import requests

# Mapping of model names to Bedrock model IDs
MODEL_ID_MAPPING = {
    "claude-3-sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "claude-3-haiku": "anthropic.claude-3-haiku-20240307-v1:0",
    "mistral-large": "mistral.mistral-large-2402-v1:0",
    "llama3-8b": "meta.llama3-8b-instruct-v1:0",
    "llama3-70b": "meta.llama3-70b-instruct-v1:0",
}

class ChatLLM:
    def __init__(self, model):
        self.model = model
        self.system_prompt = """
            You are a helpful AI assistant. 
            You will be provided with multiple pieces of context and a question. 
            You must answer the question based on the context, however you must not disclose that you have been provided with context. I.e. do not say 'Based on the context provided...' or anything similar.
        """
        self.api_endpoint = "https://sddq61xena.execute-api.eu-west-2.amazonaws.com"

    def generate(self, prompt):
        # Prepare the request body for the API
        request_body = {
            "user_prompt": prompt,
            "system_prompt": self.system_prompt
        }

        # Make the API request
        response = requests.post(
            self.api_endpoint,
            json=request_body,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")

        response_data = response.json()
        return response_data["response"]
