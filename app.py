from fastapi import FastAPI, HTTPException
from products.router.products_router import router as products_router
from users_types.router.users_types_router import router as users_types_router

app = FastAPI()

# add a route to the app
app.include_router(products_router, prefix="/products")
app.include_router(users_types_router, prefix="/users_types")