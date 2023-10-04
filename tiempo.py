"""5) Módulo tiempo.py: Este módulo debe contener funciones para convertir entre diferentes unidades de tiempo, como segundos, minutos y horas. (1 punto) """
def Segundos_a_Minutos(sec):
    min = sec / 60
    return min

def Segundos_a_Horas(sec):
    hr = sec / 3600
    return hr

def Minutos_a_Segundos(sec):
    min = sec * 60
    return min

def Minutos_a_Horas(min):
    hr = min / 60
    return hr

def Horas_a_Segundos(hr):
    sec = hr * 3600
    return sec

def Horas_a_Minutos(hr):
    min = hr * 60
    return min

if __name__ == "__main__":
    # Ejemplos de uso
    print("Ejemplos de conversión de tiempo:")
    print("60sec a minutos:", Segundos_a_Minutos (60))
    print("7800sec a horas:", Segundos_a_Horas(7800))
    print("60min a segundos:",  Minutos_a_Segundos(60))
    print("60min a horas:", Minutos_a_Horas(60))
    print("60hr a sec:", Horas_a_Segundos(60))
    print("60hr a min:", Horas_a_Minutos(60))