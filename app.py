from flask import Flask, request, redirect, render_template

app = Flask(__name__)

title = "Mi aplicación flask"

frutas_a_comprar = ["banana", "manzana", "naranja"]

@app.get("/")
def index():
    return render_template("index.html", title=title, frutas_a_comprar=frutas_a_comprar)
    
@app.post("/")
def leer_request():
    print(request.form)
    return redirect("/") 