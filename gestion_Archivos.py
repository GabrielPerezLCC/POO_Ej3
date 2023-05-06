import datetime
from Clases import Registro
class Archivos:
    def obtener_nombre_archivo(self):
        nombre_archivo = input("Ingrese Nombre Archivo a cargar: ")
        nombre_archivo = "{}.csv".format(nombre_archivo)
        return nombre_archivo
    
    def min_max(self, listaDatos: list):
        # Mostrar día y hora de menor y mayor valor por variable
        temperaturas = [registro[2] for registro in listaDatos if registro[2] is not None]
        humedades = [registro[3] for registro in listaDatos if registro[3] is not None]
        presiones = [registro[4] for registro in listaDatos if registro[4] is not None]

        if temperaturas:
            min_temperatura = min(temperaturas)
            max_temperatura = max(temperaturas)
            print("Mínimo y máximo de temperatura:")
            print("Mínimo: día {}, hora {}, temperatura {}".format(listaDatos[temperaturas.index(min_temperatura)][0], listaDatos[temperaturas.index(min_temperatura)][1], min_temperatura))
            print("Máximo: día {}, hora {}, temperatura {}".format(listaDatos[temperaturas.index(max_temperatura)][0], listaDatos[temperaturas.index(max_temperatura)][1], max_temperatura))
        else:
            print("No hay datos de temperatura.")

        if humedades:
            min_humedad = min(humedades)
            max_humedad = max(humedades)
            print("Mínimo y máximo de humedad:")
            print("Mínimo: día {}, hora {}, humedad {}".format(listaDatos[humedades.index(min_humedad)][0], listaDatos[humedades.index(min_humedad)][1], min_humedad))
            print("Máximo: día {}, hora {}, humedad {}".format(listaDatos[humedades.index(max_humedad)][0], listaDatos[humedades.index(max_humedad)][1], max_humedad))
        else:
            print("No hay datos de humedad.")

        if presiones:
            min_presion = min(presiones)
            max_presion = max(presiones)
            print("Mínimo y máximo de presión:")
            print("Mínimo: día {}, hora {}, presión {}".format(listaDatos[presiones.index(min_presion)][0], listaDatos[presiones.index(min_presion)][1], min_presion))
            print("Máximo: día {}, hora {}, presión {}".format(listaDatos[presiones.index(max_presion)][0], listaDatos[presiones.index(max_presion)][1], max_presion))
        else:
            print("No hay datos de presión.")

