# Import libraries
from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk  # For displaying images in Tkinter
import cv2  # OpenCV (might be needed for color conversion)

model_file_path = "./runs/detect/train9/weights/best.pt"
# Load a model
model = YOLO(model_file_path)

# Global variable to hold the image
current_image_label = None


def run_yolo_inference(save: bool = False):
    global current_image_label

    # Open file dialog to select source image
    source = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if not source:
        return  # Do nothing if no file is selected

    try:
        # Run YOLO model inference
        results = model(source, stream=True, conf=0.5)

        for result in results:
            # Get the detected image (with annotations)
            img_array = result.plot()  # Generates annotated image as a numpy array

            # Handle color conversion (from BGR to RGB)
            if img_array.shape[-1] == 3:  # Check if the image has 3 color channels
                img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)

            # Convert the image to a PIL Image for displaying in Tkinter
            img = Image.fromarray(img_array)
            img = img.resize((400, 300))  # Resize to fit the UI window

            # Convert PIL image to ImageTk format
            img_tk = ImageTk.PhotoImage(image=img)

            # If there's already an image displayed, remove it
            if current_image_label is not None:
                current_image_label.destroy()

            # Add the updated image to the UI
            current_image_label = tk.Label(root, image=img_tk)
            current_image_label.image = img_tk
            current_image_label.pack(pady=10)

            # Optionally save the result if save=True
            if save:
                result.save(save_dir="./output/")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while running inference: {e}")


if __name__ == '__main__':
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("YOLO Inference UI")

    # Set up window dimensions
    root.geometry("600x500")  # Adjust size to fit the image display

    # Add an information label
    info_label = tk.Label(root, text="YOLO Inference Tool", font=("Helvetica", 16))
    info_label.pack(pady=10)

    # Add a button to run YOLO inference
    inference_button = tk.Button(root, text="Run Inference", command=run_yolo_inference, font=("Helvetica", 14))
    inference_button.pack(pady=20)

    # Run the Tkinter main loop
    root.mainloop()