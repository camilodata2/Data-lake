import psycopg2

def conectar_bd(host, puerto, nombre_bd, usuario, contraseña):
    try:
        conexion = psycopg2.connect(
            host=host,
            port=puerto,
            dbname=nombre_bd,
            user=usuario,
            password=contraseña
        )
        print("Conexión exitosa a la base de datos PostgreSQL")
        return conexion
    except (Exception, psycopg2.Error) as error:
        print("Error al conectar a la base de datos PostgreSQL:", error)

# Ejemplo de conexion
conexion = conectar_bd('localhost', '5432', 'postgres', 'postgres1', 'camilo43')