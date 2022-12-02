# product identifiers list ORDERCODE_YEAR
products = ["T1565_2020", "T2432_2019",
            "T8551_2018", "T3345_2019",
            "Y51372_2019", "Y76715_2017",
            "E98144_2018", "T7733_2020",
            "E7614_2021", "E9722_2017",
            "Y82018_2020", "T61287_2021",
            "E9152_2019", "T7749_2021"]

order_code = input("Give the order code:\n")

# check if order_code is in products[]
for i in products:
    if order_code not in i:
        pass
    else:
        print("Year of the order code:", i[-4:])
        break
