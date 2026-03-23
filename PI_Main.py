PI = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9, 5, 0, 2, 8, 8, 4, 1, 9, 7, 1, 6, 9, 3, 9, 9, 3, 7, 5, 1, 0, 5, 8]
LISTA_FINAL = []

mi_pi = input("PI --> "); print("\n")



if len(mi_pi) != len(PI):
    print("Ni siquiera acertaste la longitud de los números...")
    input("Pulsa Enter Para Salir...")
    exit()
else:
    for i in range(len(mi_pi)):
        if PI[i] == int(mi_pi[i]):
            LISTA_FINAL.append('◯')
        else:
            print("Te equivocaste en el dígito", i+1)
            LISTA_FINAL.append('✕')


PI_CIR = ['◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯', '◯']

if LISTA_FINAL != PI_CIR:
    print(LISTA_FINAL)
    input("Pulsa Enter Para Salir...")
else:
    print("Zero Errores.")
    input("Pulsa Enter Para Salir...")