from flask import Flask

app = Flask(__name__)

def make_underlined(name):
    name = f"<u>{name}</u>"
    return name

# def  make_emb

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p1 style="text-align: center">Just Testing</p1>' \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDEzcTB2OXBtcGN0d3dpNTU1aHdxNXZhamo3NDlobXI2bnQ0cGQ4MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/1YcLOSW6JCNdsfSr5E/giphy.gif"></iframe>' \
            '<img src="https://media.giphy.com/media/EZICHGrSD5QEFCxMiC/giphy.gif?cid=790b76112psfcwrqyxyyh4qupnp2sr05sqzbk2arsn8r85tg&ep=v1_gifs_trending&rid=giphy.gif&ct=g"></img>'

@app.route("/bye")
def bye(word):
    return word

@app.route("/username/<name>")
def greet(name):
    return f"Hi {name}!"

if __name__ == '__main__':
    app.run(debug=True)