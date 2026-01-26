import pandas as pd

# Read Excel file
data = pd.read_excel("Buku1.xlsx")

# Take first row as sample
row = data.iloc[0]

# Create invoice content
invoice_text = f"""
INVOICE
--------------------------------
No               : {row['No']}
Jenis Barang     : {row['Jenis Barang']}
Quantity         : {row['Quantity']}
Berat Satuan     : {row['Berat Satuan']}
Total Berat Kotor: {row['Total Berat kotor']}
Total Berat Bersih: {row['Total Berat Bersih']}
Harga Satuan USD : {row['Harga Satuan (USD)']}
Total Harga USD  : {row['Total Harga (USD)']}
--------------------------------
Thank you for your business.
"""

# Save invoice as text file
with open("invoice_output.txt", "w") as file:
    file.write(invoice_text)

print("Invoice generated successfully")

    file.write(invoice_text)

print("Invoice generated successfully")
