saldo=1000000
while True:
    print("\n--- Cajero Automático ---")
    print("1. Depositar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1": 
        monto = int(input("Ingrese el monto a depositar: "))
        if monto > 0:
            saldo=saldo+ monto
            print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
        else:
            print("El monto debe ser mayor a 0.")
    
    elif opcion == "2":
        monto = int(input("Ingrese el monto a retirar: "))
        if monto > 0:
            if monto <= saldo:
                saldo=saldo-monto
                print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto debe ser mayor a 0.")
    elif opcion == "3":
        print(f"Saldo actual: ${saldo}")
    elif opcion == "4":
        print("Gracias por usar el cajero automático.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
