def check_alphabetical_order(array):
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            return False
    return True

def main():
    arrays = []

    for i in range(5):
        user_input = input(f"Введите элементы массива {i + 1} (через пробел): ")
        array = user_input.split()
        arrays.append(array)

    found = False

    for index, array in enumerate(arrays):
        if check_alphabetical_order(array):
            print(f"Массив {index + 1} расположен в алфавитном порядке.")
            found = True

    if not found:
        print("Нет массивов с буквами в алфавитном порядке.")

if __name__ == "__main__":
    main()