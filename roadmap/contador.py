contador_luz = 0

for i in range (5):
  luz = str(input(f"La luz de la habitacion {i + 1} esta prendida?: "))
  if (luz == "si"):
    contador_luz += 1

if contador_luz >= 2:
  print("PELIGRO SE TE VA A GASTAR LA LUZ")

else:
  print("No vas a gastar la luz")

print(contador_luz)