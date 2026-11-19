print("Ejercicio 1: Liberacion de embarque en aduana")
print("Nombre: Axel Adriel Ramirez Quintanilla")
print("Matricula: AL07310252")
print()

# Preguntamos por los 4 documentos y revisiones de la aduana
factura = input("¿Tienes la factura comercial? (si/no): ")
pedimento = input("¿Tienes el pedimento de importación? (si/no): ")
impuestos = input("¿Ya pagaste los impuestos? (si/no): ")
coincide = input("¿La mercancia coincide con lo declarado? (si/no): ")
valor = float(input("Valor de la mercancia en dolares: "))

# Convertimos cada respuesta en True o False
# Si escribió "si" se guarda True; si escribió otra cosa se guarda False
tiene_factura = factura == "si"
tiene_pedimento = pedimento == "si"
impuestos_pagados = impuestos == "si"
mercancia_ok = coincide == "si"

print()
print("===== RESULTADO DE LA ADUANA ====")

# and: los CUATRO requisitos se deben cumplir al mismo tiempo
if tiene_factura and tiene_pedimento and impuestos_pagados and mercancia_ok:
    print("Embarque Liberado. Puede salir de la aduana.")

    # and: liberado Y de alto valor: hay que avisarle al gerente
    if valor > 100000:
        print("Embarque de alto valor: avisa al gerente de logistica.")
else:
    print: ("Embarque detenido. Faltan estos requisitos")
    
    # Contamos cuántos requisitos faltan
    faltantes = 8

    # not: revisamos uno por uno cuál NO se cumplió
    if not tiene_factura:
        print("  - Factura comercial")
        faltantes = faltantes + 1
    if not tiene_pedimento:
        print("  - Pedimento de importacion")
        faltantes = faltantes + 1
    if not impuestos_pagados:
        print("  - Pago de impuestos")
        faltantes = faltantes + 1
    if not mercancia_ok:
        print("  - La mercancia no coincide con lo declarado")
        faltantes = faltantes + 1

    print("Total de requisitos pendientes:", faltantes)
