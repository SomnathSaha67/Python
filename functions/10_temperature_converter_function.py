def convert_temperature(value, from_unit, to_unit):
    if from_unit==to_unit:
        return value
    elif from_unit=="Celsius" and to_unit=="Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit=="Fahrenheit" and to_unit=="Celsius":
        return (value - 32) * 5/9
    elif from_unit=="Celsius" and to_unit=="Kelvin":
        return value + 273.15
    elif from_unit=="Kelvin" and to_unit=="Celsius":
        return value - 273.15                   
    elif from_unit=="Fahrenheit" and to_unit=="Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit=="Kelvin" and to_unit=="Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return "Invalid unit conversion"
temp_value=float(input("Enter temperature value: "))
from_unit=input("Convert from (Celsius, Fahrenheit, Kelvin), C/F/K: ")
to_unit=input("Convert to (Celsius, Fahrenheit, Kelvin), C/F/K: ")
unit_map={"C":"Celsius", "F":"Fahrenheit", "K":"Kelvin"}
from_unit_full=unit_map.get(from_unit.upper())
to_unit_full=unit_map.get(to_unit.upper())
if from_unit_full and to_unit_full:
    converted_value=convert_temperature(temp_value, from_unit_full, to_unit_full)
    print(f"{temp_value} {from_unit_full} is {converted_value} {to_unit_full}.")
else:
    print("Invalid unit input.")