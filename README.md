# 📄 AI Document Chatbot

An AI-powered chatbot that allows users to upload PDF or Word documents and ask questions about the content. The chatbot provides clear answers using AI models.

---

## 🔗 Live Demo

Try the chatbot here: [AI Document Chatbot](https://7x70j33f-8501.inc1.devtunnels.ms/)

---

## 📝 Features

- Upload **PDF** or **Word (.docx)** documents.
- Ask multiple questions without re-uploading.
- AI-generated answers based on uploaded documents.
- Clear and interactive chat interface.
- Session-based chat history to track questions and answers.

---

## 💻 Technologies Used

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **AI Model:** Ollama (`llama2`) or OpenAI GPT (replaceable for cloud deployment)  
- **File Parsing:** PyPDF2, python-docx  
- **HTTP Requests:** requests  
- **Deployment:** Streamlit Cloud (frontend), Render (backend)

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-doc-chatbot.git
cd ai-doc-chatbot
