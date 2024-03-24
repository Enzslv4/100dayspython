from flask import Flask
import random

number = random.randint(0, 9)

app = Flask(__name__)

@app.route("/")
def game():
    return '<h1 style="text-align: center">Higher or low</h1>' \
            '<a style="font-weight: bold; text-align: center">Guess a number between 0 and 9</a>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" style="display: block; margin-left: auto; margin-right: auto"></iframe>' \


@app.route("/too-high")
def too_high():
    return '<h1 style="text-align: center">Too High, try again!!!</h1>' \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMTB0bmR3anNwZmhwNjE1ZWdtMjk5ZG5oYnoxZ2dkaW41NWYxdHhydiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/7SF5scGB2AFrgsXP63/giphy.gif" style="display: block; margin-left: auto; margin-right: auto"></iframe>'


@app.route("/too-low")
def too_low():
    return '<h1 style="text-align: center">Too Low, try again!!!</h1>' \
            '<img src="https://media.giphy.com/media/MuztdWJQ4PR7i/giphy.gif?cid=ecf05e47b5ph8v7iwdrvikvtnmqpkjbwho5sj9t4yb7lknya&ep=v1_gifs_search&rid=giphy.gif&ct=g" style="display: block; margin-left: auto; margin-right: auto"></iframe>'


@app.route("/right_guess")
def right_guess():
    return '<h1 style="text-align: center">You are right!!!</h1>' \
            '<img src="https://media.giphy.com/media/LZElUsjl1Bu6c/giphy.gif?cid=ecf05e47we3v160tvmp0zy8shhzr4q7kjq5yqyei0522ztaj&ep=v1_gifs_search&rid=giphy.gif&ct=g" style="display: block; margin-left: auto; margin-right: auto"></iframe>'


@app.route("/answer/<int:guessed_number>")
def greet(guessed_number):
    if guessed_number > number:
        return too_high()
    elif guessed_number < number:
        return too_low()
    else:
        return right_guess()


if __name__ == '__main__':
    app.run(debug=True)