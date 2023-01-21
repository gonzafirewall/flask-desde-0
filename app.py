from flask import Flask, request, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return """
    <form method="POST">
    <input type="text" name="texto" value="" placeholder="Escribe aqui">
    <input type="submit">
    </form>
    """

@app.post("/")
def leer_request():
    print(request.form)
    return redirect("/") 