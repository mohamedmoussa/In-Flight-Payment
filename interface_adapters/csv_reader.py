import pandas as pd

def read_customers(customers_file):
    customers_df = pd.read_csv(customers_file, delimiter=';')
    title_mapping = {1: "Female", 2: "Male"}
    customers_df['salutation'] = customers_df['title'].map(title_mapping)
    return customers_df[['customer_id', 'salutation', 'lastname', 'firstname', 'email']]

def read_purchases(purchases_file):
    return pd.read_csv(purchases_file, delimiter=';')