def orden(list):
    cant = len(list)
 
    for posactual in range(cant - 1):
        indmenor = posactual
 
        for indbusca in range(posactual + 1, cant):
            if list[indbusca] < list[indmenor]:
                indmenor = indbusca
 
        if indmenor != posactual:
            list[posactual], list[indmenor] = list[indmenor], list[posactual]
 
    return list
 
 
if __name__ == "__main__":
    num = [13, 76, 8, 20, 3]
    print("El orden pre cambios es: ", num)
 
    orden(num)
    print("el nuevo orden es: ", num)
