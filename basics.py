def calculate_discount(price, is_member):
    """
    Returns the discounted price.
    Members receive a 10% discount.
    """
    if price < 0:
        raise ValueError ("value cannot be negative")
    if is_member:
        return price - (price*0.10)
    return price