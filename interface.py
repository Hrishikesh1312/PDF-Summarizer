from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog,
    QLabel, QLineEdit, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import time
import re  

class SummarizerThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, text, length, summarizer_func):
        super().__init__()
        self.text = text
        self.length = length
        self.summarizer_func = summarizer_func

    def run(self):
        summary = self.summarizer_func(self.text, self.length)
        self.finished.emit(summary)


class PDFSummarizerUI(QWidget):
    def __init__(self, summarizer_func):
        super().__init__()
        self.setWindowTitle("🧠 PDF Summarizer")
        self.setGeometry(100, 100, 900, 700)
        self.summarizer_func = summarizer_func
        self.pdf_text = ""
        self.is_dark_mode = False

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(self.layout)

        title = QLabel("📄 PDF Summarizer")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(title)

        self.label = QLabel("Step 1: Load a PDF file")
        self.layout.addWidget(self.label)

        self.load_btn = QPushButton("📂 Load PDF")
        self.load_btn.clicked.connect(self.load_pdf)
        self.layout.addWidget(self.load_btn)

        self.length_label = QLabel(
            "Step 2: Maximum desired sentences:")
        self.layout.addWidget(self.length_label)

        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("e.g., 5")
        self.layout.addWidget(self.length_input)

        self.summarize_btn = QPushButton("🧾 Summarize")
        self.summarize_btn.clicked.connect(self.summarize)
        self.layout.addWidget(self.summarize_btn)

        self.spinner_label = QLabel("")
        self.spinner_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.spinner_label)

        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText(
            "PDF text and summary will appear here...")
        self.text_area.setFont(QFont("Courier", 10))
        self.layout.addWidget(self.text_area)

        self.theme_btn = QPushButton("🌙 Switch to Dark Mode")
        self.theme_btn.clicked.connect(self.toggle_theme)
        self.layout.addWidget(self.theme_btn)

        self.export_btn = QPushButton("💾 Export Summary")
        self.export_btn.clicked.connect(self.export_summary)
        self.layout.addWidget(self.export_btn)

        self.apply_light_theme()

    def load_pdf(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Open PDF", "", "PDF Files (*.pdf)")
        if path:
            from summarizer import extract_text_from_pdf
            self.pdf_text = extract_text_from_pdf(path)
            self.text_area.setPlainText(self.pdf_text)

    def summarize(self):
        self.start_time = time.time()
        if not self.pdf_text:
            QMessageBox.warning(self, "No PDF", "Please load a PDF first.")
            return

        length = self.length_input.text().strip()
        if not length.isdigit():
            QMessageBox.warning(self, "Invalid Length",
                                "Please enter a valid number.")
            return

        self.spinner_label.setText("⏳ Summarizing... Please wait")
        self.summarize_btn.setEnabled(False)
        self.load_btn.setEnabled(False)

        self.thread = SummarizerThread(
            self.pdf_text, int(length), self.summarizer_func)
        self.thread.finished.connect(self.on_summary_finished)
        self.thread.start()

    def export_summary(self):
        summary = self.text_area.toPlainText().strip()

        if not summary:
            QMessageBox.warning(self, "Empty Summary",
                                "There is no summary to export.")
            return

        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Summary",
            "",
            "Text File (*.txt)",
            options=options
        )

        if file_path:
            if not file_path.endswith(".txt"):
                file_path += ".txt"

            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(summary)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")

    def on_summary_finished(self, summary):
        self.spinner_label.setText("")
        self.text_area.setPlainText(summary)
        self.summarize_btn.setEnabled(True)
        self.load_btn.setEnabled(True)
        elapsed_time = time.time() - self.start_time
        self.spinner_label.setText(f"✅ Done in {elapsed_time:.2f} seconds")
        self.show_stats(summary)

    def show_stats(self, summary):
        original_words = len(self.pdf_text.split())
        summary_words = len(summary.split())

        original_sentences = len(re.findall(r'[.!?]', self.pdf_text))
        summary_sentences = len(re.findall(r'[.!?]', summary))

        word_reduction = 100 * (1 - summary_words / original_words) if original_words else 0
        sentence_reduction = 100 * (1 - summary_sentences / original_sentences) if original_sentences else 0

        stats = (f"\n---\n"
                f"📊 Word Count: {original_words} ➝ {summary_words} "
                f"({word_reduction:.1f}% shorter)\n"
                f"📝 Sentence Count: {original_sentences} ➝ {summary_sentences} "
                f"({sentence_reduction:.1f}% shorter)\n")

        self.text_area.append(stats)


    def toggle_theme(self):
        self.is_dark_mode = not self.is_dark_mode
        if self.is_dark_mode:
            self.apply_dark_theme()
            self.theme_btn.setText("☀️ Switch to Light Mode")
        else:
            self.apply_light_theme()
            self.theme_btn.setText("🌙 Switch to Dark Mode")

    def apply_dark_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #202020;
                color: #E0E0E0;
                font-size: 14px;
            }
            QLineEdit, QTextEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: 1px solid #555;
                padding: 5px;
            }
            QPushButton {
                background-color: #444;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #555;
            }
        """)

    def apply_light_theme(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                color: #000000;
                font-size: 14px;
            }
            QLineEdit, QTextEdit {
                background-color: #F5F5F5;
                color: #000000;
                border: 1px solid #CCC;
                padding: 5px;
            }
            QPushButton {
                background-color: #E0E0E0;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #D5D5D5;
            }
        """)
