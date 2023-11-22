import imageio
from PIL import Image, ImageDraw


def create_gif(image_list, gif_path, duration=0.5):
    frames = []

    for image_path in image_list:
        # Resmi Pillow ile aç ve frames listesine ekle
        img = Image.open(image_path)
        frames.append(img)

    # GIF oluşturmak için imageio kullanarak frames listesini kullan
    imageio.mimsave(gif_path, frames, duration=duration)


# Örnek olarak oluşturulan resimlerin listesi
image_list = [
    "1.jpg",
    "3.jpg",
    "2.jpg",
]  # Buradaki dosya yollarını kendi dosya yollarınıza göre güncelleyin

# GIF'in oluşturulacağı dosya yolu
gif_path = "created_gif.gif"

# GIF oluşturma fonksiyonunu çağırma
create_gif(image_list, gif_path, duration=0.5)
