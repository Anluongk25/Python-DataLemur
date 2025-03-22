def number_to_words(n):
    # Danh sách số từ 1-9
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # Danh sách số từ 10-19 (các số đặc biệt)
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
             "sixteen", "seventeen", "eighteen", "nineteen"]
    # Danh sách các bội số của 10 từ 20-90
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    # Xử lý các số từ 1 đến 9
    if 1 <= n < 10:
        return ones[n]
    # Xử lý các số từ 10 đến 19 (các số đặc biệt)
    elif 10 <= n < 20:
        return teens[n - 10]
    # Xử lý các số từ 20 đến 99
    elif 20 <= n < 100:
        return tens[n // 10] + ones[n % 10]  # Lấy phần chục + phần đơn vị

    # Xử lý các số từ 100 đến 999
    elif 100 <= n < 1000:
        remainder = n % 100  # Lấy phần dư sau khi chia cho 100
        if remainder == 0:
            return ones[n // 100] + "hundred"  # Nếu là bội số của 100 (200, 300, ...)
        else:
            return ones[n // 100] + "hundredand" + number_to_words(remainder)  
            # Thêm "hundred and" nếu không phải bội số của 100

    # Xử lý số 1000
    elif n == 1000:
        return "onethousand"

def count_letters(N):
    # Tính tổng số chữ cái của tất cả các số từ 1 đến N
    total_letters = sum(len(number_to_words(i)) for i in range(1, N + 1))
    return total_letters