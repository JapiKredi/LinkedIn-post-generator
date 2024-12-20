import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Hugging Face settings
HF_TOKEN = os.getenv("HUGGING_FACE_TOKEN")
MODEL_ID = "meta-llama/Llama-2-70b-chat-hf"

# Model settings
MODEL_CONFIG = {
    "temperature": 0.7,
    "max_length": 500,
    "top_p": 0.95,
    "top_k": 50,
    "repetition_penalty": 1.1,
}

# Prompt template
BLOG_GENERATION_PROMPT = """<s>[INST] Based on the following LinkedIn tech blog topics, generate a new, unique LinkedIn blog post about AI or technology:

Topics:
- Model Context Protocol
- AWS and hallucinations in LLMs
- Claude model updates
- AI reasoning and development

Generate a professional LinkedIn post with:
1. An engaging title
2. Main content
3. Relevant hashtags

Your response should be well-structured and professional. [/INST]"""
