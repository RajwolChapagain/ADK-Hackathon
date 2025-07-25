from google.adk import Agent
from . import prompt
import os
import sys
from pathlib import Path
from vertexai import rag

def rag_response(query:str) -> str:
    """
    Retrieves contextually relevant information from a RAG corpus.

    Args:
        query (str): The query string to search within the corpus.

    Returns:
        vertexai.rag.RagRetrievalQueryResponse: The response containing retrieved
        information from the corpus.
    """
    response = rag.retrieval_query(
            rag_resources=[
                rag.RagResource(
                    rag_corpus=os.environ.get('GOOGLE_CLOUD_RAG_RESOURCE'),
                    )
                ],
            text=query,
            )

    return str(response)

MODEL = "gemini-2.5-flash"

root_agent = Agent(
        model=MODEL,
        name="RCC_Structures_Agent_prompt",
        instruction=prompt.RCC_STRUCTURE_AGENT_PROMPT,
        tools=[rag_response]
        )
