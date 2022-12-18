Calificación = int(input("Ingrese la calificación: "))
if Calificación <=2:
  print("Reprobado")
else:
  if Calificación <=4:
    print("Insuficiente")
  elif Calificación <=6:
    print("Regular")
  elif Calificación <=8:
    print("Sobresaliente")
  elif Calificación <=10:
    print("Excelente")
if Calificación>10:
  print("EL número ingresado no es válido")
 