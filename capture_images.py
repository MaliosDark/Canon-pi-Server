import os
import time

# Función para capturar una imagen con gphoto2
def capture_image():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"static/{timestamp}.jpg"
    os.system(f"gphoto2 --capture-image-and-download --filename {filename}")

if __name__ == "__main__":
    while True:
        capture_image()
        print("Imagen capturada.")
        time.sleep(10)  # Captura una imagen cada 10 segundos
