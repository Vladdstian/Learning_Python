# list slicing

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])  # [2:5] slicing the piano_keys list from position 2 to 5
print(piano_keys[2:])  # slicing from pos 2 to the end
print(piano_keys[:5])  # slicing from the beginning to the 5th position
print(piano_keys[1:5:2])  # 2 is the step on which the list is sliced -
# piano_keys will be sliced from pos 1 to 5, and it will return every char each 2 pos
