import argparse
from interface_adapters.csv_reader import read_customers, read_purchases
from usecases.process_data import process_customer_data
from interface_adapters.api_sender import send_data_to_api

def main():
    parser = argparse.ArgumentParser(description="Send customer and purchase data to the API.")
    parser.add_argument('customers_file', help="Path to the customers CSV file")
    parser.add_argument('purchases_file', help="Path to the purchases CSV file")
    args = parser.parse_args()
    customers_df = read_customers(args.customers_file)
    purchases_df = read_purchases(args.purchases_file)
    customer_data = process_customer_data(customers_df, purchases_df)
    send_data_to_api(customer_data)

if __name__ == '__main__':
    main()