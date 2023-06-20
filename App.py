import os
from API_KEY import Mykey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = Mykey

#App framework
st.title('🦜🔗 GPT ')
prompt = st.text_input('plug in your Prompt here')