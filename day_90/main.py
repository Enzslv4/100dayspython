import tkinter as tk
from threading import Timer

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
        
        self.text_area = tk.Text(root, font=("Arial", 14), wrap="word")
        self.text_area.pack(expand=True, fill="both")
        self.text_area.bind("<KeyPress>", self.reset_timer)
        
        self.timer = None
        self.reset_timer()
    
    def reset_timer(self, event=None):
        if self.timer:
            self.timer.cancel()
        self.timer = Timer(5, self.clear_text)
        self.timer.start()
    
    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", "You stopped! Text deleted.")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
