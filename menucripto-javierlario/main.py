
import hashlib
#creo la funcion que muestra el menu y guarda el numero que le pasamos en una variable
def menu():
        while True:
            try:
                respuesta=input("FUNCIONES HASH \n 1-Resumen MD5 de una cadena \n 2-Resumen SHA1 de una cadena \n 3- Resumen MD5 de un fichero \n 4-Resumen SHA1 de un fichero \n 5-SALIR")
                #Ponemos un try except dentro del bucle while para que se ejecute el programa y que salte el mensaje de except si ocurre algun fallo
                #despues leo la variable de la respuesta y ejecuto el codigo de hashlib para crear el resumen de la cadena que le pasamos
                if respuesta == "1":
                    cadena = input("Introduce la cadena de la que quieres obtener el MD5:")
                    print(hashlib.md5(cadena.encode('utf-8')).hexdigest())
                    continue
                elif respuesta == "2":
                    cadena2 = input("Introduce la cadena de la que quieres obtener el SHA1:")
                    print(hashlib.sha1(cadena2.encode('utf-8')).hexdigest())
                    continue
                elif respuesta == "3":
                    cadena3 = input("Introduce el fichero del que quieres obtener el MD5:")
                    with open(cadena3, 'rb') as f:
                        print(hashlib.md5(f.read()).hexdigest())
                        continue
                elif respuesta == "4":
                    cadena4 = input("Introduce el fichero del que quieres obtener el SHA1:")
                    with open(cadena4, 'rb') as f:
                        print(hashlib.sha1(f.read()).hexdigest())
                        continue
                elif respuesta == "5":
                    break
            except:
                print("Ha habido un fallo en el programa")

#después llamo a la funcion menú que ejecuta el menú, leee el número que le pasamos y ejecuta la orden que le decimos con la cadena de carácteres que le pasamos
menu()



