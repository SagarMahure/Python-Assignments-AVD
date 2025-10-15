m =int(input("Enter Minutes"))

hours = m//60                # Used Integer Division
remaining_min = m % 60

print(f"The total time after conversion is {hours} hour and {remaining_min} minutes")