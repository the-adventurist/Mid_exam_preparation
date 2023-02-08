qty_food = float(input()) * 1000
qty_hay = float(input()) * 1000
qty_cover = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000

insufficient_products = False
for day in range(1, 31):
    qty_food -= 300
    if qty_food <= 0:
        insufficient_products = True
        break
    if day % 2 == 0:
        serving_hay = 0.05 * qty_food
        qty_hay -= serving_hay
        if qty_hay <= 0:
            insufficient_products = True
            break
    if day % 3 == 0:
        serving_cover = 1/3 * guinea_pig_weight
        qty_cover -= serving_cover
        if qty_cover <= 0:
            insufficient_products = True
            break

if insufficient_products:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {qty_food/1000:.2f}, Hay: {qty_hay/1000:.2f},"
          f" Cover: {qty_cover/1000:.2f}.")
