import pytesseract
from PIL import Image
import re
import json

def extract_invoice_data(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)

    data = {}

    data["invoice_number"] = re.search(r"Invoice No:\s*(\S+)", text).group(1)
    data["invoice_date"] = re.search(r"Date:\s*(\S+)", text).group(1)
    data["vendor_name"] = re.search(r"Vendor:\s*(.*)", text).group(1)
    data["total_amount"] = re.search(r"Invoice Amount:\s*₹(\S+)", text).group(1)

    return json.dumps(data, indent=4)

print(extract_invoice_data("invoice.jpg"))
