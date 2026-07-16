# ===========================================================================
# Curso: Fundamentos de Programación (213022)
# Fase 5: Evaluación Final POA
# Problema 3: Auditoría de Inventario
# Estudiante: Johnattan José De los rios Benavides
# ===========================================================================

# --- PASO 1: Módulo / Función de Lógica de Negocio ---
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Determina la cantidad exacta a pedir para un artículo.
    Aplica la estructura de control condicional (if-else).
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0  # Retorna 0 si hay suficiente stock

# --- PASO 2: Estructura de Control Iterativa (Ciclo) y Entrada de Datos ---
def ejecutar_auditoria():
    print("===========================================================================")
    print("                     REPORTE DE PEDIDOS DE INVENTARIO                      ")
    print("===========================================================================")
    
    # MATRIZ SOLICITADA: Representada como una lista de listas (arreglo bidimensional)
    # Formato de columnas: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]
    matriz_inventario = [
        ["A001", "Arroz 1kg", 15, 30],
        ["A002", "Aceite 1L", 5, 10],
        ["A003", "Azúcar 1kg", 25, 20],
        ["A004", "Café 500g", 8, 15],
        ["A005", "Sal 1kg", 12, 10]
    ]
    
    # Cabecera de la tabla de salida
    print(f"{'Código':<8} | {'Artículo':<15} | {'Cantidad a Pedir':<15}")
    print("-" * 45)
    
    # Recorrido de la matriz mediante índices
    for fila in matriz_inventario:
        codigo = fila[0]
        nombre = fila[1]
        actual = fila[2]
        minimo = fila[3]
        
        # Llamado a la función lógica de negocio
        cantidad_pedir = calcular_cantidad_a_pedir(actual, minimo)
        
        # Mostrar los resultados limpios en pantalla
        print(f"{codigo:<8} | {nombre:<15} | {cantidad_pedir} unidades")
        
    print("=" * 45)

# Ejecutar el programa principal
if __name__ == "__main__":
    ejecutar_auditoria()
