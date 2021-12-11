prefix = "92313"
middle_range = 5
suffix = "89"

def consecutive(digits, character):
    rang = ""
    for zero in range(digits):
        rang += character
    return rang

filename = prefix + consecutive(middle_range,"x") + suffix + ".txt"
open(filename, "w").write('') # emptify file if exists
with open(filename, "a") as file:
    for mid_num in range(int(consecutive(middle_range, "9"))):
        digits = middle_range - len(str(mid_num))
        number = prefix + str(mid_num) + suffix
        if digits > 0:
            number = prefix + consecutive(digits, "0") + str(mid_num) + suffix
        print(number)
        file.write(number+"\n")
