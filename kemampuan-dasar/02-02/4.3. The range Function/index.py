for i in range(5):
    print(i)

    list(range(5, 10))

    
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

    for num in range(2, 10):
        if num % 2 == 0:
            print("Found an even number", num)
            continue
            print("Found an odd number", num)
            