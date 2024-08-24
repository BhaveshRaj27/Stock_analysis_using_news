import os
import streamlit as st
import shutil
import time 
import pickle 
import langchain 
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader 
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

#take all the environment variable from .env file and load them into environment
from dotenv import load_dotenv
load_dotenv()

st.title("News Research tool")

st.sidebar.title('News Article URLs')

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

file_path = "faiss_index"

main_placeholder = st.empty()
llm = OpenAI(temperature=0.6, max_tokens=1000)

if process_url_clicked:
    loader = UnstructuredURLLoader(urls = urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()

    #Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n','\n','.',','],
        chunk_size = 1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs =  text_splitter.split_documents(data)

    #creating embedding and saving it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai =  FAISS.from_documents(docs,embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    # with open(file_path, "wb") as f:
    #     pickle.dump(vectorstore_openai, f)
    if os.path.exists(file_path):
        shutil.rmtree(file_path)
    vectorstore_openai.save_local(file_path)
   

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        embeddings = OpenAIEmbeddings()
        vectorIndex = FAISS.load_local(file_path, embeddings, allow_dangerous_deserialization=True)
    #     with open(file_path, "rb") as f:
    # vectorstore = pickle.load(f)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorIndex.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
        # result will be a dictionary of this format --> {"answer": "", "sources": [] }
        st.header("Answer")
        st.write(result["answer"])

        # Display sources, if available
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  # Split the sources by newline
            for source in sources_list:
                st.write(source)