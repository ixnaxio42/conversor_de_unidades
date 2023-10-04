"""1) Módulo temperatura.py: Este módulo debe contener funciones para convertir entre diferentes unidades de temperatura, como Celsius, Fahrenheit y Kelvin.(0.5 puntos) """
"""2) Módulo masa.py: Este módulo debe contener funciones para convertir entre diferentes unidades de masa, como kilogramos, libras y onzas.(0.5 puntos) """
"""3) Crear el primer versionamiento con git de los dos módulos creados de temperatura y masa (usar git add y git commit ). (0.5 puntos) """
"""4) Crear una nueva rama llamada “desarrollo” y en esta nueva rama agregar los módulos tiempo.py y convertidor.py (recuerda usar git branch ). (0.5 puntos) """
"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
"""6) Módulo convertidor.py: Este módulo importa los módulos de masa, temperatura y tiempo. Actúa como el punto de entrada del programa. Debe permitir a los usuarios seleccionar la categoría de conversión deseada (temperatura, masa o tiempo), ingresar el valor a convertir y las unidades de origen y destino, y obtener el resultado de la conversión.(2 puntos) """
"""7) Versionar esta rama “desarrollo” con git add y git commit para luego fusionar con la rama master (para fusionar, usar: git merge). (1 punto) """
""" Desde la rama main o master subir al nuevo repositorio de github llamado conversor_de_unidades. (1 punto) """

""" Recuerda que cada uno de los módulos, deben incluir el bloque if __name__ == "__main__" para sus pruebas en cada módulo. """
#Ignacio navarro
import temperatura
import masa
import tiempo
def main():
    while True:
        # Muestra el menú principal
        print("Menú Principal:")
        print("[1] convertir de Celcius a Fahrenheit")
        print("[2] convertir celsius a kelvin")
        print("[3] convertir de fahrenheit a celsius ")
        print("[4] convertir de fahrenheit a kelvin ")
        print("[5] convertir de kelvin a celsius")
        print("[6] convertir de kelvin a fahrenheit")
        print("[7] convertir de Kilogramos a Gramos")
        print("[8] convertir de Kilogramos a Toneladas ")
        print("[9] convertir de Gramos a Kilogramos")
        print("[10] convertir de Gramos a Toneladas ")
        print("[11] convertir de Toneladas a Kilogramos ")
        print("[12] convertir de Toneladas a Gramos")
        print("[13] convertir de Segundos a Minutos ")
        print("[14] convertir de Segundos a Horas")
        print("[15] convertir de Minutos a Segundos")
        print("[16] convertir de Minutos a Horas ")
        print("[17] convertir de Horas a Segundos ")
        print("[18] convertir de Horas a Minutos")
        print("[0] Salir")
        
        # Solicita al usuario que ingrese una opción
        opcion = input("Ingrese una opción: ")
        valor_inicial= int(input("igrese valor inicial"))
        try:
            opcion = int(opcion)
            if opcion == 0:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            elif opcion == 1:
                respuesta = temperatura.celsius_a_fahrenheit(valor_inicial)
                print("[1] Convertir Celcius a Fahrenheit  ")
            elif opcion == 2:
                respuesta = temperatura.celsius_a_kelvin(valor_inicial)
                print("[2] convertir celsius a kelvin")
            elif opcion == 3:
                respuesta = temperatura.fahrenheit_a_celsius(valor_inicial)
                print("[3] convertir de fahrenheit a celsius ")
            elif opcion == 4:
                respuesta = temperatura.fahrenheit_a_kelvin(valor_inicial)
                print("[4] convertir de fahrenheit a kelvin ")
            elif opcion == 5:
                respuesta = temperatura.kelvin_a_celsius(valor_inicial)
                print("[5] convertir de kelvin a celsius")
            elif opcion == 6:
                respuesta = temperatura.kelvin_a_fahrenheit(valor_inicial)
                print("[6] convertir de kelvin a fahrenheit")
            elif opcion == 7:
                respuesta = masa.Kilogramos_a_Gramos(valor_inicial)
                print("[7] convertir de Kilogramos a Gramos")
            elif opcion == 8:
                respuesta = masa.Kilogramos_a_Toneladas(valor_inicial)
                print("[8] convertir de Kilogramos a Toneladas ")
            elif opcion == 9:
                respuesta = masa.Gramos_a_Kilogramos(valor_inicial)
                print("[9] convertir de Gramos a Kilogramos")
            elif opcion == 10:
                respuesta = masa.Gramos_a_Toneladas(valor_inicial)
                print("[10] convertir de Gramos a Toneladas ")
            elif opcion == 11:
                respuesta = masa.Toneladas_a_Kilogramos(valor_inicial)
                print("[11] convertir de Toneladas a Kilogramos ")
            elif opcion == 12:
                respuesta = masa.Toneladas_a_Gramos(valor_inicial)
                print("[12] convertir de Toneladas a Gramos")
            elif opcion == 13:
                respuesta = tiempo.Segundos_a_Minutos(valor_inicial)
                print("[13] convertir de Segundos a Minutos ")
            elif opcion == 14:
                respuesta = tiempo.Segundos_a_Horas(valor_inicial)
                print("[14] convertir de Segundos a Horas")
            elif opcion == 15:
                respuesta = tiempo.Minutos_a_Segundos(valor_inicial)
                print("[15] convertir de Minutos a Segundos")
            elif opcion == 16:
                respuesta = tiempo.Minutos_a_Horas(valor_inicial)
                print("[16] convertir de Minutos a Horas ")
            elif opcion == 17:
                respuesta = tiempo.Horas_a_Segundos(valor_inicial)
                print("[17] convertir de Horas a Segundos ")
            elif opcion == 18:
                respuesta = tiempo.Horas_a_Minutos(valor_inicial)
                print("[18] convertir de Horas a Minutos")

            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Solo puede ingresar valores numéricos.")

if __name__ == "__main__":
    main()