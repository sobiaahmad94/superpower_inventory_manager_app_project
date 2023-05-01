DROP TABLE IF EXISTS superpower_products;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    email_address VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE superpower_products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_price FLOAT,
    selling_price FLOAT,
    manufacturer_id INT NOT NULL REFERENCES manufacturers(id) ON DELETE CASCADE 
);

