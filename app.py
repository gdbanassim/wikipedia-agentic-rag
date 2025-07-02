import os
import streamlit as st
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")




# Streamlit UI
st.set_page_config(page_title="Wikipedia RAG Bot", layout="centered")
st.title("📚 Wikipedia RAG Bot")
st.markdown("Ask anything and get answers based on real-time Wikipedia summaries.")

# Input from user
query = st.text_input("Ask a question:", "")

if query:
    with st.spinner("Searching Wikipedia..."):
        # Wikipedia wrapper
        wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)

        # Tool for Wikipedia
        wikipedia_tool = Tool(
            name="Wikipedia",
            func=WikipediaQueryRun(api_wrapper=wiki_wrapper).run,
            description="Useful for answering general knowledge questions using Wikipedia"
        )

        # Language model
        llm = ChatGroq(temperature=0, model="qwen-qwq-32b", api_key=api_key)

        # Initialize agent with Wikipedia tool
        agent = initialize_agent(
            tools=[wikipedia_tool],
            llm=llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=False
        )
        # Get the response
        response = agent.run(query)

        # Display the result
        st.success("Answer:")
        st.markdown(f"**{query.capitalize()}**\n\n{response}")



