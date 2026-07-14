# =====================================================================
# Curso: Fundamentos de Programación (213022)
# Fase 5: Evaluación Final POA
# Problema 3: Auditoría de Inventario
# =====================================================================

# --- PASO 1: Módulo / Función de Lógica de Negocio ---
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Determina la cantidad exacta a pedir para un artículo.
    Aplica la estructura de control condicional (if-else).
    """
    # Si el Stock Actual es menor al Stock Mínimo, se pide la diferencia
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    # Si el Stock Actual es suficiente, no se pide nada (0 unidades)
    else:
        return 0


# --- PASO 2: Definición de la Matriz de Datos ---
# Formato: [Código, Nombre, Stock Actual, Stock Mínimo]
inventario = [
    ["ART01", "Arroz 1kg", 15, 30],
    ["ART02", "Aceite 1L", 5, 10],
    ["ART03", "Azúcar 1kg", 25, 20],  # No requiere (stock actual es mayor)
    ["ART04", "Café 500g", 8, 15],
    ["ART05", "Sal 1kg", 12, 12]      # No requiere (stock actual es igual al mínimo)
]


# --- PASO 3: Función Principal para Procesar y Mostrar Resultados ---
def ejecutar_auditoria():
    print("=========================================")
    print("        REPORTE DE PEDIDOS DE INVENTARIO ")
    print("=========================================\n")
    
    # Cabecera de la tabla de salida
    print(f"{'Artículo':<15} | {'Cantidad a Pedir'}")
    print("-" * 35)
    
    # Estructura de repetición (Ciclo For) para recorrer la matriz
    for articulo in inventario:
        # Extraemos los datos de cada columna de la fila actual
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        # Llamamos al módulo para realizar el cálculo individual
        cantidad_a_solicitar = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Imprimimos el resultado formateado
        print(f"{nombre:<15} | {cantidad_a_solicitar} unidades")
        
    print("\n=========================================")


# --- PASO 4: Punto de Entrada del Programa ---
if __name__ == "__main__":
    ejecutar_auditoria()
