import cv2
import numpy as np

# Fungsi untuk mendeteksi warna dan bentuk pisang
def detect_banana(image_path):
    # Membaca gambar
    image = cv2.imread(image_path)
    
    # Mengkonversi gambar ke ruang warna HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Rentang warna kuning dalam ruang warna HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # Membuat mask yang akan menunjukkan di mana warna kuning ada pada gambar
    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    # Menerapkan mask pada gambar asli
    result = cv2.bitwise_and(image, image, mask=mask)

    # Mengonversi gambar hasil deteksi ke citra abu-abu
    gray_result = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)

    # Menggunakan deteksi kontur untuk menemukan bentuk pisang
    contours, _ = cv2.findContours(gray_result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Menggambar kontur pada gambar asli
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # Menampilkan gambar asli, hasil deteksi warna, dan bentuk pisang
    cv2.imshow('Original Image', image)
    cv2.imshow('Banana Color Detected', result)
    
    # Menunggu tombol apapun ditekan untuk keluar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Jalankan fungsi dengan path ke gambar pisang Anda
detect_banana('pisang3.jpeg')
