DROP TABLE IF EXISTS manufacturers;
DROP TABLE IF EXISTS superpower_products;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    email_address VARCHAR(255),
    location VARCHAR(255)
)

CREATE TABLE superpower_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_cost FLOAT,
    selling_cost FLOAT,
    manufacturer_id INT NOT NULL REFERENCES ON DELETE CASCADE manufacturers(id)
)

