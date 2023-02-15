batches = int(input())
single_cookie_in_grams = 25
cup = 140
small_spoon = 10
big_spoon = 20
cookies_per_box = 5
total_boxes_of_cookies = 0


for _ in range(batches):
    qty_flour = int(input())
    qty_sugar = int(input())
    qty_cocoa = int(input())
    if qty_flour <=0 or qty_sugar <= 0 or qty_cocoa <= 0:
        continue
    flour_cups = qty_flour // cup
    sugar_big_spoon = qty_sugar // big_spoon
    cocoa_small_spoon = qty_cocoa // small_spoon
    boxes_cookies_per_bach = (cup + small_spoon + big_spoon)\
                             * min(flour_cups, sugar_big_spoon, cocoa_small_spoon) / single_cookie_in_grams
    made_boxes = 0
    if boxes_cookies_per_bach <= 0:
        print("Ingredients are not enough for a box of cookies.")
    else:
        made_boxes = int(boxes_cookies_per_bach / cookies_per_box)
        print(f"Boxes of cookies: {made_boxes}")
    total_boxes_of_cookies += made_boxes

print(f"Total boxes: {total_boxes_of_cookies}")
