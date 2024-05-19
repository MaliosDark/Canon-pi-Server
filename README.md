
### Estructura del Proyecto


```
photo_server/
├── app.py
├── capture_images.py
├── static/
│   └── (aquí se guardarán las imágenes)
├── templates/
│   └── index.html
├── wifi_setup.sh
```


```markdown
# Raspberry Pi Photo Server

Este proyecto configura una Raspberry Pi como un punto de acceso WiFi que captura imágenes automáticamente desde una cámara Canon EOS 1000D y las muestra en una galería web. Puedes acceder, descargar y eliminar las imágenes a través de una interfaz web.

## Requisitos

- Raspberry Pi Zero W (o cualquier modelo compatible con WiFi)
- Tarjeta microSD (al menos 8GB)
- Cámara Canon EOS 1000D
- Cable USB para conectar la cámara a la Raspberry Pi
- Fuente de alimentación para la Raspberry Pi

## Instrucciones de Instalación

### Escribir la Imagen en la Tarjeta SD

1. Descarga la imagen del sistema desde el siguiente enlace: [raspberry_pi_image.img.gz](http://tu-enlace-de-descarga.com).
2. Descomprime el archivo descargado:

   ```bash
   gzip -d raspberry_pi_image.img.gz
   ```

3. Utiliza una herramienta como `Etcher`, `Raspberry Pi Imager`, o `dd` para escribir la imagen en la tarjeta SD.

   **Usando `dd` en Linux:**

   ```bash
   sudo dd if=raspberry_pi_image.img of=/dev/sdX bs=4M
   ```

   Asegúrate de reemplazar `/dev/sdX` con el identificador correcto de tu tarjeta SD.

### Configuración Inicial

1. Inserta la tarjeta SD en la Raspberry Pi.
2. Conecta la cámara Canon EOS 1000D a la Raspberry Pi usando el cable USB.
3. Conecta la fuente de alimentación a la Raspberry Pi y enciéndela.

### Conexión al Punto de Acceso WiFi

1. En tu dispositivo (laptop, smartphone, etc.), busca redes WiFi disponibles y conéctate a la red llamada `PhotoServer`.
2. La contraseña por defecto es `your_password`.

### Acceso a la Interfaz Web

1. Abre un navegador web y accede a la siguiente dirección:

   ```
   http://192.168.4.1:5000
   ```

2. Verás una galería con las imágenes capturadas. Desde esta interfaz, puedes:
   - Ver las imágenes.
   - Descargar imágenes individuales.
   - Eliminar imágenes.

## Estructura del Proyecto

- **capture_images.py:** Script que captura imágenes periódicamente desde la cámara.
- **app.py:** Servidor Flask que proporciona la interfaz web para la galería de imágenes.
- **static/:** Directorio donde se guardan las imágenes capturadas.
- **templates/index.html:** Plantilla HTML para la galería de imágenes.
- **wifi_setup.sh:** Script para configurar la Raspberry Pi como un punto de acceso WiFi.

## Personalización

### Cambiar la Contraseña del Punto de Acceso

1. Abre el archivo `/home/pi/photoserver/wifi_setup.py`:

   ```bash
   sudo nano /etc/hostapd/hostapd.conf
   ```

2. Cambia la línea `wpa_passphrase=your_password` a la nueva contraseña deseada.
3. Guarda y cierra el archivo, luego reinicia los servicios:

   ```bash
   sudo systemctl restart hostapd
   sudo systemctl restart dnsmasq
   ```

### Ajustar el Intervalo de Captura

1. Abre el archivo `capture_images.py`:

   ```bash
   nano /home/pi/photo_server/capture_images.py
   ```

2. Cambia el valor en `time.sleep(10)` al número de segundos deseado.
3. Guarda y cierra el archivo, luego reinicia el servicio:

   ```bash
   sudo systemctl restart capture_images.service
   ```

## Solución de Problemas

- **No se muestra la red WiFi:** Asegúrate de que los servicios `hostapd` y `dnsmasq` están funcionando:

  ```bash
  sudo systemctl status hostapd
  sudo systemctl status dnsmasq
  ```

- **No se capturan imágenes:** Verifica la conexión USB y el estado del servicio de captura de imágenes:

  ```bash
  sudo systemctl status capture_images.service
  ```

- **La interfaz web no carga:** Verifica el estado del servicio Flask:

  ```bash
  sudo systemctl status photo_server.service
  ```

## Contacto

Para cualquier pregunta o soporte, puedes contactarnos en [malios666@gmail.com](malios666@gmail.com).

¡Gracias por usar nuestro proyecto de servidor de fotos para Raspberry Pi y Camaras Canon!
```