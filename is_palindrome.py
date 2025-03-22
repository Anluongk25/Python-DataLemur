def is_palindrome(phrase):
    left, right = 0, len(phrase) - 1  # Đặt hai con trỏ ở hai đầu chuỗi

    while left < right:
        # Bỏ qua các ký tự không phải chữ hoặc số ở phía trái
        while left < right and not phrase[left].isalnum():
            left += 1
        # Bỏ qua các ký tự không phải chữ hoặc số ở phía phải
        while left < right and not phrase[right].isalnum():
            right -= 1
        
        # So sánh hai ký tự sau khi chuyển về chữ thường
        if phrase[left].lower() != phrase[right].lower():
            return False

        left += 1
        right -= 1

    return True