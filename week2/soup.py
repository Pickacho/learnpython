SOUP_SIZES = ['Small', 'Medium', 'Large']
SOUP_TYPES = ['Tomato', 'Chiken', 'Pea', 'Corn']


def is_legal_soup_size(soup_size):
    if soup_size in SOUP_SIZES:
        return True
    else:
        return False


def is_legal_soup_types(soup_types):
    if soup_types in SOUP_TYPES:
        return True
    else:
        return False


def is_order_legal(given_soup_type, given_soup_size):
    if is_legal_soup_types(given_soup_type) and is_legal_soup_size(given_soup_size):
        return True
    else:
        return False


def get_order():
    customer_order = input("order know!")
    customer_order_splited = customer_order.split(" ")
    customer_soup_size = customer_order_splited[0]
    customer_soup_type = customer_order_splited[1]
    legal_order = is_order_legal(customer_soup_size, customer_soup_size)
    if legal_order:
        print("Thank you")
    else:
        print("No! Bad Customer!")
    return legal_order


def manage_order_procces():
    is_first_order_successful = get_order()
    if is_first_order_successful:
        return
    is_first_order_successful = get_order()
    if is_first_order_successful:
        return
    is_first_order_successful = get_order()
    if is_first_order_successful:
        return
    print("Go Away!m come back - one year!")
