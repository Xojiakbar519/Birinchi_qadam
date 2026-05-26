import cv2
import numpy as np
import os

# Papka yo‘li
input_folder = r"C:\Users\HP\Desktop\oz"

# Qo‘llab-quvvatlanadigan formatlar
valid_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

for filename in os.listdir(input_folder):
    if filename.lower().endswith(valid_ext):
        input_path = os.path.join(input_folder, filename)

        # Rasmni o‘qish
        img = cv2.imread(input_path)

        if img is None:
            print(f"Xatolik: {filename} o‘qilmadi")
            continue

        # Gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Blur
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        # Adaptive threshold (universal)
        thresh = cv2.adaptiveThreshold(
            blur, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )

        # Oqartirishni kuchaytirish
        thresh[thresh > 240] = 255

        # Kichik shovqinni tozalash
        kernel = np.ones((2,2), np.uint8)
        clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # Saqlash nomi
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(input_folder, f"{name}_clean.png")

        cv2.imwrite(output_path, clean)

        print(f"Tayyor: {output_path}")

print("Barcha rasmlar qayta ishlandi.")
