#importo pymysql
"""import pymysql
#creo la conexion
conexion = pymysql.connect(host='localhost', user='root', password='', db='tiendamvc')
try:
    with conexion.cursor() as cursor:
        #creo la consulta
        consulta = "SELECT * FROM customer"
        
        #ejecuto la consulta
        cursor.execute(consulta)
        #obtengo los resultados
        resultados = cursor.fetchall()
        #recorro los resultados
        for fila in resultados:
            print(fila)
            
except Exception as e:
    print("Ocurrió un error al consultar: ", e) 
finally:
    conexion.close()
    print("Conexion cerrada")   
try:
    with conexion.cursor() as cursor:
        #creo la consulta
        consulta = "insert into customer(name) values(%s)"
        datos = ("Alvaro Rodriguez")
        cursor.execute(consulta, datos)
        
        #confirma la transacción
        conexion.commit()
        
        print("Registro insertado correctamente")
        
        
        
            
except Exception as e:
    print("Ocurrió un error al consultar: ", e) 
finally:
    conexion.close()
    print("Conexion cerrada")   """