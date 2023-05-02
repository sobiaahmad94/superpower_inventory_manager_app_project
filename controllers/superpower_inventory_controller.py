from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.SuperpowerProduct import SuperpowerProduct

import repositories.superpower_product_repository as superpower_product_repository
import repositories.manufacturer_repository as manufacturer_repository

superpower_products_blueprint = Blueprint('superpower_products', __name__)

# READ
# superpower_products inventory table shown - superpower_products index.jinja
# will use GET
@superpower_products_blueprint.route('/superpower_products') # superpower_products index.jinja
def superpower_products():
    superpower_products = superpower_product_repository.select_all()
    return render_template('superpower_products/index.jinja', superpower_products = superpower_products)

# NEW
# add a new superpower_product to the superpower_products inventory - superpower_products/new
# will use GET
@superpower_products_blueprint.route('/superpower_products/new')
def new_superpower_product():
    superpower_products = superpower_product_repository.select_all()
    return render_template('superpower_products/add_superpower_product.jinja', superpower_products = superpower_products)

# UPDATE (edit)
# edit a superpower_product within the superpower_products inventory - superpower_products/<id>/edit
# will use POST


# DELETE
# delete a superpower_product within the superpower_products inventory - superpower_products/<id>/delete
# will use POST


