# WaterMark Program

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

def upload_image():
    global img, img_tk, img_path
    img_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if img_path:
        img = Image.open(img_path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        canvas.create_image(200, 200, image=img_tk)

def add_watermark():
    if not img_path:
        messagebox.showerror("Erro", "Por favor, carregue uma imagem primeiro.")
        return
    
    watermark_text = watermark_entry.get()
    if not watermark_text:
        messagebox.showerror("Erro", "Por favor, insira um texto para a marca d'água.")
        return
    
    img_with_watermark = Image.open(img_path)
    draw = ImageDraw.Draw(img_with_watermark)
    font = ImageFont.load_default()
    text_position = (10, 10)
    text_color = (255, 255, 255)
    
    draw.text(text_position, watermark_text, fill=text_color, font=font)
    img_with_watermark.show()
    img_with_watermark.save("watermarked_image.png")
    messagebox.showinfo("Sucesso", "Imagem salva como 'watermarked_image.png'")

root = tk.Tk()
root.title("Watermark App")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

btn_upload = tk.Button(root, text="Upload Image", command=upload_image)
btn_upload.pack()

watermark_entry = tk.Entry(root)
watermark_entry.pack()

btn_watermark = tk.Button(root, text="Add Watermark", command=add_watermark)
btn_watermark.pack()

root.mainloop()
