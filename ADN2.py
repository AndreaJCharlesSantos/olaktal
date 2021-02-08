import csv
import operator
class Persona(object):
    def __init__(self, elementos):
     print("Se creó el objeto")
     self.elementos = elementos

    def __str__(self):
     return "Persona: {}".format(self.elementos)
     '''
    def archivocsv(cadena1, existecsv):
     
     with open(cadena1) as j:
      cadena1 = csv.DictReader(j) #Aquí está agregando todos los datos existentes en el csv
     existecsv = True # Servirá para validar más adelante la existencia 
     return cadena1, existecsv
     '''

    def BUSCAR(lineacsv, lineatxt):
     with open(lineatxt) as j:
      cadenatxt = j.read()  
      cadena = cadenaDNA(cadenatxt) #Crea el objeto de la secuencia  	
     archivocsv = open(lineacsv)
     cadenacsv = csv.DictReader(archivocsv)
     contador = {}
     for limitaciones in cadenacsv.fieldnames[1:]: #Aquí permite empezar a buscar desde la posición 1 que es donde existen las secuencias
      contador[limitaciones] = Persona.Concidencia(cadenatxt, limitaciones)

     for columna in cadenacsv:
      if all(contador[limitaciones] == int(columna[limitaciones]) for limitaciones in contador):
       respuesta =Persona(columna["name"])
       print("Las coincidencias son: ")
       print(respuesta)
       print(cadena)
       archivocsv.close()
       return
     else:
      print("No se encontraron coincidencias ")
     archivocsv.close()

    def Concidencia(cadenatxt, limitaciones):
     print(cadenatxt)
     cont = 0

     limite = 0
     tam = len(limitaciones)
     #print(tam)
     #print(limitaciones)
     for i in range(len(cadenatxt)):
       limite = cadenatxt.count(limitaciones)
       print(limite)
     '''
      cont = 0
      while True:
       inicio = i + tam * cont
       fin = inicio+tam
       if cadenatxt[inicio:fin] == limitaciones:
        cont += 1
       else:
        break
      limite = max(limite, cont)
     '''
     return limite

class cadenaDNA(object):
    def __init__(self,cadena):
     print("Si se creó el objeto")
     self.cadena = cadena

    def __str__(self):
     return "cadena: {}".format(self.cadena)
    '''
    def archivotxt(cadena2,existetxt):
     with open(cadena2) as linea:
      cadena2 = linea.read() #Guarda en un diccionario las cadenas en el txt
      #cadena =cadenaDNA(cadena2) #Creación del objeto de cadena
     #existetxt = True # Servirá para validar más adelante la existencia 
     existetxt = True
     return cadena2, existetxt
    '''
#Inicio
op = 0
cadenatxt = {}
cadenacsv = {}
existetxt = False
existecsv = False
a = ""
print("Bienvenido")
while op != 4:  
 print("Carga primero el txt y después el csv")
 print("1. Cargar archivo txt")
 print("2. Cargar archivo csv")
 print("3. Mostrar resultados")
 print("4. Salir")
 op = int(input("Ingrese lo que desea hacer: "))
 if op == 1:
  #cadenatxt = cadenaDNA.archivotxt(a)
  lineatxt = input("Ingresa el archivo txt: ")
  #cadenatxt = cadenaDNA.archivotxt(lineatxt,existetxt)
  existetxt = True
 elif op == 2:
  #cadenacsv = Persona.archivocsv(a)
  lineacsv = input("Ingresa el archivo csv: ")
  #cadenacsv = Persona.archivocsv(lineacsv,existecsv)
  existecsv = True  
 elif op == 3:
  if existetxt == True and existecsv == True:
   Persona.BUSCAR(lineacsv,lineatxt)
  else:
   print("Ingrese los archivos en orden")
 elif op == 4:
  print("Adiós")
 else:
  print("Incorrecto")