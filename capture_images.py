import os
import time
import subprocess

def download_images():
    try:
        cmd = 'env LANG=C gphoto2 --debug --debug-logfile=my-logfile.txt --get-all-files --filename static/%Y%m%d-%H%M%S-%n.jpg'
        subprocess.run(cmd, shell=True, check=True)
        print("Imágenes descargadas.")
    except subprocess.CalledProcessError as e:
        print("Error al descargar las imágenes. Reintentando...")
        time.sleep(5)
        download_images()

if __name__ == "__main__":
    download_images()
