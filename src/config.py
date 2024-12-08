import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_PATH = "path/to/your/llama-2-7b.gguf"  # Update with your model path

# Model settings
MODEL_CONFIG = {"n_ctx": 2048, "n_threads": 4, "temperature": 0.7, "max_tokens": 500}

# Prompt template
BLOG_GENERATION_PROMPT = """Based on the following LinkedIn tech blog topics, generate a new, unique LinkedIn blog post about AI or technology:

Topics:
- Model Context Protocol
- AWS and hallucinations in LLMs
- Claude model updates
- AI reasoning and development

Generate a professional LinkedIn post with:
1. An engaging title
2. Main content
3. Relevant hashtags

Post:
"""
