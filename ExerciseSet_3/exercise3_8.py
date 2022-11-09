costs = float(input("What is the total cost of the order?\n"))
total_cost = 0
student = False
vip = False
vip_points = 0
shipping_costs = 0
code_sale = 0

# Add the shipment costs (7.95€) on top of the total cost
# If the total cost exceeds 99€, shipment costs are free
if costs <= 99:
    shipping_costs = 7.95
    sales_code = input("Sales code:\n").lower()

if input("Student? (y/n)\n").lower() == "y":
    student = True
else:
    student = False

# if vip, ask for points
if input("VIP? (y/n)\n").lower() == "y":
    vip = True
    vip_points = int(input("Points?\n"))
else:
    vip = False

# code reduces amount of total costs by 10% (100-10 = 90)
if code_sale == "FALL22":
    total_cost = (costs * 0.9)

# elif because either first code or second code
# sales_code reduces amount of total costs by 10% (100-20 = 80)
elif code_sale == "BK2SCHOOL" and student:
    total_cost = (costs * 0.8)

# if vip reduce total cost for each full 1000 vip points but first ask if vip has points
if vip:
    if vip_points > 0:
        use_points = input(f"Do you want to use your VIP Points? (y/n)\n")
        if use_points == "y":
            total_cost -= ((vip_points // 1000) * 5)

# if vip for each 10€ cost give 100 points
if vip:
    vip_points += ((total_cost // 10) * 100)

# add shipping costs to total costs
total_cost += shipping_costs

# f print total costs with shipment:
print(f"Total costs including possible shipment costs: {total_cost}€")
