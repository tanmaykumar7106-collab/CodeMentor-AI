# 💡 CodeMentor AI

> **AI-Powered Coding, Testing & Learning Assistant** built with **IBM Granite**, **Python**, and **Streamlit**.

CodeMentor AI is an AI-powered desktop application that helps students and developers improve their programming skills by generating software test cases, reviewing source code, and providing guided solutions for coding problems.

---

## ✨ Features

### 🧪 Test Generator

Generate comprehensive software test cases from source code.

* Functional Test Cases
* Boundary Test Cases
* Edge Cases
* Negative Test Cases
* Expected Outputs
* Priority Classification
* CSV & Markdown Export

---

### 💡 Code Analyzer

Analyze your code and receive AI-powered feedback.

* Code Explanation
* Logic Review
* Improvement Suggestions
* Optimized Code
* Time Complexity Analysis
* Space Complexity Analysis
* Learning Tips

---

### 🎯 Problem Solver

A guided assistant for coding interview and DSA practice.

Choose your preferred help level:

* 💭 Hint Only
* 📖 Approach
* ✅ Complete Solution

Includes:

* Problem Explanation
* Input & Output Analysis
* Constraints
* Brute Force Approach
* Optimized Approach
* Dry Run
* Complexity Analysis
* Test Cases
* Final Code (Complete Solution mode only)

---

## 🚀 Tech Stack

### Frontend

* Streamlit
* Streamlit Ace

### Backend

* Python

### AI

* IBM Granite (Ollama)

### Libraries

* Pandas
* Matplotlib
* Requests

---

## 📂 Project Structure

```text
CodeMentor-AI/
│
├── app.py
├── requirements.txt
│
├── features/
│   ├── test_generator.py
│   ├── code_analyzer.py
│   └── problem_solver.py
│
├── prompts/
│   ├── test_case.py
│   ├── review.py
│   └── problem.py
│
├── services/
│   └── llm.py
│
├── ui/
│   ├── dashboard.py
│   ├── metrics.py
│   ├── table.py
│   └── charts.py
│
├── utils/
│
└── assets/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CodeMentor-AI.git
cd CodeMentor-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🤖 Setup IBM Granite

Install Ollama:

https://ollama.com

Pull the Granite model:

```bash
ollama pull granite3.1-dense:2b
```

Start Ollama:

```bash
ollama serve
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

> Add screenshots here after deployment.

* Home Dashboard
* Test Generator
* Code Analyzer
* Problem Solver

---

## 🎯 Future Improvements

* File Upload Support
* PDF Report Export
* Multiple LLM Support
* Code Quality Score
* Syntax Highlighted Output
* Session History
* Additional Programming Languages

---

## 👨‍💻 Author

Developed by **Tanmay Kumar**

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.
