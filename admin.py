import streamlit as st
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
import os
import tempfile 
from auth import *
from streamlit_pdf_viewer import pdf_viewer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

load_dotenv()
openai_api_key = os.environ["OPENAI_API_KEY"]
embeddings_model = OpenAIEmbeddings(model='text-embedding-3-small')

def initialize_session_state():
    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "generated" not in st.session_state:
        st.session_state["generated"] = ["Hello! 👋 How can I help you?"]

    if "past" not in st.session_state:
        st.session_state["past"] = []

def conversation_chat(query, chain, history):
    result = chain.invoke({
        "query": query
    })
    print(result["result"])
    return result["result"]

def display_chat_history(chain):
    user_input = st.chat_input("Type your question here")
    if user_input:
        fullprompt = user_input + SystemConstants.SYSTEM_MESSAGE
        with st.spinner("Generating response ......"):
            output = conversation_chat(
                query=fullprompt,
                chain=chain,
                history=st.session_state["history"]
            )
        
        st.session_state["past"].append(user_input)
        st.session_state["generated"].append(output)

    if st.session_state["generated"]:   
        for i in range(len(st.session_state["generated"])):
            with st.chat_message("assistant"):
                st.markdown(st.session_state["generated"][i])
            if i < len(st.session_state["past"]):
                with st.chat_message("user"):
                    st.markdown(st.session_state["past"][i])

def create_conversational_chain(vector_store):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = RetrievalQA.from_llm(
    retriever=vector_store.as_retriever(), llm=llm
    )
    return chain

def process_uploaded_files(uploaded_files, option):
    
    for file in uploaded_files:
        file_extension = os.path.splitext(file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(file.read())
            temp_file_path = temp_file.name
        loader = None
        if file_extension == ".pdf":
            loader = PyPDFLoader(temp_file_path)
        else:
            st.sidebar.warning("Unsupported file format, please upload a file with .pdf extension")
        if loader:
            pages = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            splits = text_splitter.split_documents(pages)
            embedding = OpenAIEmbeddings()
            vector_store = Chroma.from_documents(documents=splits, embedding=embedding, persist_directory=option)
            st.sidebar.write("Processing " + file.name)
            print("done")
            print(vector_store._collection.count())
            vector_store.persist()
        with st.sidebar:
            st.write(file.name)
            binary_data = file.getvalue()
            pdf_viewer(input=binary_data, width=500, height=600, key=file.name)
        

def admin(authenticator, name):
    initialize_session_state()
    st.title("ChatBot")
    
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name},")
    option = st.sidebar.selectbox( 
    'Scheme',
     ('retirement', 'healthcare'),
     placeholder= 'Please select a scheme',
     index=None
     )
    if option is None:
        st.sidebar.error("Please choose a scheme")
    else:
        st.sidebar.write(f"Selected: {option}")
    
    uploaded_files = st.sidebar.file_uploader(
        "Upload Files",
        accept_multiple_files=True
        ,key="file_uploader"
    )

    print(uploaded_files)
    
    confirm_upload = st.sidebar.button('Upload Documents')
    if uploaded_files:
        with st.sidebar:
            st.write("Document Count: " + str(len(uploaded_files)))
            process_uploaded_files(uploaded_files, option)          
                        
    if confirm_upload:
        if option == None:
            st.sidebar.error("Please choose a scheme")
        if not uploaded_files:
            st.sidebar.error("Please upload a document")
        elif uploaded_files and option != None:
            st.sidebar.success("Documents saved to knowledge repository.")
            
            
      
    st.sidebar.info(UIConstants.CHATBOT_CONTEXT)
    st.sidebar.info(UIConstants.SUGGESTIONS)
    
    embedding = OpenAIEmbeddings()

    vector_store = Chroma(
        embedding_function=embedding,
        persist_directory=option
    )

    chain = create_conversational_chain(vector_store=vector_store)

    display_chat_history(chain=chain)