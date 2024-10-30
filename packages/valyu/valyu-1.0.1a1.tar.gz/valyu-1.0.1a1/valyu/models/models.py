import json
import boto3

# Mapping of model names to Bedrock model IDs
MODEL_ID_MAPPING = {
    "claude-3-sonnet": "anthropic.claude-3-sonnet-20240229-v1:0",
    "claude-3-haiku": "anthropic.claude-3-haiku-20240307-v1:0",
    "mistral-large": "mistral.mistral-large-2402-v1:0",
    "llama3-8b": "meta.llama3-8b-instruct-v1:0",
    "llama3-70b": "meta.llama3-70b-instruct-v1:0",
}

# Initialize Bedrock client
bedrock_client = boto3.client("bedrock-runtime", region_name="eu-west-2")

class ChatLLM:
    def __init__(self, model):
        self.model = model
        self.system_prompt = """
            You are a helpful AI assistant. 
            You will be provided with multiple pieces of context and a question. 
            You must answer the question based on the context, however you must not disclose that you have been provided with context. I.e. do not say 'Based on the context provided...' or anything similar.
        """
        self.model_id = MODEL_ID_MAPPING.get(model, model)

    def generate(self, prompt):
        # Prepare the request body for Bedrock
        native_request = {
            "max_tokens": 1024,
            "temperature": 0.5,
            "top_p": 1,
            "system": self.system_prompt,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt
                        }
                    ]
                }
            ]
        }

        if "anthropic" in self.model_id:
            native_request["anthropic_version"] = "bedrock-2023-05-31"

        response = bedrock_client.invoke_model(
            modelId=self.model_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps(native_request)
        )

        response_body = json.loads(response["body"].read())
        generated_text = response_body["content"][0]["text"]

        return generated_text
