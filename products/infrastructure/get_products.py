from models.response_model import APIResponse

def get_products():
    return APIResponse(
        message="All products",
        data=[
            {"name": "apple", "price": 1.0},
            {"name": "banana", "price": 0.5},
            {"name": "cherry", "price": 2.0},
        ],
        status="ok"
    )