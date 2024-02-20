import sys
import os
from pathlib import Path
from PIL import Image, ImageTk
from rembg import remove
import tkinter as tk
from tkinter import filedialog

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing App")

        # Create and set up widgets
        self.label = tk.Label(root, text="Select an image:")
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="Browse", command=self.browse_image)
        self.button.pack(pady=10)

        self.process_button = tk.Button(root, text="Process Image", command=self.process_image)
        self.process_button.pack(pady=10)

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        self.label.config(text=f"Selected image: {file_path}")
        self.image_path = file_path

    def process_image(self):
        if not hasattr(self, 'image_path'):
            tk.messagebox.showerror("Error", "Please select an image first.")
            return

        # Load the input image
        image = Image.open(self.image_path)

        # Specify output directory
        output_dir = Path("output_images")
        output_dir.mkdir(exist_ok=True)

        # Resize and save images with different sizes
        
        # Remove the background
        image_rem = remove(image)

        # Save the image with the background removed
        image_rem.save(output_dir / "background_removed.png")

        sizes = [16, 32, 48, 180, 192, 512]
        for size in sizes:
            resized_image = image_rem.resize((size, size))
            resized_image.save(output_dir / f"{size}.png")

        tk.messagebox.showinfo("Success", "Image processing completed!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()