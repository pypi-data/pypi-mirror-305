import json
import requests
from pydantic import BaseModel
from typing import List, Dict, Any
import os
import boto3

LAMBDA_ARN = 'arn:aws:lambda:eu-west-2:627665855519:function:dev-lambda-arxivsearch'

class ContextMatch(BaseModel):
    id: str
    index: str
    score: float
    text: str

class ContextResponse(BaseModel):
    top_k_matches: List[ContextMatch]

class Context:
    def __init__(self, data_sources, credit_budget):
        self.data_sources = data_sources
        self.credit_budget = credit_budget
        self.top_k = 2
        self.lambda_client = boto3.client('lambda', region_name='eu-west-2')

    def fetch_context(self, query: str) -> ContextResponse:
        try:
            print(f"Fetching context for query: {query}\n")
            payload = {
                "query": query,
                "budget": 1000,
                "db_store": [source for source in self.data_sources],
                "top_k": self.top_k
            }
            
            response = self.lambda_client.invoke(
                FunctionName=LAMBDA_ARN,
                InvocationType='RequestResponse',
                Payload=json.dumps(payload)
            )
            
            data = json.loads(response['Payload'].read())
            body = json.loads(data['body'])
            print(f"Response data: {data}")

            if "results" in body:
                matches = [ContextMatch(
                    id=match['_id'],
                    index=match['_index'],
                    score=match['_score'],
                    text=match['_source']['text']
                ) for match in body['results'][:self.top_k]]
                return ContextResponse(top_k_matches=matches)
            else:
                print("Unexpected response format")
                return None
        except Exception as e:
            print(f"Error fetching context: {e}")
            return None
