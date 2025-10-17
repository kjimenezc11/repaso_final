import csv
import pandas as pd



def menu():
    while True:  
        try:
            mantenimientos = []
            print("\nMenu de opciones")
            print("1. Registrar moto:")
            print("2. Guardar cambios moto")
            print("3. Consultar moto")
            print("4. Salir")
            opcion = int(input("Seleccione una opcion: "))
    

            if opcion == 1:
               registrar_mantenimientos(mantenimientos)
            elif opcion == 2:
                print("Guardar cambios moto")
            elif opcion == 3:
                print("Consultar moto")
            elif opcion == 4:
                print("Saliendo del programa, Hasta luego!")
                break
            else:
                print("Opcion no valida")   
        except ValueError:
            print("Entrada no valida, por favor ingrese un numero entre 1 y 4.")



def registrar_mantenimientos(mantenimientos:list):
    while True:
        try:
            pass
            tipo_mantenimiento = input("Ingrese el tipo de mantenimiento: ")
            costo_mantenimiento = float(input("Ingrese el costo del mantenimiento: "))
            fecha_mantenimiento = input("Ingrese la fecha del mantenimiento (DD/MM/AAAA): ")
            cliente = input("Ingrese el nombre del cliente: ")
            cantidad_km = float(input("Ingrese la cantidad de kilometros recorridos: "))
            
            if costo_mantenimiento < 0 or tipo_mantenimiento < 0:
                print("El costo y el tipo de mantenimiento no pueden ser negativos. Por favor, intente de nuevo.")
                continue
             
            mantenimiento = {
                "tipo_mantenimiento": tipo_mantenimiento,
                "costo_mantenimiento": costo_mantenimiento,
                "fecha_mantenimiento": fecha_mantenimiento,
                "cliente": cliente,
                "cantidad_km": cantidad_km
            }


            mantenimientos.append(mantenimiento)
            
            continuar = input("¿Desea registrar otro mantenimiento? (s/n): ").lower()
            if continuar != 's':
                break



        except ValueError:
            print("Entrada no valida, por favor intente de nuevo.")
            continue


def guardar_mantenimientos(mantenimientos:list):
    try:
       if not mantenimientos:
           print("No hay mantenimientos para guardar.")
           return
       else:
           with open("mantenimientos.csv", "a") as archivo:
               guardado = csv.DictWriter(archivo, fieldnames=['tipo_mantenimiento', 'costo_mantenimiento', 'fecha_mantenimiento', 'cliente', 'cantidad_km'])
               guardado.writeheader()
               guardado.writerows(mantenimientos)
           print("Mantenimientos guardados exitosamente.")
    except Exception as e:
        print(f"\nError al guardar los mantenimientos: {e}")



def consultar_mantenimientos():
    try: 
        df = pd.read_csv("mantenimientos.csv")
        if df.empty:
           print("No hay mantenimientos registrados.")
        else:
           print('\nMantenimientos registrados:')
           df['Subtotal'] = df['cantidad_km'] * df['costo_mantenimiento']
           Total = df['Subtotal'].sum()
           print(f'Total de mantenimiento:{Total:.2f}')

           mantenimiento_mas_echo = df.groupby('tipo_mantenimiento')['cantidad_km'].sum().idxmax()
           print(f'Mantenimiento mas echo: {mantenimiento_mas_echo}')

            tendencia_cliente = df

        
if __name__ == "__main__":
    print("Bienvenido al sistema MJ")
    menu()