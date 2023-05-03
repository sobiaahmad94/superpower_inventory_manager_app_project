from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.SuperpowerProduct import SuperpowerProduct

import repositories.superpower_product_repository as superpower_product_repository
import repositories.manufacturer_repository as manufacturer_repository

superpower_products_blueprint = Blueprint('superpower_products', __name__)


# superpower products

# READ
# superpower_products inventory table shown - superpower_products index.jinja
# will use GET
@superpower_products_blueprint.route('/superpower_products') # superpower_products index.jinja
def superpower_products():
    superpower_products = superpower_product_repository.select_all()
    return render_template('superpower_products/index.jinja', superpower_products = superpower_products)

# SHOW one specific superpower_product from superpower_products
# superpower_products - /superpower_products/<id>
@superpower_products_blueprint.route('/superpower_products/<id>', methods=['GET']) # superpower_products index.jinja
def superpower_product_show_by_id(id):
    superpower_product = superpower_product_repository.select(id)
    return render_template('superpower_products/show_one_specific_superpower_product.jinja', superpower_product = superpower_product)

# NEW
# GET '/superpower_products/new'
@superpower_products_blueprint.route('/superpower_products/new', methods=['GET'])
def new_superpower_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template('superpower_products/add_superpower_product.jinja', manufacturers = manufacturers)


# # CREATE 
# # add a new superpower_product to the superpower_products inventory - superpower_products/new
# # will use GET
@superpower_products_blueprint.route('/superpower_products', methods=['POST'])
def create_superpower_product():
    name = request.form['superpower-product-name']
    description = request.form['superpower-product-description']
    stock_quantity = request.form['superpower-product-stock-quantity']
    buying_price = request.form['superpower-product-buying-price']
    selling_price = request.form['superpower-product-selling-price']
    manufacturer_id = request.form['manufacturer-id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    new_product = SuperpowerProduct(name, description, stock_quantity, buying_price, selling_price, manufacturer)
    superpower_product_repository.save(new_product)
    return redirect('/superpower_products')

# UPDATE (edit)
# edit a superpower_product within the superpower_products inventory - superpower_products/<id>/edit
# will use POST
@superpower_products_blueprint.route('/superpower_products/<id>/edit', methods=['GET'])
def edit_superpower_product(id):
    superpower_product = superpower_product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('superpower_products/edit_superpower_product.jinja', superpower_product = superpower_product, manufacturers = manufacturers)

@superpower_products_blueprint.route('/superpower_products/<id>', methods=['POST'])
def update_superpower_product(id):
    name = request.form['superpower-product-name']
    description = request.form['superpower-product-description']
    stock_quantity = request.form['superpower-product-stock-quantity']
    buying_price = request.form['superpower-product-buying-price']
    selling_price = request.form['superpower-product-selling-price']
    manufacturer_id = request.form['manufacturer-id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    updated_product = SuperpowerProduct(name, description, stock_quantity, buying_price, selling_price, manufacturer)
    superpower_product_repository.update(updated_product)
    return redirect('/superpower_products')

# DELETE
# delete a superpower_product within the superpower_products inventory - superpower_products/<id>/delete
# will use POST

# smaproducts

