liste = [5,2,4,6,1,3]
def merge(dizi):
    if len(dizi) > 1:
        print("Parçalanan değerler " + str(dizi))
        orta = len(dizi) // 2
        solDizi = dizi[:orta]
        sagDizi = dizi[orta:]
        merge(solDizi)
        merge(sagDizi)
        mergeSort(dizi,solDizi,sagDizi)

def mergeSort(dizi,solDizi,sagDizi):
    i,j,k = 0,0,0
    while i < len(solDizi) and j < len(sagDizi):
        if solDizi[i] < sagDizi[j]:
            dizi[k] = solDizi[i]
            i += 1
        else:
            dizi[k] = sagDizi[j]
            j += 1
        k += 1
    while i < len(solDizi):
        dizi[k] = solDizi[i]
        i += 1
        k += 1
    while j < len(sagDizi):
        dizi[k] = sagDizi[j]
        j += 1
        k += 1
        print("Birleştirilmiş hali " + str(dizi))

merge(liste)