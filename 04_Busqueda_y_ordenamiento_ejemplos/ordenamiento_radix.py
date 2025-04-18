def obtener_digito(numero, posicion_digito, base = 10):
    """
    Obtiene el dígito en la posición especificada (de derecha a izquierda) de un número.
    Devuelve cero si la posición es mayor que el número de dígitos del número.
    """
    return (numero // (base ** posicion_digito)) % base

def ordenamiento_radix(lista):
    """
    Ordena una lista de números enteros utilizando el algoritmo de ordenamiento Radix.
    """
    # Encuentra el número máximo para determinar el número de dígitos
    max_num = max(lista)
    exp = 1  # Exponente para la posición del dígito
    lista_aux = [[] for _ in range(10)]  
    pos = 0  # Inicializa la posición del dígito
    while max_num // exp > 0:
        # Coloca los números en la lista auxiliar según el dígito actual
        for num in lista:
            digit = obtener_digito(num, pos)  # Obtiene el dígito en la posición actual
            lista_aux[digit].append(num)

        # Reconstruye la lista original a partir de la lista auxiliar
        sig_pos = 0  # Inicializa la posición en la lista original
        for sublist in lista_aux:
            for num in sublist:
                lista[sig_pos] = num  # Añade el número a la lista original 
                sig_pos += 1    


        # Limpia la lista auxiliar para la siguiente posición de dígito
        lista_aux = [[] for _ in range(10)]

        # Aumenta el exponente para pasar al siguiente dígito
        exp *= 10
        pos += 1
 
 
    return lista



if __name__ == "__main__":
    
    cifra1 = 123467
    posicion = 2
    print(f"El dígito en la posición {posicion} de {cifra1} es: {obtener_digito(cifra1, posicion)}")
    
    cifra2 = 17
    posicion = 3
    print(f"El dígito en la posición {posicion} de {cifra2} es: {obtener_digito(cifra2, posicion)}")

    lista = [170, 45, 75, 90, 802, 24, 2, 66]
    print(f"Lista original: {lista}")
    lista_ordenada = ordenamiento_radix(lista)
    print(f"Lista ordenada: {lista_ordenada}")