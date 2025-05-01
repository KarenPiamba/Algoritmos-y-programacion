usuarios = {
    "iperurena": {"nombre": "Iñaki", "apellido": "Perurena", "password": "123123"},
    "fmuguruza": {"nombre": "Fermín", "apellido": "Muguruza", "password": "654321"},
    "aolaizola": {"nombre": "Aimar", "apellido": "Olaizola", "password": "123456"}
}
intentos = 0
while intentos < 3:
    usuario=input("Usuario: ")
    contraseña=input("Contraseña: ")
    if usuario in usuarios and usuarios[usuario]["password"]==contraseña:
        datos=usuarios[usuario]
        print(f"Bienvenido {datos["nombre"]} {datos["apellido"]}")
        break
    else:
        print("Usuario o contraseña incorrectos.")
        intentos=intentos
