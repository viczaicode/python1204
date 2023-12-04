def negyedik():
    lista = []
    beFajl = open("fajlok/dal.txt", "r", encoding="utf-8")
    for sor in beFajl:
        lista.append(sor.strip())
    beFajl.close()

    # lista kiírása
    kiFajl = open("fajlok/negyedik.txt", "w", encoding="utf-8")
    for index in range(0, len(lista), 1):
        daraboltSor = lista[index].split(" ")
        print(daraboltSor[0], file=kiFajl)

    kiFajl.close()