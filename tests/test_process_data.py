import pandas as pd
from usecases.process_data import process_customer_data


def test_process_customer_data():
    customers = pd.DataFrame({
        'customer_id': [1],
        'salutation': ['Male'],
        'lastname': ['Moussa'],
        'firstname': ['Mohamed'],
        'email': ['moussa.mohamed@exemple.com']
    })

    purchases = pd.DataFrame({
        'customer_id': [1],
        'product_id': ['4321'],
        'price': [10],
        'currency': ['USD'],
        'quantity': [1],
        'date': ['2023-09-01']
    })

    result = process_customer_data(customers, purchases)

    assert len(result) == 1
    customer = result[0]

    assert customer['salutation'] == 'Male'
    assert customer['last_name'] == 'Moussa'
    assert customer['first_name'] == 'Mohamed'
    assert customer['email'] == 'moussa.mohamed@exemple.com'
    assert len(customer['purchases']) == 1
    purchase = customer['purchases'][0]
    assert purchase['product_id'] == '4321'
    assert purchase['price'] == 10
    assert purchase['currency'] == 'USD'
    assert purchase['purchased_at'] == '2023-09-01'
