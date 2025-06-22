# 🧠 PDF Summarizer (Local & Private) — using Ollama + PyQt5

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

# Run your model of choice (e.g. LLaMA 3)
ollama run llama3
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/pdf-summarizer
cd pdf-summarizer

# Start Ollama model in a separate terminal
ollama run llama3

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

- ✅ Load and summarize **one or many** PDF files at once
- ✅ Choose summary length (in number of sentences)
- ✅ Dark Mode / Light Mode toggle
- ✅ Export summaries as `.txt`
- ✅ Clean and responsive desktop UI
- ✅ 100% local — your documents never leave your device

---

## 👤 Screenshot

> *Add a screenshot of the app here for visual clarity*

---

## 📂 Folder Structure

```
pdf-summarizer/
├── main.py              # Entry point
├── ui_main.py           # PyQt5 GUI
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

