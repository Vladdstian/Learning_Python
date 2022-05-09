# Today the topic will be around the Control Flow and logical operators in Python
water_level = 50
water = "Cold"
# conditional if / else
if water_level < 70:  # if statement:
    print("Drain Water")  # this is the if block and as any other block should be indented with 4 spaces
    if water == "Hot":  # inside the if statement (inside its block) we can create another if (nested if's) and so on...
        print("water temperature is good!")
    else:
        water = "Hot"
        print("water temperature increased")
elif water_level == 0:  # elif statement
    print("turn on the water")  # elif is another if that describe another situation for the first if
else:  # else doesn't need a statement because it describes all the other possible situations
    print("Continue")  # same indentation with 4 blocks; PS: auto indentation from PyCharm is great

# Comparison operators: > Greater than; < Less than; >= Greater than or equal to; <= Less than or equal to;
# == Equal to; != Not Equal to
