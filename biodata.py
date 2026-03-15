# Nama: Danang Adiwijaya
# NIM: F1D02310044
# Kelas: D 

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QComboBox, QPushButton, 
                               QMessageBox, QFrame)
from PySide6.QtCore import Qt

class FormBiodata(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.resize(400, 450)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(12)

        layout.addWidget(QLabel("Nama Lengkap:"))
        self.input_nama = QLineEdit()
        layout.addWidget(self.input_nama)

        layout.addWidget(QLabel("NIM:"))
        self.input_nim = QLineEdit()
        self.input_nim.setPlaceholderText("Masukkan NIM")
        layout.addWidget(self.input_nim)

        layout.addWidget(QLabel("Kelas:"))
        self.input_kelas = QLineEdit()
        self.input_kelas.setPlaceholderText("Contoh: TI-2A")
        layout.addWidget(self.input_kelas)

        layout.addWidget(QLabel("Jenis Kelamin:"))
        self.combo_jk = QComboBox()
        self.combo_jk.addItems(["Pilih Jenis Kelamin...", "Laki-laki", "Perempuan"])
        layout.addWidget(self.combo_jk)

        layout_tombol = QHBoxLayout()
        self.btn_tampilkan = QPushButton("Tampilkan")
        self.btn_reset = QPushButton("Reset")
        
        self.btn_tampilkan.setObjectName("btnTampilkan")
        self.btn_reset.setObjectName("btnReset")
        
        layout_tombol.addWidget(self.btn_tampilkan)
        layout_tombol.addWidget(self.btn_reset)
        layout_tombol.addStretch()
        layout.addLayout(layout_tombol)

        self.frame_hasil = QFrame()
        self.frame_hasil.setObjectName("frameHasil")
        layout_hasil = QVBoxLayout()
        
        self.label_judul_hasil = QLabel("<b>DATA BIODATA</b>")
        self.label_judul_hasil.setObjectName("judulHasil")
        self.label_teks_hasil = QLabel("")
        self.label_teks_hasil.setObjectName("teksHasil")
        
        layout_hasil.addWidget(self.label_judul_hasil)
        layout_hasil.addWidget(self.label_teks_hasil)
        self.frame_hasil.setLayout(layout_hasil)
        
        self.frame_hasil.hide() 
        layout.addWidget(self.frame_hasil)

        layout.addStretch()
        self.setLayout(layout)

        self.btn_tampilkan.clicked.connect(self.tampilkan_data)
        self.btn_reset.clicked.connect(self.reset_data)

        self.setStyleSheet("""
            QWidget {
                background-color: #f5f6f7;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 13px;
                color: #333;
            }
            QLineEdit, QComboBox {
                padding: 8px;
                border: 1px solid #7cb342;
                border-radius: 5px;
                background-color: #e8f5e9;
            }
            QComboBox {
                background-color: #ffffff;
                border: 1px solid #ccc;
            }
            QPushButton {
                padding: 8px 16px;
                border-radius: 5px;
                color: white;
                font-weight: bold;
                border: none;
            }
            QPushButton#btnTampilkan {
                background-color: #3498db;
            }
            QPushButton#btnTampilkan:hover {
                background-color: #2980b9;
            }
            QPushButton#btnReset {
                background-color: #95a5a6;
            }
            QPushButton#btnReset:hover {
                background-color: #7f8c8d;
            }
            QFrame#frameHasil {
                background-color: #dceedd;
                border-left: 5px solid #2e7d32;
                border-radius: 4px;
                padding: 10px;
                margin-top: 10px;
            }
            QLabel#judulHasil {
                color: #004d40;
                font-size: 14px;
                margin-bottom: 5px;
            }
            QLabel#teksHasil {
                color: #1b5e20;
                line-height: 1.5;
            }
        """)

    def tampilkan_data(self):
        nama = self.input_nama.text().strip()
        nim = self.input_nim.text().strip()
        kelas = self.input_kelas.text().strip()
        jk = self.combo_jk.currentText()

        if not nama or not nim or not kelas or self.combo_jk.currentIndex() == 0:
            QMessageBox.warning(self, "Peringatan", "Semua field harus diisi dengan lengkap!")
            return

        hasil = f"Nama: {nama}\nNIM: {nim}\nKelas: {kelas}\nJenis Kelamin: {jk}"
        self.label_teks_hasil.setText(hasil)
        
        self.frame_hasil.show()

    def reset_data(self):
        self.input_nama.clear()
        self.input_nim.clear()
        self.input_kelas.clear()
        self.combo_jk.setCurrentIndex(0)
        
        self.frame_hasil.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormBiodata()
    window.show()
    sys.exit(app.exec())