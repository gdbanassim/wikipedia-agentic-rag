# Wikipedia Agentic RAG 

A lightweight, real-time agent that retrieves factual answers from Wikipedia and generates natural responses using a Groq-hosted LLM via LangChain.


## 🚀 Features
- 🧠 Retrieval-Augmented Generation (RAG) using Wikipedia
- 🤖 Uses Groq API with the `qwen-qwq-32b` model for fast, accurate responses
- 🌐 Built with LangChain and Streamlit
- 🔍 Automatically retrieves summaries from Wikipedia based on the user's question

## 🛠️ Tech Stack
| Component               | Description                                      |
|------------------------|--------------------------------------------------|
| LangChain              | Framework to build LLM pipelines                 |
| langchain_community    | For Wikipedia query and tool wrappers            |
| langchain_groq         | For connecting to Groq-hosted LLMs               |
| Streamlit              | Web UI for asking questions and showing answers  |
| WikipediaAPIWrapper    | Fetches relevant summaries from Wikipedia        |
| dotenv                 | Securely loads API keys from .env file           |

## 📁 Project Structure
```
wikipedia_rag_bot/
├── app.py                  # Main Streamlit app
├── .env                    # Contains your Groq API key
└── requirements.txt        # Python dependencies
```

## 🧾 Requirements
Install dependencies:
```
pip install streamlit langchain langchain-community langchain-groq wikipedia python-dotenv
```

## 🔐 .env File
Create a `.env` file in the root directory with your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

## 📜 How It Works
1. User enters a question via the Streamlit interface.
2. `WikipediaAPIWrapper` fetches a relevant summary from Wikipedia.
3. The `WikipediaQueryRun` tool is registered as a LangChain Tool.
4. Groq's `Qwen-QWQ-32B` model is used through `ChatGroq`.
5. An agent is initialized using `ZERO_SHOT_REACT_DESCRIPTION`.
6. The agent uses Wikipedia content and the LLM to generate a contextual response.
7. The final answer is shown in the app.

## 🧪 Example
**User asks:**
> "Tell me about black holes"

**Bot responds (summarized from Wikipedia):**
> "A black hole is a region of spacetime exhibiting gravitational acceleration so strong that nothing—no particles or even electromagnetic radiation such as light—can escape from it..."
