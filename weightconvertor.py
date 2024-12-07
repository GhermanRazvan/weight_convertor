your_weight = float(input("Enter your weight: "))
choice = input('''
What is the measure you enter you weight in?
Press l for lbs or k for kg
 
 ''')
if choice == "L" or choice == "l":
    converted = your_weight * 0.45
    print(f'Your weight in kg is: {converted} kg')
elif choice == "K" or choice == "k":
    converted = your_weight / 0.45
    print(f'Your weight in lb is: {converted} lbs')


