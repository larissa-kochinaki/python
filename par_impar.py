def select_sort(arr):
    # Percorre todos os elementos do array
    for i in range(len(arr)):
        # Assume que o primeiro elemento não ordenado é o menor
        min_index = i
        # Percorre o restante do array para encontrar o menor elemento
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

