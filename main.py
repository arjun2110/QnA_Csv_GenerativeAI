import streamlit as st

# Function to handle Frame 1
def frame1():
    st.title("Frame 1")
    st.sidebar.header("Sidebar")
    st.sidebar.write("Note: Select a file to upload")
    
    file = st.sidebar.file_uploader("Choose a file")
    
    if file is not None:
        st.write("File uploaded:", file.name)
    
    dropdown = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.write(f"Dropdown selection: {dropdown}")
    
    if st.button("Button"):
        st.write("Button clicked!")
    
    if file:
        st.write("Processing the uploaded file...")
        # Add file processing logic here

# Function to handle Frame 2
def frame2():
    st.title("Frame 2 - Model")
    
    st.write("Upload files for model processing")
    model_file1 = st.file_uploader("Upload File 1")
    model_file2 = st.file_uploader("Upload File 2")
    
    if st.button("Submit"):
        if model_file1 is not None and model_file2 is not None:
            st.write("Files uploaded:")
            st.write("File 1:", model_file1.name)
            st.write("File 2:", model_file2.name)
            # Add model processing logic here
        else:
            st.write("Please upload both files before submitting.")

# Function to handle Frame 3
def frame3():
    st.title("Frame 3")
    st.sidebar.header("Sidebar")
    
    st.write("Enter text and upload a file")
    text_input = st.text_input("Text Input")
    file_input = st.file_uploader("File Inputrrrr")
    
    if st.button("Submit"):
        if text_input and file_input:
            st.write("Text entered:", text_input)
            st.write("File uploaded:", file_input.name)
            # Add text and file handling logic here
        else:
            st.write("Plzx ease enter text and upload a file before submitting.")

# Main function to control navigation
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Frame 1", "Frame 2", "Frame 3"])
    
    if page == "Frame 1":
        frame1()
    elif page == "Frame 2":
        frame2()
    elif page == "Frame 3":
        frame3()

if __name__ == "__main__":
    main()
