import json
import requests
from pydantic import BaseModel
from typing import List, Dict, Any
import os

API_ENDPOINT = 'https://sz28eh10ye.execute-api.eu-west-2.amazonaws.com/query'

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

    def fetch_context(self, query: str) -> ContextResponse:
        try:
            print(f"Fetching context for query: {query}\n")
            payload = {
                "query": query
            }
            
            print(f"Sending payload: {json.dumps(payload, indent=2)}")
            
            headers = {
                'Content-Type': 'application/json'
            }
            
            response = requests.post(
                API_ENDPOINT, 
                json=payload,
                headers=headers
            )
            
            response.raise_for_status()
            
            data = response.json()
            print(f"Response data: {data}")

            if "results" in data:
                matches = [ContextMatch(
                    id=match['_id'],
                    index=match['_index'],
                    score=match['_score'],
                    text=match['_source']['text']
                ) for match in data['results'][:self.top_k]]
                return ContextResponse(top_k_matches=matches)
            else:
                print("Unexpected response format")
                return None
        except Exception as e:
            print(f"Error fetching context: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Error response: {e.response.text}")
            return None
