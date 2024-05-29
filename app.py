import streamlit as st 
from streamlit_modal import Modal
import os 
import pandas as pd 
st.set_page_config(layout="wide", page_icon="<3")
st.title("Question Answer with CSV Using Langchain SQL Agent")
st.write("------------")

UPLOAD_FOLDER = 'uploaded_csv'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

file_list = os.listdir(UPLOAD_FOLDER)

st.sidebar.title("QnA CSV")
option=st.sidebar.selectbox("select file from dropdow", file_list, placeholder="please select an file", index=None, key="selectbox")
if option:
    st.write(option,"file selected")


c1, c2= st.columns([8,1])
modal = Modal(key="Demo_Key",title="test")
for col in st.columns(8):
    with col:
        open_modal = c2.button(label='Upload file', key="uploadd_button")
        if open_modal:
            with modal.container():
                file = st.file_uploader("Choose a file", type="csv", key="Csv_uploader")
                submit=st.button("Submit", key="file_submit")
    
                if submit:
                    st.write("file added ")
                if file is not None and submit:
                    # Display the name of the uploaded file
                    st.write("File uploaded:", file.name)

                    # Create the full path to save the file
                    save_path = os.path.join(UPLOAD_FOLDER, file.name)

                    # Read the file as a pandas DataFrame (optional, depends on your use case)
                    df = pd.read_csv(file)

                    # Save the uploaded file to the specified folder
                    with open(save_path, "wb") as f:
                        f.write(file.getbuffer())

                    st.write(f"File saved at: {save_path}, now you can close the model")
