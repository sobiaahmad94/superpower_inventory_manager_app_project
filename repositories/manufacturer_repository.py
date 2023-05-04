from db.run_sql import run_sql


from models.Manufacturer import Manufacturer

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, description, email_address, location) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.description, manufacturer.email_address, manufacturer.location]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['description'], row['email_address'], row['location'], row['id'])
        manufacturers.append(manufacturer)

        print(manufacturers) # Add this line to print out the list of manufacturers

    return manufacturers

select_all()

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        manufacturer = Manufacturer(result['name'], result['description'], result['email_address'], result['location'], result['id'])
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, description, email_address, location) = (%s, %s, %s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.description, manufacturer.email_address, manufacturer.location, manufacturer.id]
    run_sql(sql, values)
    