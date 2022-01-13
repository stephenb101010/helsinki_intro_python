# Write your solution here
temp_fahr = int(input("Please type in a temperature (F): "))
temp_cels = ((temp_fahr - 32) * 5) / 9
print(f"{temp_fahr} degrees Fahrenheit equals {temp_cels} degrees Celsius")
if temp_cels < 0:
    print("Brr! It's cold in here!")