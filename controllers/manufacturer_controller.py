from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
from models.SuperpowerProduct import SuperpowerProduct
from models.Manufacturer import Manufacturer


import repositories.superpower_product_repository as superpower_product_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint('manufacturers', __name__)

# manufacturers

# READ
# manufacturers inventory table shown - manufacturers index.jinja
# will use GET
@manufacturers_blueprint.route('/manufacturers') # manufacturers index.jinja
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/index.jinja', manufacturers = manufacturers)

# SHOW one specific manufacturer from manufacturers
# manufacturers - /manufacturers/<id>
@manufacturers_blueprint.route('/manufacturers/<id>', methods=['GET']) # manufacturers index.jinja
def manufacturers_show_by_id(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('manufacturers/show_one_specific_manufacturer.jinja', manufacturer = manufacturer)


# # NEW
# # GET '/manufacturer/new'
@manufacturers_blueprint.route('/manufacturers/new', methods=['GET'])
def new_superpower_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturer/add_manufacturer_product.jinja', manufacturers = manufacturers)


# # # CREATE 
# # # add a new manufacturer to the manufacturers' inventory - manufacturers/new
# # # will use GET
@manufacturers_blueprint.route('/manufacturers', methods=['GET'])
def create_manufacturer_product():
    name = request.form['manufacturer-product-name']
    description = request.form['manufacturer-description']
    email_address = request.form['manufacturer-email']
    location = request.form['manufacturer-location']
    manufacturer_id = request.form['manufacturer-id']
    manufacturer = manufacturer_repository.select(manufacturer_id)
    new_manufacturer = Manufacturer(name, description, email_address, location)
    manufacturer_repository.save(new_manufacturer)
    return redirect('/manufacturers')

# # UPDATE (edit)
# # edit a manufacturer within the manufacturers' inventory - manufacturers/<id>/edit
# will use POST
@manufacturers_blueprint.route('/manufacturers/<id>/edit', methods=['GET', 'POST'])
def edit_manufacturer_product(id):
    manufacturer = manufacturer_repository.select(id)
    superpower_products = manufacturer_repository.select_all()
    return render_template('manufacturers/edit_manufacturer.jinja', manufacturer = manufacturer, superpower_products = superpower_products)

@manufacturers_blueprint.route('/manufacturers/<id>', methods=['POST'])
def update_manufacturer(id):
    name = request.form['manufacturer-name']
    description = request.form['manufacturer-description']
    email_address = request.form['manufacturer-email-address']
    location = request.form['manufacturer-location']
    manufacturer_id = request.form['manufacturer-id']
    updated_manufacturer = Manufacturer(name, description, email_address, location, manufacturer_id)
    manufacturer_repository.update(updated_manufacturer)
    return redirect('/manufacturers')

# # DELETE
# # delete a manufacturer within the superpower_products inventory - superpower_products/<id>/delete
# # will use POST (used GET instead as it was simpler)
@manufacturers_blueprint.route('/manufacturers/<id>/delete', methods=['GET'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')





