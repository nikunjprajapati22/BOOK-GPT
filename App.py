import os
from API_KEY import Mykey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

llm = OpenAI(temperature=0, openai_api_key = Mykey,verbose=True)
st.title('🦜🔗Book GPT ')
file = st.file_uploader("Choose a Book from you have questions", accept_multiple_files=False)
if file is not None:
    file_details = {"FileName":file.name,"FileType":file.type}
    #st.write(file_details)
    file_path = os.path.abspath(file.name)

#print(file_path)


#prompt templates
loader = TextLoader(file_path,encoding="utf8")
doc = loader.load()
#print(f'you have {len(doc)} document')
#print(f'you have {len(doc[0].page_content)} characters in that document')

text_splitter = RecursiveCharacterTextSplitter(chunk_size=3000, chunk_overlap= 400)
docs = text_splitter.split_documents(doc)

#get the total number of characters so we can average it later
num_total_characters = sum([len(x.page_content) for x in docs])
#print (f"Now you have {len(docs)} documents that have an average of {num_total_characters / len(docs):,.0f} characters (smaller pieces)")

#get your embeddings engine ready
embeddings = OpenAIEmbeddings(openai_api_key = Mykey)

'''#memory
title_memory = ConversationBufferMemory(input_key = 'topic', memory_key = 'chat_history')
script_memory = ConversationBufferMemory(input_key = 'title', memory_key = 'chat_history')

#llms
llm = OpenAI(temperature = 0.9)
title_chain = LLMChain(llm=llm, prompt=title_template,verbose=True, output_key='title', memory = title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template,verbose=True, output_key='script',memory= script_memory)

wiki = WikipediaAPIWrapper()


#showTime

if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    st.write(script)

    with st.expander('Title History'):
        st.info(title_memory.buffer)

    with st.expander('Script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'):
        st.info(wiki_research)
'''