class Customer:
    def __init__(self, customer_id, salutation, last_name, first_name, email):
        self.customer_id = customer_id
        self.salutation = salutation
        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.purchases = []

    def add_purchase(self, purchase):
        self.purchases.append(purchase)