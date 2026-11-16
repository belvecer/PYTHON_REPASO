class Ejercicio4:
    inventario = ["camisetas", "pantalones", "zapatos", "gorras", "bufandas"]
    inventario.append("clacetines")
    inventario.insert(1, "abrigos")

    eliminar = inventario.pop(-1)

    for prenda in inventario:
        print(f"Tenemos disponible en stock: {prenda}")

    if "zapatos" in inventario:
        print("\n¡Atención! Los zapatos todavía están disponibles en el inventario.")
    else:
        print("\nLos zapatos ya no se encuentran en el inventario.")