import json
from valyu.data.context_loader import Context, ContextResponse
from pydantic import BaseModel

class LLMResponse(BaseModel):
    response: str
    metadata: ContextResponse | None

class PromptTemplate:
    def __init__(self, template):
        self.template = template

    def enrich_and_invoke(self, context: Context, prompt: str, llm) -> LLMResponse:
        enriched_context = context.fetch_context(prompt)
        if enriched_context:
            context_str = "\n".join([f"{match.text}" 
                                     for i, match in enumerate(enriched_context.top_k_matches)])
            filled_prompt = self.template.format(context=context_str, prompt=prompt)
            llm_response = llm.generate(filled_prompt)
            return LLMResponse(response=llm_response, metadata=enriched_context)
        else:
            llm_response = llm.generate(prompt)
            return LLMResponse(response=llm_response, metadata=None)
