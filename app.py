from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message":"This is Home"}


@app.route("/api")
def api():
    return {"message":"This is API"}

@app.route("/products")
def products():
    product1 = {"id":1, "name":"Product 1", "price" : 12.99}
    product2 = {"id":2, "name":"Product 2", "price" : 14.99}
    product3 = {"id":3, "name":"Product 3", "price" : 24.99}
    return {"data":[product1, product2, product3]}


# if(__name__ == "__main__"):
#     app.run()