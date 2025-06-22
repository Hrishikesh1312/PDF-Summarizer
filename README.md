# 🧠 PDF Summarizer — using Ollama + PyQt5

A simple, privacy-focused desktop app to summarize one or more PDF files using LLMs — all running locally on your machine.

This project uses:

- 🧠 [Ollama](https://ollama.com) for local large language model inference
- 🐍 PyQt5 for a modern desktop user interface
- 📄 Support for **single or batch PDF summarization**
- 🌙 Toggle between dark mode and light mode
- 📂 Export summaries as `.txt` files

---

## ⚙️ Requirements

> Ensure you have the following installed:

```bash
# Python dependencies
pip install PyQt5 fitz reportlab requests

# Ollama (for LLMs)
https://ollama.com/download

# Start the Ollama server
ollama serve
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/Hrishikesh1312/PDF-Summarizer
cd PDF-Summarizer

# Start Ollama in a separate terminal
ollama serve

# Run the app
python main.py
```

---

## 🛡️ Why Local?

This tool **never sends your PDF files or content to the cloud**.

✅ Your PDFs are read and summarized **entirely on your system**\
✅ Ollama runs the LLM **locally**, using models like `llama3`\
✅ No API keys or internet needed after setup

---

## ✨ Features

- ✅ Choose summary length (in number of sentences)
- ✅ Dark Mode / Light Mode toggle
- ✅ Export summaries as `.txt`
- ✅ Clean and responsive desktop UI
- ✅ 100% local — your documents never leave your device

---

## 👤 Screenshot

Light Theme             |  Dark Theme
:-------------------------:|:-------------------------:
![Screenshot 2025-06-22 135917](https://github.com/user-attachments/assets/e08b1047-f3de-4c6c-872c-7e2cf5b0a594)  |  ![Screenshot 2025-06-22 135932](https://github.com/user-attachments/assets/d45f0039-a317-47e7-a691-0645f58b0ccd)

---

## 📂 Folder Structure

```
pdf-summarizer/
├── main.py              # Entry point
├── interface.py           # PyQt5 GUI
├── summarizer.py        # PDF text extraction + Ollama integration
└── README.md
```

---

## 🧠 Customizing the Model

You can change the model used by editing `summarizer.py`:

```python
def summarize_with_ollama(text, summary_length=5, model="llama3"):
```

Try other local models like `mistral`, `gemma`, etc. (see: `ollama list`)

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- [Ollama](https://ollama.com) — for blazing fast local LLMs
- [PyMuPDF](https://pymupdf.readthedocs.io/) — for fast and accurate PDF parsing
- [PyQt5](https://doc.qt.io/qtforpython/) — for beautiful UIs in Python

---

