from fastapi import APIRouter, Form, UploadFile, File
from fastapi.responses import JSONResponse
from models.response_model import APIResponse
from products.infrastructure  import products_infrastructure
from products.model import product_model
from db.models.FlowStockDB import products
from typing import List, Optional
import time
import os

# This is the router for the products.
router = APIRouter()

# This route returns all products.
@router.get("", response_model=APIResponse)
def all_products():
    return products_infrastructure.get_products()

# This route creates a product.
@router.post("/create_product", response_model=APIResponse)
def create_product(
    # Here we use Form and File to receive the data from the request.
    title: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...),
    images: List[UploadFile] = File(...)
    ):

    # We create a directory to store the images.
    os.makedirs("images", exist_ok=True)

    # We create a list to store the paths of the images.s
    images_paths = []
    count = 0
    # This loop saves the images in the images directory.
    # and appends the path to the images_paths list.
    for image in images:
        timestamp = int(time.time()) + count
        image_path = f"images/product_image_{timestamp}.{image.filename.split('.')[-1]}"
        with open(image_path, "wb") as buffer:
            buffer.write(image.file.read())
        images_paths.append(image_path)
        count += 13

    # We create a dictionary with the product data.
    product_data = {
        "title": title,
        "description": description,
        "price": price,
        "stock": stock,
        "images": images_paths
    }

    return products_infrastructure.create_product(product_data)

# This route returns a product by id.
@router.post("/get_product", response_model=APIResponse)
def get_product(product_id: int = Form(...)):
    return products_infrastructure.get_product_by_id(product_id)

# This route updates a product.
@router.put("/update_product", response_model=APIResponse)
async def edit_product(
    product_id: int = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    stock: int = Form(...),
    created_at: str = Form(...),
    old_images: Optional[str] = Form(None),
    new_images: List[UploadFile] = File(None)
    ):

    old_images_list = old_images.split(",") if old_images else []

    if new_images:
        uploaded_images = []
        for i, image in enumerate(new_images):
            file_extension = image.filename.split('.')[-1]
            renamed_file = f"product_image_{int(time.time())}.{file_extension}"
            image_path = os.path.join('images', renamed_file)

            # Guardar la imagen
            with open(image_path, "wb") as buffer:
                buffer.write(await image.read())
            uploaded_images.append(renamed_file)
        
        combined_images = old_images_list + uploaded_images
    else:
        combined_images = old_images_list
    
    if len(combined_images) > 5:
        combined_images = combined_images[:5]

    product_image = ','.join(combined_images)

    product_data = {
        "id": product_id,
        "title": title,
        "description": description,
        "price": price,
        "stock": stock,
        "created_at": created_at,
        "images": product_image
    }

    return products_infrastructure.update_product(product_data)

# This route deletes a product.
@router.post("/delete_product", response_model=APIResponse)
def delete_product(product_id: int = Form(...)):
    return products_infrastructure.delete_product(product_id)