import tkinter as tk
import time
import random

sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast requires practice and patience.",
    "Python is a great programming language for beginners.",
    "Speed typing tests can help improve accuracy and efficiency."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.sample_text = random.choice(sample_texts)
        self.start_time = None
        
        self.label = tk.Label(root, text=self.sample_text, wraplength=400, font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        
        self.button = tk.Button(root, text="Check Speed", command=self.calculate_speed)
        self.button.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)
    
    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time.time()
    
    def calculate_speed(self):
        if self.start_time is None:
            return
        
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        typed_text = self.entry.get()
        typed_words = len(typed_text.split())
        wpm = round((typed_words / elapsed_time) * 60)
        
        self.result_label.config(text=f"Your typing speed: {wpm} WPM")
        self.start_time = None
        
root = tk.Tk()
app = TypingSpeedTest(root)
root.mainloop()
