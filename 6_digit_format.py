while True:
    try:
        nums = int(input("Enter a number between 0-1000: "))
        if nums in range(0, 1001):
            numstr = str(nums) #converts the int to a string to make zfill function work
            break
        else:
            print("Try using numbers from 0 to 1000!")
            continue
    except ValueError:
        print("Try using numbers from 0 to 1000!")

print(numstr.zfill(6))