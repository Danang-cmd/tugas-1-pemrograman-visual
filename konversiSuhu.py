# Nama: Danang Adiwijaya
# NIM: F1D02310044
# Kelas: D

import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton, QMessageBox, QFrame)
from PySide6.QtCore import Qt

class AplikasiKonversiSuhu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konversi Suhu")
        self.resize(350, 350)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(15)

        self.label_judul = QLabel("KONVERSI SUHU")
        self.label_judul.setAlignment(Qt.AlignCenter)
        self.label_judul.setObjectName("bannerJudul")
        layout.addWidget(self.label_judul)

        layout.addWidget(QLabel("Masukkan Suhu (Celsius):"))
        self.input_celsius = QLineEdit()
        layout.addWidget(self.input_celsius)

        layout_tombol = QHBoxLayout()
        
        self.btn_fahrenheit = QPushButton("Fahrenheit")
        self.btn_kelvin = QPushButton("Kelvin")
        self.btn_reamur = QPushButton("Reamur")
        
        layout_tombol.addWidget(self.btn_fahrenheit)
        layout_tombol.addWidget(self.btn_kelvin)
        layout_tombol.addWidget(self.btn_reamur)
        layout.addLayout(layout_tombol)

        self.frame_hasil = QFrame()
        self.frame_hasil.setObjectName("frameHasil")
        layout_hasil = QVBoxLayout()
        
        self.label_judul_hasil = QLabel("<b>Hasil Konversi:</b>")
        self.label_judul_hasil.setObjectName("judulHasil")
        self.label_teks_hasil = QLabel("")
        self.label_teks_hasil.setObjectName("teksHasil")
        
        layout_hasil.addWidget(self.label_judul_hasil)
        layout_hasil.addSpacing(10)
        layout_hasil.addWidget(self.label_teks_hasil)
        self.frame_hasil.setLayout(layout_hasil)
        
        self.frame_hasil.hide()
        layout.addWidget(self.frame_hasil)

        layout.addStretch()
        self.setLayout(layout)

        self.btn_fahrenheit.clicked.connect(lambda: self.hitung_konversi("Fahrenheit"))
        self.btn_kelvin.clicked.connect(lambda: self.hitung_konversi("Kelvin"))
        self.btn_reamur.clicked.connect(lambda: self.hitung_konversi("Reamur"))

        self.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                font-family: 'Segoe UI', Arial, sans-serif;
                font-size: 13px;
                color: #333;
            }
            QLabel#bannerJudul {
                background-color: #3498db;
                color: white;
                font-size: 16px;
                font-weight: bold;
                padding: 12px;
                border-radius: 5px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #7cb342;
                border-radius: 5px;
                background-color: #e8f5e9;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 10px;
                border-radius: 5px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QFrame#frameHasil {
                background-color: #d6eaf8;
                border-left: 5px solid #0b5345;
                border-radius: 4px;
                padding: 10px;
            }
            QLabel#judulHasil {
                color: #0b5345;
            }
            QLabel#teksHasil {
                color: #154360;
                font-size: 13px;
            }
        """)

    def ambil_nilai_celsius(self):
        teks_input = self.input_celsius.text().strip()
        
        if not teks_input:
            QMessageBox.warning(self, "Peringatan", "Harap masukkan suhu terlebih dahulu!")
            return None
            
        try:
            teks_input = teks_input.replace(',', '.')
            celsius = float(teks_input)
            return celsius
        except ValueError:
            QMessageBox.critical(self, "Error", "Input tidak valid! Pastikan Anda hanya memasukkan angka.")
            self.input_celsius.clear() 
            return None

    def hitung_konversi(self, satuan_tujuan):
        celsius = self.ambil_nilai_celsius()
        
        if celsius is None:
            return

        hasil = 0.0
        
        if satuan_tujuan == "Fahrenheit":
            hasil = (celsius * 9/5) + 32
        elif satuan_tujuan == "Kelvin":
            hasil = celsius + 273.15
        elif satuan_tujuan == "Reamur":
            hasil = celsius * 4/5

        teks_hasil = f"{celsius:g} Celsius = {hasil:.2f} {satuan_tujuan}"
        self.label_teks_hasil.setText(teks_hasil)
        
        self.frame_hasil.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AplikasiKonversiSuhu()
    window.show()
    sys.exit(app.exec())