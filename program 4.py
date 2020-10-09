def computepay():
    h = int(raw_input("unesite sate"))
    r = float(raw_input("unesite cijenu po satu"))
    if h > 40:
        return 40*r+ (h-40)*r*1.5
    else:
        return h*r
print ("Pay",computepay())
