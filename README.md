# In-Flight Payment Integration System
## Project Description
- This project aims to integrate an in-flight payment system for purchasing Duty-Free products and food (snacks, beverages, etc.) during flights. 
Given the potential lack of continuous internet connectivity, customer data and purchases are recorded in flat CSV files. 
These files are then sent to Display’s servers via 4G once the plane has landed. 
The system reads these files, interprets the data, and sends it to the ground processing system’s API.
## Usage
1. Install the required dependencies:
pip install -r requirements.txt
2. Ensure the CSV files are present on the hard drive.
3. Run the CLI to process and send the data:
  python cli.py path/to/customer.csv path/to/purchase.csv
## Clean Architecture
This project follows the principles of Clean Architecture to ensure maintainability, scalability, and testability.