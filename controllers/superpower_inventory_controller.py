from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.SuperpowerProduct import SuperpowerProduct

import repositories.superpower_product_repository as superpower_product_repository
import repositories.manufacturer_repository as manufacturer_repository

superpower_products_blueprint = Blueprint('superpower_products', __name__)

# index
@superpower_products_blueprint.route('/superpower_products')
def superpower_products():
    superpower_products = superpower_product_repository.select_all()
    return render_template('superpower_products/index.jinja', all_superpower_products = superpower_products)
