def get_cart(session):
    return session.get("cart")


def get_cart_items(cart):
    return cart["items"]
