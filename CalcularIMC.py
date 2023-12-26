print("Calculadora de IMC")
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    return weight / height ** 2

weight = float(input('Ingrese su peso corporal en Kilos:'))
height = float(input('Ingrese su Altura en metros:'))


print(bmi(weight,height ))
