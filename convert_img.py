from PIL import Image
from PIL import ImageOps
import os
import shutil


def convert_img(input_path: str, output_path: str):
    # Open the image
    image = Image.open(input_path)

    # Get image dimensions
    width, height = image.size

    # Calculate cropping box (center crop to 640x640)
    left = (width - 640) // 2
    top = (height - 640) // 2
    right = left + 640
    bottom = top + 640

    # Crop the image
    image = image.crop((left, top, right, bottom))

    width, height = image.size

    # Padding img to above 640
    # Pad the image with white pixels to make dimensions at least 640
    if width < 640 or height < 640:
        new_width = max(640, width)
        new_height = max(640, height)
        image = ImageOps.expand(image, border=(
            (new_width - width) // 2,
            (new_height - height) // 2,
            (new_width - width + 1) // 2,
            (new_height - height + 1) // 2
        ), fill="white")
    else:
        image = image
    
    # Save the result
    image.save(output_path)



if __name__ == "__main__":
    img_dir = r"/mnt/c/Users/loitr/OneDrive/PARAmeter/Project/Machine Vision/imgs/my_fruit_img"
    save_path = r"/mnt/c/Users/loitr/OneDrive/PARAmeter/Project/Machine Vision/imgs/my_fruit_img_processed"
    # Ensure the directory exists
    if not os.path.exists(img_dir):
        print(f"Error: Directory {img_dir} does not exist.")

    file_names = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]
    if not file_names:
        print("No such files found in the directory.")

    # looping through directory to convert image to 640x640
    for idx, file_name in enumerate(file_names):
        convert_img(img_dir + "/" + file_name, save_path + f"/image_{idx + 1}.jpg")

        print(f"Converted {file_name} to 640x640, saved as {f'image_{idx + 1}.jpg'}")