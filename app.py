from fastapi import FastAPI, HTTPException
from products.router.products_router import router as products_router

app = FastAPI()

# add a route to the app
app.include_router(products_router, prefix="/products")