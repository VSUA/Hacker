import itertools
for main, des, dri in itertools.product(zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks)):
    sum = main[1] + des[1] + dri[1]
    if sum <= 30:
        print(main[0], des[0], dri[0], sum)
