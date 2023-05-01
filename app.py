from flask import Flask, render_template, request, url_for

from controllers.superpower_inventory_controller import superpower_products_blueprint

app = Flask(__name__)

app.register_blueprint(superpower_products_blueprint)

@app.route('/')
def home():
    return render_template('index.jinja')

if __name__ == '__main__':
    app.run(debug=True)