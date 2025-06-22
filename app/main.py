from PyQt5.QtWidgets import QApplication
from interface import PDFSummarizerUI
from summarizer import summarize_with_ollama
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFSummarizerUI(summarizer_func=summarize_with_ollama)
    window.show()
    sys.exit(app.exec_())
