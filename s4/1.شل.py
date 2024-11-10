w_earth = 80
conversion_factor = 0.165
for year in range(1,16):
    w_earth+=1
    w_moon = w_earth * conversion_factor
    print(f"year{year}:weight on the moon = {w_moon}kiloogram")
