from entities.customer import Customer
from entities.purchase import Purchase


def process_customer_data(customers, purchases):
    customer_dict = {}
    for _, row in customers.iterrows():
        customer_id = row['customer_id']
        if customer_id not in customer_dict:
            customer_dict[customer_id] = Customer(
                customer_id,
                row['salutation'],
                row['lastname'],
                row['firstname'],
                row['email']
            )

    for _, row in purchases.iterrows():
        purchase = Purchase(
            product_id=row['product_id'],
            price=row['price'],
            currency=row['currency'],
            quantity=row['quantity'],
            purchased_at=row['date']
        )
        customer_dict[row['customer_id']].add_purchase(purchase)
    return [
        {
            "salutation": customer.salutation,
            "last_name": customer.last_name,
            "first_name": customer.first_name,
            "email": customer.email,
            "purchases": [
                {
                    "product_id": str(purchase.product_id),
                    "price": purchase.price,
                    "currency": purchase.currency,
                    "quantity": purchase.quantity,
                    "purchased_at": purchase.purchased_at
                } for purchase in customer.purchases
            ]
        }
        for customer in customer_dict.values()
    ]
