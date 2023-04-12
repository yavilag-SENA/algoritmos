#Leer datos de archivo
import matplotlib.pyplot as plt

voltaje=120

cargas=[]

with open('corrientes.txt', 'r') as archivo_ingreso:   #f=open("asdf.txt","w")
	corrientes=[]
	corrientes2=[]
	
	for linea in archivo_ingreso:
		# Procesar cada línea del archivo
		dato = float(linea.strip())  # Eliminar espacios en blanco y saltos de línea
		corrientes.append(dato)  # Agregar el dato de cada corriente a la lista
		cargas.append(voltaje/dato) # Agregar dato de carga a la lista

with open('cargas_salida.txt', 'w') as archivo_salida:
	for i in range(len(cargas)):
		cadena=str(cargas[i])+"\n"
		archivo_salida.write(cadena)



archivo_ingreso.close()
archivo_salida.close()

for i in range(10):
	corrientes2.append(corrientes[i])

#plt.plot(corrientes,"r")
plt.plot(corrientes2,"g")
plt.show()


