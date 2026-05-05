# Proyecto calculadora
import areas
import perimetros

def menu():
    print("--- CALCULADORA GEOMÉTRICA ---")
    print("1. Calcular Área de Cuadrado")
    print("2. Calcular Perímetro de Cuadrado")
    # Aquí podéis añadir más opciones según necesitéis
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        lado = float(input("Lado: "))
        print(f"Resultado: {areas.area_cuadrado(lado)}")
    elif opcion == "2":
        lado = float(input("Lado: "))
        print(f"Resultado: {perimetros.perimetro_cuadrado(lado)}")

menu()
