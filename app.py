from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from products.router.products_router import router as products_router
from users_types.router.users_types_router import router as users_types_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# add a route to the app
app.include_router(products_router, prefix="/products")
app.include_router(users_types_router, prefix="/users_types")
# add a route to the app to serve static files, in this case images
app.mount("/images", StaticFiles(directory="images"), name="images")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)