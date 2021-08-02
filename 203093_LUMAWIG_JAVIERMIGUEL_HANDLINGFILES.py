products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# PROBLEM 1 (function 1: Product Info Lookup)
def get_product (code):
    return (products[code])

# PROBLEM 2 (function 2: Product Property Lookup)
def get_property (code, property):
    return(products[code][property])

# PROBLEM 3 (function 3: POS Terminal)
def main():

    quantity_americano = 0
    quantity_brewedcoffee = 0
    quantity_cappuccino = 0
    quantity_dalgona = 0
    quantity_espresso = 0
    quantity_frappuccino = 0

    resibo = set()
    total = 0
    init_list = []


    while(True):
        place_order = input("Enter customer's order: (product_code),(quantity) ")

        if place_order == "/":
            break
        else:
            init_list.append(place_order.split(","))

            order_quantity = int(place_order.split(',')[1])

            resibo.add(place_order.split(',')[0])

            prod_code = (place_order.split(',')[0])

            #add quantity based on product code
            if prod_code == "americano":
                quantity_americano += order_quantity
            elif prod_code == "brewedcoffee":
                quantity_brewedcoffee += order_quantity
            elif prod_code == "cappuccino":
                quantity_cappuccino += order_quantity
            elif prod_code == "dalgona":
                quantity_dalgona += order_quantity
            elif prod_code == "espresso":
                quantity_espresso += order_quantity
            elif prod_code == "frappuccino":
                quantity_frappuccino += order_quantity

    #tally quantities of each product
    products['americano']['quantity'] = quantity_americano
    products['brewedcoffee']['quantity'] = quantity_brewedcoffee
    products['cappuccino']['quantity'] = quantity_cappuccino
    products['dalgona']['quantity'] = quantity_dalgona
    products['espresso']['quantity'] = quantity_espresso
    products['frappuccino']['quantity'] = quantity_frappuccino

    resibo = sorted(resibo)

    #write receipt

    with open('receipt.txt','w') as receipt_file:
        receipt_file.write('==\n')
        receipt_file.write('CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n')
        for x in resibo:
            receipt_file.write(f"{x}\t\t\t{products[x]['name']}\t\t\t{products[x]['quantity']}\t\t\t {(products[x]['quantity']) * (products[x]['price'])}\n")
            total += products[x]["quantity"] * products[x]["price"]
        receipt_file.write(f'Total:\t\t\t\t\t\t\t\t\t\t{total}\n')
        receipt_file.write('==')

main()
