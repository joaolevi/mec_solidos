import math

def cross_product(vector1, vector2): # Produto vetorial
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Os vetores devem ser tridimensionais")

    result = [0, 0, 0]
    result[0] = vector1[1] * vector2[2] - vector1[2] * vector2[1]
    result[1] = vector1[2] * vector2[0] - vector1[0] * vector2[2]
    result[2] = vector1[0] * vector2[1] - vector1[1] * vector2[0]

    return result

def vector_magnitude(vector): # Módulo
    return math.sqrt(sum([component**2 for component in vector]))

def unit_vector(vector): # Normalização
    magnitude = vector_magnitude(vector)
    if magnitude == 0:
        raise ValueError("O vetor tem magnitude zero, não pode ser normalizado.")
    return [component / magnitude for component in vector]

def dot_product(vector1, vector2): # u * v
    if len(vector1) != len(vector2):
        raise ValueError("Os vetores devem ter o mesmo comprimento")

    return sum(x * y for x, y in zip(vector1, vector2))

def scalar_product_with_cross(vector1, vector2, scalar_vector): # u * (r x F)
    cross_result = cross_product(vector1, vector2)
    return dot_product(cross_result, scalar_vector)

# Exemplo de uso
if __name__ == "__main__":
    scalar_vector = [0.8944, 0.4472, 0]
    vector1 = [0.6, 0, 0]
    vector2 = [0, 0, -300]

    scalar_product = scalar_product_with_cross(vector1, vector2, scalar_vector)
    print("O produto escalar do produto vetorial de", vector1, "e", vector2, "com", scalar_vector, "é", scalar_product)
