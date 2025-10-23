import csv
import pandas as pd


def menu():
    mantenimientos = []
    while True:
        try:
            print("\n=== MENÚ DE OPCIONES ===")
            print("1. Registrar mantenimiento")
            print("2. Guardar mantenimientos en archivo")
            print("3. Consultar todos los mantenimientos")
            print("4. Consultar mantenimientos por moto")
            print("5. Salir")

            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_mantenimientos(mantenimientos)
            elif opcion == 2:
                guardar_mantenimientos(mantenimientos)
            elif opcion == 3:
                consultar_mantenimientos()
            elif opcion == 4:
                consultar_mantenimientos_moto()
            elif opcion == 5:
                print(" Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print(" Opción no válida.")
        except ValueError:
            print(" Entrada no válida, por favor ingrese un número del 1 al 5.")


# ==============================
#   FUNCIÓN: REGISTRAR
# ==============================
def TiposMantenimientos():
    print("\nTipos de mantenimiento disponibles:")
    print("1. Cambio de aceite")
    print("2. Revisión de frenos")
    print("3. Sustitución de neumáticos")
    print("4. Inspección general")


def registrar_mantenimientos(mantenimientos: list):
    while True:
        try:
            TiposMantenimientos()
            tipo_mantenimiento = int(input("Seleccione el tipo de mantenimiento (1-4): "))
            costo_mantenimiento = float(input("Ingrese el costo del mantenimiento: "))
            fecha_mantenimiento = input("Ingrese la fecha del mantenimiento (DD/MM/AAAA): ")
            cliente = input("Ingrese el nombre del cliente: ")
            cantidad_km = float(input("Ingrese la cantidad de kilómetros recorridos: "))
            numero_placa = input("Ingrese el número de placa de la moto: ").upper()

            if costo_mantenimiento < 0:
                print(" El costo no puede ser negativo.")
                continue

            # Diccionario del mantenimiento
            mantenimiento = {
                "tipo_mantenimiento": tipo_mantenimiento,
                "costo_mantenimiento": costo_mantenimiento,
                "fecha_mantenimiento": fecha_mantenimiento,
                "cliente": cliente,
                "cantidad_km": cantidad_km,
                "numero_placa": numero_placa
            }

            mantenimientos.append(mantenimiento)
            print(" Mantenimiento registrado correctamente.")

            continuar = input("¿Desea registrar otro mantenimiento? (s/n): ").lower()
            if continuar != 's':
                break

        except ValueError:
            print(" Entrada no válida. Intente de nuevo.")


# ==============================
#   FUNCIÓN: GUARDAR
# ==============================
def guardar_mantenimientos(mantenimientos: list):
    try:
        if not mantenimientos:
            print(" No hay mantenimientos para guardar.")
            return

        archivo_existe = False
        try:
            with open("mantenimientos.csv", "r") as _:
                archivo_existe = True
        except FileNotFoundError:
            archivo_existe = False

        # Abrir el archivo y guardar
        with open("mantenimientos.csv", "a", newline='', encoding='utf-8') as archivo:
            fieldnames = ['tipo_mantenimiento', 'costo_mantenimiento', 'fecha_mantenimiento', 'cliente', 'cantidad_km', 'numero_placa']
            writer = csv.DictWriter(archivo, fieldnames=fieldnames)

            # Escribir encabezado solo si el archivo no existe
            if not archivo_existe:
                writer.writeheader()

            writer.writerows(mantenimientos)
            mantenimientos.clear()

        print(" Mantenimientos guardados exitosamente.")

    except Exception as e:
        print(f" Error al guardar los mantenimientos: {e}")


# ==============================
#   FUNCIÓN: CONSULTAR TODOS
# ==============================
def consultar_mantenimientos():
    try:
        df = pd.read_csv("mantenimientos.csv")

        if df.empty:
            print(" No hay mantenimientos registrados.")
            return

        print("\n MANTENIMIENTOS REGISTRADOS:")
        print(df.to_string(index=False))

        # Calcular total
        total = df['costo_mantenimiento'].sum()
        print(f"\n Total general de mantenimientos: {total:.2f} colones")

        # Tipo de mantenimiento más realizado
        mantenimiento_mas_hecho = df['tipo_mantenimiento'].value_counts().idxmax()
        cantidad_mas_hecho = df['tipo_mantenimiento'].value_counts().max()
        print(f" Mantenimiento más realizado: Tipo {mantenimiento_mas_hecho} ({cantidad_mas_hecho} veces)")

        # Cliente con más registros
        cliente_top = df['cliente'].mode()[0]
        print(f" Cliente con más mantenimientos: {cliente_top}")

    except FileNotFoundError:
        print(" No se encontró el archivo de mantenimientos.")
    except Exception as e:
        print(f" Error al consultar mantenimientos: {e}")


# ==============================
#   FUNCIÓN: CONSULTAR POR MOTO
# ==============================
def consultar_mantenimientos_moto():
    try:
        df = pd.read_csv("mantenimientos.csv")

        if df.empty:
            print(" No hay mantenimientos registrados.")
            return

        moto = input("Ingrese el número de placa de la moto a consultar: ").upper()
        mantenimientos_moto = df[df['numero_placa'] == moto]

        if mantenimientos_moto.empty:
            print(f" No hay mantenimientos registrados para la moto con placa {moto}.")
        else:
            print(f"\n Mantenimientos registrados para la moto {moto}:")
            print(mantenimientos_moto.to_string(index=False))

            total_moto = mantenimientos_moto['costo_mantenimiento'].sum()
            print(f"\n Total invertido en la moto {moto}: {total_moto:.2f} colones")

    except FileNotFoundError:
        print(" No se encontró el archivo de mantenimientos.")
    except Exception as e:
        print(f" Error al consultar mantenimientos por moto: {e}")


# ==============================
#   PROGRAMA PRINCIPAL
# ==============================
if __name__ == "__main__":
    print("🏍️ Bienvenido al sistema de control de mantenimientos MJ")
    menu()
