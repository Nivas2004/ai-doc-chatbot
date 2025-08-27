import streamlit as st
import requests
import uuid
st.set_page_config(page_title="AI Document Chatbot", page_icon="🤖", layout="wide")
st.title("📄 AI Document Chatbot")
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
with st.sidebar:
    st.header("Instructions")
    st.write("""
    1. Upload a PDF or Word document once.
    2. Ask multiple questions without re-uploading.
    3. Click **Ask** to get AI-generated answers.
    """)
uploaded_file = st.file_uploader("Upload PDF or Word document", type=["pdf", "docx"])
if uploaded_file:
    if st.button("Upload Document"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        data = {"session_id": st.session_state.session_id}
        try:
            response = requests.post("http://127.0.0.1:8000/upload/", files=files, data=data)
            st.success(response.json().get("message", "Uploaded successfully."))
        except Exception as e:
            st.error(f"Upload failed: {str(e)}")
query = st.text_input("Enter your question:")
if st.button("Ask"):
    if not query:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing..."):
            try:
                data = {"session_id": st.session_state.session_id, "query": query}
                response = requests.post("http://127.0.0.1:8000/chat/", data=data)
                answer = response.json().get("answer", "No answer returned.")
                answer_formatted = answer.replace("\n", "  \n")
                st.session_state.chat_history.append(("You", query))
                st.session_state.chat_history.append(("AI", answer_formatted))
            except Exception as e:
                st.error(f"Error connecting to backend: {str(e)}")
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"""
            <div style="display:flex; justify-content:flex-end; margin:5px 0;">
                <div style="
                    background-color:#DCF8C6;
                    color:#000000;
                    padding:12px;
                    border-radius:15px;
                    max-width:70%;
                    word-wrap:break-word;
                    box-shadow:1px 1px 3px rgba(0,0,0,0.1);
                ">
                    <strong>You:</strong> {message}
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="display:flex; justify-content:flex-start; margin:5px 0;">
                <div style="
                    background-color:#F1F0F0;
                    color:#000000;
                    padding:12px;
                    border-radius:15px;
                    max-width:70%;
                    word-wrap:break-word;
                    box-shadow:1px 1px 3px rgba(0,0,0,0.1);
                ">
                    <strong>AI:</strong>  
                    {message}
                </div>
            </div>
        """, unsafe_allow_html=True)
st.markdown("<script>window.scrollTo(0, document.body.scrollHeight);</script>", unsafe_allow_html=True)
