"""
    Assertion aren't for data validation
    Assertions can be disabled
"""

def delete_product(prod_id, user):
    """Dont use assertion for data validation""""
    assert user.is_admin(), 'You must be admin'
    assert store.has_product(prod_id), 'Unknow product'

    store.get_product(prod_id).delete()


def delete_product_RIGHT(prod_id, user):
    if not user.is_admin():
        raise AuthError('Must be admin to delete')
    if not store.has_product(prod_id):
        raise ValueError('Unknow product id')
    store.get_product(prod_id).delete()