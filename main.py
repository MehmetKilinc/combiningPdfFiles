import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton
from PyPDF2 import PdfFileMerger

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Birleştirme")
        self.setGeometry(100, 100, 400, 300)

        self.merge_button = QPushButton("Birleştir", self)
        self.merge_button.setGeometry(150, 150, 100, 30)
        self.merge_button.clicked.connect(self.merge_pdfs)

    def merge_pdfs(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("PDF Dosyaları (*.pdf)")
        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            merger = PdfFileMerger()
            for file_path in file_paths:
                merger.append(file_path)
            output_path, _ = QFileDialog.getSaveFileName(self, "Birleştirilmiş PDF Kaydet", "", "PDF Dosyası (*.pdf)")
            if output_path:
                merger.write(output_path)
                merger.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
