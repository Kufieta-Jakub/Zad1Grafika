# Zadanie 1

import urllib.request

import cv2
import matplotlib.pyplot as plt
import numpy as np

SOURCE = "https://thumb.wikimedia.org/wikipedia/commons/thumb/7/77/Horses_grazing_at_Trunkol_meadow%2C_Jammu_and_Kashmir%2C_India_%28crop%29.jpg/3840px-Horses_grazing_at_Trunkol_meadow%2C_Jammu_and_Kashmir%2C_India_%28crop%29.jpg?utm_source=commons.wikimedia.org&utm_campaign=imageinfo&utm_content=thumbnail"


def load_image(source):
    if source.startswith(("http://", "https://")):
        request = urllib.request.Request(source, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request) as response:
            data = np.asarray(bytearray(response.read()), dtype=np.uint8)
        img_bgr = cv2.imdecode(data, cv2.IMREAD_COLOR)
    else:
        img_bgr = cv2.imread(source, cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise ValueError("Nie udało się wczytać obrazu.")
    return cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)


image = load_image(SOURCE)

height, width = image.shape[:2]
resized = cv2.resize(image, (width // 2, height // 2), interpolation=cv2.INTER_AREA)
gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)
result = cv2.rotate(gray, cv2.ROTATE_90_CLOCKWISE)

print(result)
print(result.shape)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(image)
axes[0].set_title(f"Oryginał {image.shape[1]}x{image.shape[0]}")
axes[1].imshow(result, cmap="gray")
axes[1].set_title(f"Wynik {result.shape[1]}x{result.shape[0]}")
plt.tight_layout()
plt.show()
