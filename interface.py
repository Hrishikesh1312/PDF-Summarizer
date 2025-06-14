from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QTextEdit, QFileDialog, QLabel, QLineEdit, QMessageBox
)

class PDFSummarizerUI(QWidget):
    def __init__(self, summarizer_func):
        super().__init__()
        self.setWindowTitle("PDF Summarizer - Ollama + Qt")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Load a PDF to summarize")
        self.layout.addWidget(self.label)

        self.text_area = QTextEdit()
        self.layout.addWidget(self.text_area)

        self.load_btn = QPushButton("Load PDF")
        self.load_btn.clicked.connect(self.load_pdf)
        self.layout.addWidget(self.load_btn)

        # Summary length input
        self.length_label = QLabel("Desired summary length (in sentences):")
        self.layout.addWidget(self.length_label)

        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("e.g., 5")
        self.layout.addWidget(self.length_input)

        self.summarize_btn = QPushButton("Summarize")
        self.summarize_btn.clicked.connect(self.summarize)
        self.layout.addWidget(self.summarize_btn)

        self.summarizer_func = summarizer_func
        self.pdf_text = ""

    def load_pdf(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open PDF", "", "PDF Files (*.pdf)")
        if path:
            from summarizer import extract_text_from_pdf
            self.pdf_text = extract_text_from_pdf(path)
            self.text_area.setPlainText(self.pdf_text)

    def summarize(self):
        if not self.pdf_text:
            QMessageBox.warning(self, "No PDF", "Please load a PDF first.")
            return

        length = self.length_input.text().strip()
        if not length.isdigit():
            QMessageBox.warning(self, "Invalid Length", "Please enter a valid number for summary length.")
            return

        length = int(length)
        summary = self.summarizer_func(self.pdf_text, summary_length=length)
        self.text_area.setPlainText(summary)
