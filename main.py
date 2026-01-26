import pandas as pd

# Read Excel file
data = pd.read_excel("Buku1.xlsx")

# Take first row as sample invoice
invoice = data.iloc[0]

# Create invoice content
invoice_text = f"""
INVOICE
------------------------
Invoice No : {invoice['InvoiceNo']}
Customer   : {invoice['Customer']}
Product    : {invoice['Product']}
Quantity   : {invoice['Quantity']}
Price      : {invoice['Price']}
Total      : {invoice['Quantity'] * invoice['Price']}
------------------------
Thank you for your business.
"""

# Save invoice as text file
with open("invoice_output.txt", "w") as file:
    file.write(invoice_text)

print("Invoice generated successfully")
