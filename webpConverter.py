import os
from PIL import Image

def convert_images_to_webp(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            try:
                with Image.open(input_path) as img:
                    base_name = os.path.splitext(filename)[0]
                    output_path = os.path.join(output_folder, f"{base_name}.webp")
                    img.convert("RGB").save(output_path, "webp")
                    print(f"Skonwertowano: {filename} -> {base_name}.webp")
            except Exception as e:
                print(f"Błąd podczas przetwarzania pliku {filename}: {e}")

if __name__ == "__main__":
    input_folder = "ImgToConvert"
    output_folder = "webpReady"

    convert_images_to_webp(input_folder, output_folder)