def kol_sums(matrica):
    results = []
    max_lenght_row = max([len(row)for row in matrica])
    try:
        for i in range(max_lenght_row):
            count = 0
            for row in matrica:
                count += row[i]
            results.append(count)
    except:
        raise ValueError
    return results
matrica = [[1,2,3],[4,5,6]]
print(kol_sums(matrica))