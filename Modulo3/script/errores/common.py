## otros errores

## typado de error 
""" try:
    listav1=[1,2,3,4,5,5,6,7]
    dictv1={"name":1}
    print(len(listav1))
    print(listav1[2])
    print(dictv1["name"])
    print(0/0)
except Exception as e:
    print('este fue el error',e) """


def sumar(nu1:int,nu2:int)->int:
    return nu1+nu2

try:
    nu1=int(input("ingrese el numero 1: "))
    nu2=int(input("ingrese el numero 2: "))
    res=sumar(nu1,nu2)
except Exception as f:
    print("ocurrio un error ",f)
else:
    print(res)
    print("Todo ha funcionado correctamente")
finally:
    print("siempre me ejecuto asi falle o sea correcto el bloque try")