from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List, Optional

app = FastAPI()

# Sample product data
products = [
    {"id": 1, "name": "Product 1", "price": 10},
    {"id": 2, "name": "Product 2", "price": 20},
    {"id": 3, "name": "Product 3", "price": 30}
]

cart = []

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.post("/add_to_cart/", response_class=HTMLResponse)
async def add_to_cart(request: Request, product_id: int = Form(...)):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart.append(product)
    return templates.TemplateResponse("index.html", {"request": request, "products": products})

@app.get("/cart", response_class=HTMLResponse)
async def view_cart(request: Request):
    total = sum(item['price'] for item in cart)
    return templates.TemplateResponse("cart.html", {"request": request, "cart": cart, "total": total})
