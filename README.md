# Stratova

Stratova is an AI agent system designed to leverage local knowledge bases using a Retrieval-Augmented Generation (RAG) architecture. It grounds agent tasks with specific company guidelines and documentation.

## Tech Stack
* **Language:** Python 3.10+
* **Framework:** LangChain
* **Vector Database:** ChromaDB
* **LLM Provider:** OpenAI / Anthropic

---


### Environment Setup
Clone the repository and set up your local isolated environment:

```bash
# Navigate to project
cd Stratova

# Create virtual environment
python -m venv .venv

# Activate environment (Mac)
source venv/bin/activate

# Activate environment (Windows)
.venv\Scripts\Activate.ps1
```

#install requirements 
pip install -r requirements.txt

#### Configure Environment Variables:
Create a file named exactly .env in the root of the project folder. 
Add your OpenAI API key: 
```text
OPENAI_API_KEY= api-key-here
```
⚠️ **Important**: Never commit your .env file to GitHub. It is already included in our .gitignore.
