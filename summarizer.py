import fitz
import requests

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def summarize_with_ollama(text, summary_length=5, model="llama3"):
    prompt = (
        f"Summarize the following text in approximately {summary_length} sentences:\n\n{text}"
    )
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt, "stream": False}
    )
    if response.ok:
        return response.json()["response"]
    return "Error: Could not summarize."

