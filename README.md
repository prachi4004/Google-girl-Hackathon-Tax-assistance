# Google-girl-Hackathon-Tax-assistance
AI Tax Assistant is a web-based tax automation tool that extracts financial details from Form 16 (PDF), calculates tax liabilities, and provides AI-powered tax guidance using OCR and OpenAI's GPT model. 
# AI Tax Assistant
A web-based AI-powered Tax Assistant that automates **tax filing**, **simplifies complex calculations**, **identifies deductions**, and **minimizes errors** using **OCR and AI**.

## 📌 Features
✅ **Upload Form 16 (PDF) and extract financial details**  
✅ **Automated tax calculation (Salary, Deductions, Tax Deducted, and Tax Liability)**  
✅ **AI Chatbot for tax-related queries**  
✅ **Flask backend for OCR and tax processing**  
✅ **React frontend for an interactive UI**  

---

## 🚀 Tech Stack
- **Frontend:** React.js, Tailwind CSS  
- **Backend:** Flask, Python  
- **OCR & Extraction:** `pdfplumber`, `re (Regex)`
- **AI Integration:** OpenAI API  

---

## 🔧 Installation Guide
### **1️⃣ Clone the Repository**
https://github.com/prachi4004/Google-girl-Hackathon-Tax-assistance.git

2️⃣ Install Backend Dependencies
```bash
pip install -r requirements.txt
```

3️⃣ Install Frontend Dependencies
```bash
npm install
```

4️⃣ Set Up OpenAI API Key
Create a .env file in the backend/ directory.
Add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
``` 

5️⃣ Start Backend (Flask)
```bash
cd backend
python app.py
```
Server runs at: http://127.0.0.1:5000

6️⃣ Start Frontend (React)
```bash
cd frontend
npm start
```
App runs at: http://localhost:3000

📂 Project Structure
ai-tax-assistant/
│── backend/  
│   ├── app.py              # Flask API server  
│   ├── ocr.py              # Extracts financial details from Form 16  
│   ├── tax_calculator.py   # Tax calculations  
│   ├── chatbot.py          # AI-powered tax assistant (ChatGPT API)  
│   ├── requirements.txt    # Backend dependencies  
│   ├── .env                # API keys (ignored in Git)  
│   ├── templates/          # HTML templates (if needed)  
│   └── static/             # Static assets (CSS/JS)  
│  
│── frontend/  
│   ├── src/  
│   │   ├── components/     # React UI components  
│   │   ├── App.js          # Main React App  
│   │   ├── index.js        # Entry point  
│   ├── public/  
│   ├── package.json        # Frontend dependencies  
│   └── .env                # (Optional) Frontend API keys  
│  
└── README.md
🔥 Usage Instructions
📤 Upload a Form 16 (PDF)
1️⃣ Click "Upload Form 16"
2️⃣ The system extracts Salary, Deductions, and Tax Deducted
3️⃣ It calculates Tax Liability

💬 Chat with AI
1️⃣ Ask tax-related queries in the chatbox
2️⃣ AI provides real-time tax advice using OpenAI GPT
