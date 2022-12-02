# list with product identifiers:
products = ["PHILIPS_Boiler_HD4646_2020_09_21_C_1",
            "KENWOOD_KitchenMachine_KVL8300S_2015_09_22_C_3",
            "BOSCH_Blender_MMB65G5M_2016_05_07_C_3",
            "WHIRLPOOL_Microwave_MCP345WH_2019_01_15_C_1",
            "ROSENLEW_Freezer_RPP2330_2017_01_29_C_2",
            "ELECTROLUX_Fridge_ERF4114AOW_2017_11_07_C_2"]
# create empty array:
products_done = []

for i in range(len(products)):
    # remember, parts is a LIST of three elements
    # by using split(), it doesn't matter how long
    # different parts are! this works always!
    parts = products[i].split("_")

    # categories of numbers between 1-3 with meanings:
    product_type = parts[-1]
    if product_type == "1":
        product_type = "Small electronics"
        parts.append(product_type)
    elif product_type == "2":
        product_type = "Appliances"
        parts.append(product_type)
    elif product_type == "3":
        product_type = "Blenders"
        parts.append(product_type)

    products_done.append(parts)   # product must be added to the list

for i in products_done:   # access index and print each product in the format
    print(f"Brand: {i[0]}")
    print(f"Name and model: {i[1]} ({i[2]})")
    print(f"Category: {i[8]}")
    print(f"Addition date: {i[3]}.{i[4]}.{i[5]}\n")
