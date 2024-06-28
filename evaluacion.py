#importo el archivo csv
import csv
#defino una funcion llamada menu para establecer la opcion
def menu():
    print('''
                <<< MENU >>>
          [1]- Agregar productos
          [2]- Leer el inevtario
          [3]- Clasificar y exportar productos
          [4]- Salir
          ======================================''')
    op = int(input("ingrese una opción:"))
    return op

#esta es la opcion 1 
def agregar_productos():
    #le pido al user que ingrese los datos del producto
    id_producto = input("ingrese el ID del producto:")
    nombre_producto = input("ingrese el nombre del producto:")
    categoria = input("ingrese categoria(electroica, textil o calzado):")
    precio_producto = input("ingrese el precio del producto:")
    #creo un archivo muevo llamado inventario.csv para almacenar los datos dados por el user
    #lo defino en modo de escritura para que se escriban los datos
    with open('inventario.csv', 'a', newline='') as inventarioproductos:
        escritorinventario = csv.writer(inventarioproductos)
        escritorinventario.writerow([id_producto,nombre_producto,categoria,precio_producto])
    #muestra in mensaje que se guaro con exito
    print("Se a guardado con exito!")

#esta es la opcion 2
def leerinventario():
    #abro el archivo ya creado anteriormente y lo defino en modo de lestura
    with open('inventario.csv', 'r', newline='') as inventarioproductos:
        leerarchivo_inventario = csv.reader(inventarioproductos)
        #lo muestro en pantalla 1 por uno
        for fila in leerarchivo_inventario:
            print(fila)
            
#esta es la opcion 3      
def clas_expor_productos():
    #creo listas para guardar los datos de cada categoria
    electronica =[]
    textil =[]
    calzado = []
    #abro el archivo en modo de lectura
    with open('inventario.csv', 'r', newline='') as inventarioproductos:
        leerarchivo = csv.reader(inventarioproductos)
        for fila in leerarchivo:
            id_producto, nombre_producto, categoria, precio_producto = fila
            if fila[2] == 'electronica':
                electronica.append([id_producto, nombre_producto,categoria, precio_producto])
            elif fila[2] == 'textil':
                textil.append([id_producto, nombre_producto, categoria, precio_producto])
            elif fila [2] == 'calzado':
                calzado.append([fila]) 
            else:
                print("---")
        print("categoria electronica:")
        print(electronica)    
        print("categoria textil:")
        print(textil)
        print("categoria calzado:")
        print(calzado)
        
        with open('clasificacion_productos.txt', 'w', newline='') as clasificaciones:
            clasificaciones.write('electronica')
            for elemento in electronica:
                clasificaciones.write(str(elemento))
                
            clasificaciones.write('textil')
            for elemento in textil:
                clasificaciones.write(str(elemento))
            
            clasificaciones.write('calzado')
            for elemento in calzado:
                clasificaciones.write(str(elemento))
            
            print("productos clasificados!")
                  
            
 
   
while True:
    op = menu()
    if op == 1:
        agregar_productos()
    elif op == 2:
        leerinventario()
    elif op == 3:
        clas_expor_productos()
    else:
        print("¡Adios!")
        break