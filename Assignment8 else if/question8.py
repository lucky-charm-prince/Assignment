# 8. Weather Monitoring System

# A weather monitoring system classifies the weather condition based on temperature:

# * Below 0°C → Freezing
# * 0°C to 20°C → Cold
# * 21°C to 35°C → Warm
# * Above 35°C → Hot

# Write a Python program to classify the weather.

# Input:
# Enter temperature: 38

# Output:
# Weather Condition: Hot


temperature=int(input("enter the temperature="))
if temperature<0:
    print("freezing")
elif temperature>=0 and temperature<=20:
    print("clod")
elif temperature>=21 and temperature<=35:
    print("warm")
else:
    print("hot")