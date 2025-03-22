def weakest_strong_link(strength):
    rows, cols = len(strength), len(strength[0])

    
    row_min = {i: min(strength[i]) for i in range(rows)} # tìm giá trị nhỏ nhất trong hàng i

    
    col_max = {j: max(strength[i][j] for i in range(rows)) for j in range(cols)} #tìm giá trị lớn nhất trong cột j

    # check xem có đảm bảo điều kiện số đó có nhỏ nhất trong hàng và lớn nhất trong cột không
    for i in range(rows):
        for j in range(cols):
            if strength[i][j] == row_min[i] and strength[i][j] == col_max[j]:
                return strength[i][j]

    return -1 #nếu không thỏa điều kiện vòng lặp for, trả về -1