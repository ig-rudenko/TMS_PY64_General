from flask import Flask, render_template, request, redirect, url_for

from services import get_all_products, create_product

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static_url",
)


@app.get("/")
def hello_world():
    return render_template("home.html")


@app.get("/home")
def home():
    return render_template("home.html")


@app.get("/products")
def get_all_products_view():
    return render_template("products.html", products=get_all_products())


@app.get("/products/create")
def get_create_products_form_view():
    return render_template("create-products.html")


@app.post("/products/create")
def create_products_view():
    name = request.form.get("product-name")
    count = request.form.get("count")
    price = request.form.get("price")
    errors = {}

    if not name:
        errors["product-name"] = "Product name is required"
    elif len(name) > 64:
        errors["product-name"] = "Product name is too long. Max 64 characters"

    if not count:
        errors["count"] = "Count is required"
    elif not count.isdigit():
        errors["count"] = "Count must be a number"
    elif int(count) < 0:
        errors["count"] = "Count must be a positive number"

    if not price:
        errors["price"] = "Price is required"
    elif not price.isdigit():
        errors["price"] = "Price must be a number"
    elif int(price) < 0:
        errors["price"] = "Count must be a positive number"

    if errors:
        return render_template(
            "create-products.html",
            errors=errors,
            product_name=name,
            count=count,
            price=price,
        )

    product = create_product(name, int(count), int(price))
    # return render_template("create-products-success.html", product=product)

    return redirect(url_for("get_all_products_view"))
