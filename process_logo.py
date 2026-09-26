import base64
import requests
from PIL import Image
import numpy as np
import io

URL = "https://media.licdn.com/dms/image/v2/C4D0BAQGLgt6-3_a1NQ/company-logo_200_200/company-logo_200_200/0/1631021473995/dpsgurugram67a_logo?e=2147483647&v=beta&t=q87K_InIaBx6y8qzTndUVbEWlXpPpLibmue7UyWrCEo"

def process_logo():
    response = requests.get(URL)
    img_bytes = response.content
    img = Image.open(io.BytesIO(img_bytes)).convert("RGB")
    a = np.asarray(img).astype(np.float32)
    
    # Projection logic from prompt
    G = np.array([0., 93., 62.])
    W = np.array([255., 255., 255.])
    d = W - G
    t = np.clip(((a - G) @ d) / (d @ d), 0., 1.)
    out = W * (1 - t[..., None]) + G * t[..., None]
    
    out_img = Image.fromarray(out.astype(np.uint8))
    
    # Save to file
    out_img.save("logo_green_on_white.png")
    print("Logo saved as logo_green_on_white.png")

process_logo()
