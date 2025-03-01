import tkinter as tk
import random

class Breakout:
    def __init__(self, root):
        self.root = root
        self.root.title("Breakout Game")
        
        self.canvas = tk.Canvas(root, width=500, height=400, bg="black")
        self.canvas.pack()
        
        self.paddle = self.canvas.create_rectangle(200, 370, 300, 380, fill="white")
        self.ball = self.canvas.create_oval(240, 350, 260, 370, fill="red")
        
        self.ball_dx = random.choice([-3, 3])
        self.ball_dy = -3
        
        self.blocks = []
        self.create_blocks()
        
        self.canvas.bind_all("<Left>", self.move_left)
        self.canvas.bind_all("<Right>", self.move_right)
        
        self.run_game()
    
    def create_blocks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        for i in range(5):
            for j in range(7):
                block = self.canvas.create_rectangle(10 + j*70, 10 + i*30, 70 + j*70, 30 + i*30, fill=colors[i])
                self.blocks.append(block)
    
    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)
    
    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)
    
    def run_game(self):
        self.update_ball()
        self.root.after(20, self.run_game)
    
    def update_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        
        if ball_coords[0] <= 0 or ball_coords[2] >= 500:
            self.ball_dx = -self.ball_dx
        if ball_coords[1] <= 0:
            self.ball_dy = -self.ball_dy
        if ball_coords[3] >= 400:
            self.canvas.create_text(250, 200, text="Game Over", fill="white", font=("Arial", 20))
            return
        
        paddle_coords = self.canvas.coords(self.paddle)
        if (ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2] and
                ball_coords[3] >= paddle_coords[1] and ball_coords[1] <= paddle_coords[3]):
            self.ball_dy = -self.ball_dy
        
        for block in self.blocks:
            block_coords = self.canvas.coords(block)
            if (ball_coords[2] >= block_coords[0] and ball_coords[0] <= block_coords[2] and
                    ball_coords[3] >= block_coords[1] and ball_coords[1] <= block_coords[3]):
                self.canvas.delete(block)
                self.blocks.remove(block)
                self.ball_dy = -self.ball_dy
                break
        
        if not self.blocks:
            self.canvas.create_text(250, 200, text="You Win!", fill="white", font=("Arial", 20))
            return

root = tk.Tk()
Breakout(root)
root.mainloop()