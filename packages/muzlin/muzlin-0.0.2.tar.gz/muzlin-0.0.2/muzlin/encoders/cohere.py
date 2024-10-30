import os
from typing import List, Optional

import cohere

from muzlin.encoders import BaseEncoder
from muzlin.utils.defaults import EncoderDefault

# Code adapted from https://github.com/aurelio-labs/semantic-router/blob/main/semantic_router/encoders/cohere.py


class CohereEncoder(BaseEncoder):
    client: Optional[cohere.Client] = None
    type: str = 'cohere'
    input_type: Optional[str] = 'search_query'

    def __init__(
        self,
        name: Optional[str] = None,
        cohere_api_key: Optional[str] = None,
        input_type: Optional[str] = 'search_query',
    ):
        if name is None:
            name = EncoderDefault.COHERE.value['embedding_model']
        super().__init__(
            name=name,
            input_type=input_type,  # type: ignore
        )
        self.input_type = input_type
        cohere_api_key = cohere_api_key or os.getenv('COHERE_API_KEY')
        if cohere_api_key is None:
            raise ValueError("Cohere API key cannot be 'None'.")
        try:
            self.client = cohere.Client(cohere_api_key)
        except Exception as e:
            raise ValueError(
                f"Cohere API client failed to initialize. Error: {e}"
            ) from e

    def __call__(self, docs: List[str]) -> List[List[float]]:
        if self.client is None:
            raise ValueError('Cohere client is not initialized.')
        try:
            embeds = self.client.embed(
                docs, input_type=self.input_type, model=self.name
            )
            return embeds.embeddings
        except Exception as e:
            raise ValueError(f"Cohere API call failed. Error: {e}") from e
