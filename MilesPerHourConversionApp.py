conv_const = 0.44704
print('Welcome to the MPH to MPS Conversion App',end="\n")
while True:
    try:
        mph = float(input("What is your speed in miles per hour: "))
        mps = round(mph * conv_const,2)
    except:
        print("You must enter a number.")
        continue
    else:
        break

print(f"Your speed in meters per second is {mps}")
