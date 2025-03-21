while True:
    try:
        nums = int(input("Enter a number between 0-1000: "))
        if nums in range(0, 1001):
            break
        else:
            print("Try using numbers from 0 to 1000!")
            continue
    except ValueError:
        print("Try using numbers from 0 to 1000!")

print (nums)