import pandas as pd

# === CONFIG ===
INPUT_FILE = "Buku1.xlsx"
OUTPUT_TXT = "all_invoices.txt"
OUTPUT_EXCEL = "invoice_output.xlsx"

# === READ EXCEL (REAL-WORLD MESSY FORMAT) ===
df = pd.read_excel(
    INPUT_FILE,
    header=None,
    skiprows=2
)

# Remove empty rows
df = df.dropna(how="all")

# Set column names manually
df.columns = [
    "NO",
    "JENIS BARANG",
    "TOTAL SATUAN",
    "QUANTITY",
    "BERAT SATUAN",
    "TOTAL BERAT KOTOR",
    "TOTAL BERAT BERSIH",
    "HARGA SATUAN USD",
    "TOTAL HARGA USD"
]

# Remove TOTAL / JUMLAH row if exists
df = df[df["NO"].apply(lambda x: str(x).isdigit())]

# === GENERATE TEXT INVOICES ===
all_invoices = []

for _, row in df.iterrows():
    invoice = f"""
INVOICE
--------------------------------
No              : {row['NO']}
Jenis Barang    : {row['JENIS BARANG']}
Quantity        : {row['QUANTITY']}
Berat Satuan    : {row['BERAT SATUAN']}
Total Berat     : {row['TOTAL BERAT KOTOR']}
Harga Satuan    : {row['HARGA SATUAN USD']}
Total Harga USD : {row['TOTAL HARGA USD']}
--------------------------------
"""
    all_invoices.append(invoice)

# Save TXT
with open(OUTPUT_TXT, "w") as f:
    f.write("\n".join(all_invoices))

# Save Excel summary
df.to_excel(OUTPUT_EXCEL, index=False)

print("SUCCESS ✅")
print("Generated:")
print("- all_invoices.txt")
print("- invoice_output.xlsx")
