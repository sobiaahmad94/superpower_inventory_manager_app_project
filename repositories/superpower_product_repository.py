from db.run_sql import run_sql

from models.Manufacturer import Manufacturer
from models.SuperpowerProduct import SuperpowerProduct
import repositories.manufacturer_repository as manufacturer_repository

def save(superpower_product):
    sql = "INSERT INTO superpower_products (name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s"
    values = [superpower_product.name, superpower_product.description, superpower_product.stock_quantity, superpower_product.selling_cost, superpower_product.manufacturer_id]
    results = run_sql(sql, values)
    id = results[0]['id']
    superpower_product.id = id
    return superpower_product

def select_all():
    superpower_products = []

    sql = "SELECT * FROM superpower_products"
    results = run_sql(sql)

    for row in results: 
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        superpower_product = SuperpowerProduct(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_cost'], manufacturer, row['id'])
        superpower_products.append(superpower_product)
    return superpower_products

def select(id):
    superpower_product = None
    sql = "SELECT * FROM superpower_products WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)


    if results:
        result = results[0]
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        superpower_product = SuperpowerProduct(result['name'], result['description'], result['stock_quantity'], result['buying_cost'], result['selling_cost'], manufacturer, result['id'])
    return superpower_product

def delete_all():
    sql = "DELETE FROM superpower_products"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM superpower_products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(superpower_product):
    sql = "UPDATE superpower_products SET (name, description, stock_quantity, buying_cost, selling_cost, manufacturer_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [superpower_product.name, superpower_product.description, superpower_product.stock_quantity, superpower_product.buying_cost, superpower_product.selling_cost, superpower_product.manufacturer.id, superpower_product.id]
    run_sql(sql, values)

def superpower_products_from_manufacturer(manufacturer):
    superpower_products = []

    sql = "SELECT * FROM superpower_products = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        superpower_product = SuperpowerProduct(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_cost'], row['manufacturer_id'], manufacturer, row['id'])
        superpower_products.append(superpower_product)
    return superpower_products

