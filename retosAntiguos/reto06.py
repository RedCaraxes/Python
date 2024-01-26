"""
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
"""

import cv2
import requests
url="https://pixabay.com/es/images/download/feather-7854908_1280.jpg"
respuesta=requests.get(url)
imagen = cv2.imdecode(respuesta.content, cv2.IMREAD_COLOR)
alto, ancho = imagen.shape[:2]

print(f"La imagen tiene {ancho} píxeles de ancho y {alto} píxeles de alto.")