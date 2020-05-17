for i in range(10):
    print("1) loop 1: ", i)

    for j in range(10):
        print("    loop 2: ", j)
        if (j > 5):
            break

    print("2) loop 1: ", i)

