from flask import Flask, render_template, request, redirect, session
from models import init_db, add_user, validate_user, add_product, get_products
import prometheus_client

app = Flask(__name__)
app.secret_key = "secret123"

# Prometheus metric
REQUEST_COUNT = prometheus_client.Counter('request_count', 'App Request Count')

@app.route("/")
def index():
    REQUEST_COUNT.inc()
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        add_user(request.form["username"], request.form["password"])
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if validate_user(request.form["username"], request.form["password"]):
            session["user"] = request.form["username"]
            return redirect("/products")
    return render_template("login.html")

@app.route("/products")
def products():
    if "user" not in session:
        return redirect("/login")
    return render_template("products.html", products=get_products())

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        add_product(request.form["name"], request.form["price"])
    return render_template("admin.html")

@app.route("/metrics")
def metrics():
    return prometheus_client.generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
