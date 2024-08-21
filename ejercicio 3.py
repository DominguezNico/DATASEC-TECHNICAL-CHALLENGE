import mysql.connector

# configuro la conexión a la base de datos
config = {
    'user': '***',  # el usr y el password podrian guardarse
    'password': '***',  # en una variable de entorno .env
    'host': 'localhost',
    'database': 'example_db',
}

# conecto a la base de datos
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# realizo la consulta SQL para obtener los clientes con más de 3 eventos fallidos
query = """
      SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer,
        COUNT(e.status) AS failures
      FROM customers c
        JOIN campaigns ca ON c.id = ca.customer_id
        JOIN events e ON ca.id = e.campaign_id
      WHERE e.status = 'failure'
      GROUP BY c.id
      HAVING failures > 3;
"""

# ejecuto la consulta
cursor.execute(query)

# obtengo y muestro los resultados
results = cursor.fetchall()
for row in results:
    print(f"customer: {row[0]}, failures: {row[1]}")

# cierro la conexión
cursor.close()
conn.close()
