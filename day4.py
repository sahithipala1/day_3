print("\033[38;5;4m")
s = "abc"
print("Uncoloured text: ", s)
colored_s = "\033[38;5;4m" + s
print("Coloured text: ", colored_s)