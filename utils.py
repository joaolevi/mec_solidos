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

def angle_between_vectors(vector1, vector2): # Ângulo entre vetores
    dot = dot_product(vector1, vector2)
    magnitude1 = vector_magnitude(vector1)
    magnitude2 = vector_magnitude(vector2)
    return math.acos(dot / (magnitude1 * magnitude2))

def binary_moment(vector1, vector2, force1, force2): # Momento binário
    cross_result_1 = cross_product(vector1, force1)
    cross_result_2 = cross_product(vector2, force2)
    return [x + y for x, y in zip(cross_result_1, cross_result_2)]

def tangent_angle(vector):
    angle_radians = math.atan(vector[1] / vector[0])
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

def sum_vectors(vector1, vector2):
    return [x + y for x, y in zip(vector1, vector2)]

def menu():
    print("1. Produto vetorial")
    print("2. Módulo")
    print("3. Normalização")
    print("4. Produto escalar")
    print("5. Produto escalar com produto vetorial")
    print("6. Binario")
    print("7. Angulo entre vetores")
    print("8. Angulo tangente")
    print("9. Somar vetores")
    print("10. Sair")
    return int(input("Escolha uma opção: "))

def main():
    while True:
        option = menu()
        if option == 1:
            vector1 = [float(x) for x in input("Digite o primeiro vetor: ").split()]
            vector2 = [float(x) for x in input("Digite o segundo vetor: ").split()]
            print("Produto vetorial:", cross_product(vector1, vector2))
        elif option == 2:
            vector = [float(x) for x in input("Digite o vetor: ").split()]
            print("Módulo:", vector_magnitude(vector))
        elif option == 3:
            vector = [float(x) for x in input("Digite o vetor: ").split()]
            print("Vetor normalizado:", unit_vector(vector))
        elif option == 4:
            vector1 = [float(x) for x in input("Digite o primeiro vetor: ").split()]
            vector2 = [float(x) for x in input("Digite o segundo vetor: ").split()]
            print("Produto escalar:", dot_product(vector1, vector2))
        elif option == 5:
            scalar_vector = [float(x) for x in input("Digite o versor: ").split()]
            vector1 = [float(x) for x in input("Digite o primeiro vetor: ").split()]
            vector2 = [float(x) for x in input("Digite o segundo vetor: ").split()]
            print("Produto escalar com produto vetorial:", scalar_product_with_cross(vector1, vector2, scalar_vector))
        elif option == 6:
            vector1 = [float(x) for x in input("Digite o primeiro vetor: ").split()]
            vector2 = [float(x) for x in input("Digite o segundo vetor: ").split()]
            force1 = [float(x) for x in input("Digite a força 1: ").split()]
            force2 = [float(x) for x in input("Digite a força 2: ").split()]
            print("Momento binário:", binary_moment(vector1, vector2, force1, force2))
        elif option == 7:
            vector1 = [float(x) for x in input("Digite o primeiro vetor: ").split()]
            vector2 = [float(x) for x in input("Digite o segundo vetor: ").split()]
            print("Ângulo entre vetores:", angle_between_vectors(vector1, vector2))
        elif option == 8:
            vector = [float(x) for x in input("Digite o vetor: ").split()]
            print("Ângulo tangente:", tangent_angle(vector))
        elif option == 9:
            vector1 = [float(x) for x in input("Digite o primeiro vetor: ").split()]
            vector2 = [float(x) for x in input("Digite o segundo vetor: ").split()]
            print("Soma dos vetores:", sum_vectors(vector1, vector2))
        elif option == 10:
            break
        else:
            print("Opção inválida")

# Exemplo de uso
if __name__ == "__main__":
    # scalar_vector = [0.8944, 0.4472, 0]
    # vector1 = [0.6, 0, 0]
    # vector2 = [0, 0, -300]

    # scalar_product = scalar_product_with_cross(vector1, vector2, scalar_vector)
    # print("u * (r x F)", vector1, "e", vector2, "com", scalar_vector, "é", scalar_product)
    main()
