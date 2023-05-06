from Clases import Registro
from gestion_Archivos import Archivos
from Menu_Varios import Menu

import csv

if __name__ == "__main__":
   archivo_obj=Archivos()
   nombre_archivo=archivo_obj.obtener_nombre_archivo()
   with open (nombre_archivo, "r") as archivo:
      registros=archivo.readlines()
      cantreg=len(registros)
      listaDatos=[[None for _ in range(24)]for _ in range(cantreg)]
      for i, registro in enumerate(registros):
            datos = registro.split(",")
            dia=int(datos[0])
            #print("dia: ",dia)
            hora=int(datos[1])
            #print("hora: ",hora)
            temperatura = float(datos[2])
            humedad = float(datos[3])
            presion = float(datos[4])
            regist_obj=Registro(dia,hora,temperatura,humedad,presion)
            listaDatos[dia-1][hora] = [temperatura, humedad, presion]
            #listaDatos[i % 24][i] = [temperatura, humedad, presion]
            print("día {} hora  {}  {}".format(dia,hora,listaDatos[dia-1][hora]))

   opcion= Menu.menuOpciones()
   regist_obj=Archivos()
   if opcion=="1":
       regist_obj.min_max(listaDatos)