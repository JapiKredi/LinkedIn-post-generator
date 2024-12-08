from src.model import LlamaModel
from src.config import BLOG_GENERATION_PROMPT


class PostGenerator:
    def __init__(self):
        self.model = LlamaModel()

    def generate_post(self) -> str:
        """Generate a new blog post."""
        try:
            return self.model.generate_completion(BLOG_GENERATION_PROMPT)
        except Exception as e:
            raise Exception(f"Error generating post: {str(e)}")
