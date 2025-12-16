def get_integers_from_stdin():
    list = []
    while True:
        try:
            num = int(input("Enter an integer: \n"))
            list.append(num)
        except KeyboardInterrupt:
            print("Input interrupted.")
            break
    return list