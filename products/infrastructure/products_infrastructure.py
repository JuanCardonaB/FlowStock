from models.response_model import APIResponse
from products.model import product_model
from db.connection import Session
from db.models.FlowStockDB import products
from datetime import datetime

# This function returns all products.
def get_products():
    try:
        session = Session()
        products_list = session.query(products).all()
        session.close()

        if not products_list:
            return APIResponse(
                message="No products found",
                data=None,
                status="ok",
                status_code=200
            )

        return APIResponse(
            message="All products",
            data=[products.to_dict() for products in products_list],
            status="ok",
            status_code=200
        )

    except Exception as e:
        return APIResponse(
            message=f"An error occurred while fetching products {e}",
            data=None,
            status="error",
            status_code=500
        )

# This function creates a product.
def create_product(request: product_model.ProductRequest) -> APIResponse:
    try:

        images = []
        for image in request['images']:
            image = image.split('/')[-1]
            images.append(image)
        images = ','.join(images)

        session = Session()
        new_product = products(
            title=request['title'],
            description=request['description'],
            price=request['price'],
            stock=request["stock"],
            product_images=images,
            created_at=datetime.now()
        )
        session.add(new_product)
        session.commit()
        new_product = new_product.to_dict()
        session.close()

        return APIResponse(
            message='Product created succesfuly',
            data=new_product,
            status="ok",
            status_code=200
        )
    except Exception as e:
        return APIResponse(
            message=f"An error occurred while creating product {e}",
            data=None,
            status="error",
            status_code=500
        )

# This function get the product by id.
def get_product_by_id(id: int) -> APIResponse:
    try:
        session = Session()
        product = session.query(products).filter(products.id == id).first()
        session.close()

        if not product:
            return APIResponse(
                message="Product not found",
                data=None,
                status="ok",
                status_code=200
            )
        
        return APIResponse(
            message="Product found",
            data=product.to_dict(),
            status="ok",
            status_code=200
        )
    except Exception as e:
        return APIResponse(
            message=f"An error occurred while fetching product {e}",
            data=None,
            status="error",
            status_code=500
        )
    
# This function updates a product.
def update_product(request: product_model.ProductResponse) -> APIResponse:
    try:
        session = Session()

        product = session.query(products).filter_by(id=request['id']).first()

        if not product:
            return APIResponse(
                message="Product not found",
                data=None,
                status="error",
                status_code=404
            )
        
        product.title = request['title']
        product.description = request['description']
        product.price = request['price']
        product.stock = request['stock']
        product.created_at = request['created_at']
        product.product_images = ','.join(request['images']) if type(request['images']) == "<class 'list'>" else request['images']

        session.commit()
        product_data = product.to_dict()
        session.close()

        return APIResponse(
            message="Product found",
            data=product_data,
            status="ok",
            status_code=200
        )

    except Exception as e:
        return APIResponse(
            message=f"An error occurred while updating product {e}",
            data=None,
            status="error",
            status_code=500
        )
    
def delete_product(id: int) -> APIResponse:
    try:
        session = Session()
        product = session.query(products).filter_by(id=id).first()

        if not product:
            return APIResponse(
                message="Product not found",
                data=None,
                status="error",
                status_code=404
            )
        
        session.delete(product)
        session.commit()
        session.close()

        return APIResponse(
            message="Product deleted",
            data=None,
            status="ok",
            status_code=200
        )

    except Exception as e:
        return APIResponse(
            message=f"An error occurred while deleting product {e}",
            data=None,
            status="error",
            status_code=500
        )