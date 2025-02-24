
f_temps = [32, 50, 77, 104, 212]


c_temps = [(f - 32) * 5/9 for f in f_temps]

# Step 3: Print the results
print("Temperatures in Fahrenheit:", f_temps)
print("Temperatures in Celsius:", c_temps)
