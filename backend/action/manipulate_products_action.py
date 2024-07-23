#
# Lab FastAPI
#
# Date    : 2024-06-29
# Auther  : Hirotoshi FUJIBE
# History :
#

# Import Libraries
from backend.mapper import products_mapper as model
from backend.database import connect_database as connect
from backend.response.list_response import JsonListResponse


def read_products():
    product_list = connect.session.query(model.ProductList.name, model.ProductList.remark).all()
    json_list = [product._asdict() for product in product_list]    # noqa
    json_response = JsonListResponse()
    json_response.set_list(json_list)
    return json_response
