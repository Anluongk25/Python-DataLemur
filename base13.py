def to_base_13(num):
    if num == 0:
        return "0"

    digits = "0123456789ABC"
    result = ""
    is_negative = num < 0
    num = abs(num)

    while num > 0:
        remainder = num % 13
        result = digits[remainder] + result
        num //= 13

    return "-" + result if is_negative else result