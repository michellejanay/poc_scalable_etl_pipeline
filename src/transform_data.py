from extract_csv import extract_csv
from datetime import datetime

def remove_ppi(data):
    for item in data:
        item.pop("customer_name", None)
        item.pop("card_num", None)
    return data

def transform_timestamp(data):
    for item in data:
        timestamp = item['Timestamp']
        converted_timestamp = datetime.strptime(timestamp, '%d/%m/%Y %H:%M')
        item['Timestamp'] = converted_timestamp
    return data

def transform_orders(data):
    split_data = []
    result = []
    # splitting orders by comma
    for item in data: 
        split_orders = item['item_purchased'].split(',')
        split_data.append(split_orders)
    # loop through list of split_data lists
    for item in split_data:
        basket = []
    # loop through strings in list
        for product_list in item:
            # split from right at first -
            order_split = product_list.rsplit('-', 1)
            # create dictionary from split list items
            order_dict = {'name': order_split[0].strip(), 'price': float(order_split[1].strip())}
            # add to order list
            basket.append(order_dict)
        # outside loop - add order to result 
        result.append(basket)
    # replace order in data with list index of dict in result
    for index in range(len(data)):
        data[index]['item_purchased'] = result[index]
    return data

def update_order_quantity(data):
    for order in data:
        # create a dictionary to track product quantities for each order
        product_dict = {}
        # iterate through each product in the 'item_purchased' list
        for product in order['item_purchased']:
            # create a unique key for the product based on name and price
            product_key = (product['name'], product['price'])
            # if the product already exists in the dictionary, increment the quantity
            if product_key in product_dict:
                product_dict[product_key]['quantity'] += 1
            else:
                # otherwise, add the product to the dictionary with a quantity of 1
                product_dict[product_key] = {**product, 'quantity': 1}
        # convert the dictionary back into a list of products and update 'item_purchased'
        order['item_purchased'] = list(product_dict.values())
    return data

def get_products_menu(data):
    all_orders = []
    seen = set()
    menu_items = []
    for item in data:
        for product in item['item_purchased']:
            all_orders.append(product)
    for products_dict in all_orders:
        products_tuple = tuple(products_dict.items())
        if products_tuple not in seen:
            seen.add(products_tuple)
            menu_items.append(products_dict)
    return menu_items

def transform_data(data):
    data = remove_ppi(data)
    data = transform_timestamp(data)
    data = transform_orders(data)
    data = update_order_quantity(data)
    return data
