def ordenburb(lista):

    cant = len(lista)
 
    for pasada in range(1, cant):
        for j in range(0, cant - pasada):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
    return lista
 
 
if __name__ == "__main__":
    nums = [8, 23, 56, 78, 15]
    print("Lista inalterada: ", nums)
 
    ordenburb(nums)
    print("nueva lista: ", nums)
 