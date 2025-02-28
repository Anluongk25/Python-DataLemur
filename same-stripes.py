def is_same_stripes(matrix):
    diagonal_values = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            key = i - j  # Chỉ số đại diện cho một đường chéo duy nhất
            if key not in diagonal_values:
                diagonal_values[key] = matrix[i][j]
            elif diagonal_values[key] != matrix[i][j]:
                return False  # Nếu có sự khác biệt, trả về False ngay lập tức
    return True  # Tất cả các đường chéo hợp lệ