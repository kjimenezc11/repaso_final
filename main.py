import csv
import pandas as pd



def menu():
    mantenimientos = []
    while True:  
        try:
            
            print("\nMenu de opciones")
            print("1. Registrar moto:")
            print("2. Guardar cambios moto")
            print("3. Consultar mantenimientos")
            print("4. Consultar mantenimientos de moto: ")
            print("5. Salir")
            opcion = int(input("Seleccione una opcion: "))
    

            if opcion == 1:
               registrar_mantenimientos(mantenimientos)
            elif opcion == 2:
                guardar_mantenimientos(mantenimientos)
            elif opcion == 3:
                consultar_mantenimientos()
            elif opcion == 4:
                consultar_mantenimientos_moto()
            elif opcion == 5:
                print("Saliendo del programa, Hasta luego!")
                break
            else:
                print("Opcion no valida")   
        except ValueError:
            print("Entrada no valida, por favor ingrese un numero entre 1 y 4.")

def consultar_mantenimientos_moto():
    try: 
        df = pd.read_csv("mantenimientos.csv")
        if df.empty:
           print("No hay mantenimientos registrados.")
        else:
           moto = input("Ingrese el nombre de la moto a consultar: ")
           mantenimientos_moto = df[df['cliente'] == moto]
           if mantenimientos_moto.empty:
               print(f"No hay mantenimientos registrados para la moto: {moto}")
           else:
               print(f'\nMantenimientos registrados para la moto {moto}:')
               print(mantenimientos_moto)
    except FileNotFoundError:
        print("No se encontro el archivo de mantenimientos.")

def TiposMantenimientos():
    print('Tipos de mantenimiento:')
    print('1. Cambio de aceite')
    print('2. Revisión de frenos')
    print('3. Sustitución de neumáticos')
    print('4. Inspección general')
   

def registrar_mantenimientos(mantenimientos:list):
    while True:
        try:
            TiposMantenimientos()
            tipo_mantenimiento = int(input("Seleccione el tipo de mantenimiento (1-4): "))
            costo_mantenimiento = float(input("Ingrese el costo del mantenimiento: "))
            fecha_mantenimiento = input("Ingrese la fecha del mantenimiento (DD/MM/AAAA): ")
            cliente = input("Ingrese el nombre del cliente: ")
            cantidad_km = float(input("Ingrese la cantidad de kilometros recorridos: "))
            numero_placa = input("Ingrese el numero de placa de la moto: ")
            numero_placa = numero_placa.upper()
            if costo_mantenimiento < 0 or tipo_mantenimiento < 0:
                print("El costo y el tipo de mantenimiento no pueden ser negativos. Por favor, intente de nuevo.")
                continue
             
            mantenimiento = {
                "tipo_mantenimiento": tipo_mantenimiento,
                "costo_mantenimiento": costo_mantenimiento,
                "fecha_mantenimiento": fecha_mantenimiento,
                "cliente": cliente,
                "cantidad_km": cantidad_km,
                "numero_placa": numero_placa
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
               guardado = csv.DictWriter(archivo, fieldnames=['tipo_mantenimiento', 'costo_mantenimiento', 'fecha_mantenimiento', 'cliente', 'cantidad_km', 'numero_placa'])
               guardado.writeheader()
               guardado.writerows(mantenimientos)
               mantenimientos = []
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
           df['Subtotal'] = df['costo_mantenimiento'].sum()
           Total = df['Subtotal'].sum()
           print(f'Total de mantenimiento:{Total:.2f}')

           mantenimiento_mas_echo = df.groupby('tipo_mantenimiento')['cantidad_km'].sum().idxmax()
           print(f'Mantenimiento mas echo: {mantenimiento_mas_echo}')

           tendencia_cliente = df[df['cliente'] == df['cliente'].mode()[0]]
           print('\nTendencia de mantenimiento por cliente:')
           print(tendencia_cliente)
    except FileNotFoundError:
        print("No se encontro el archivo de mantenimientos.")

if __name__ == "__main__":
    print("Bienvenido al sistema MJ")
    menu()