# AI-Based Intelligent Document Processing (Invoice OCR)

## Objective
Demonstrate OCR, NLP, and Generative AI understanding by extracting structured data from invoice documents.

## Document Type
Invoice

## Tools & Technologies
- Python
- Tesseract OCR
- Regular Expressions
- JSON
- NLP & LLM concepts

## Approach
1. Apply OCR to extract raw text from invoice images
2. Identify key fields using pattern matching and NLP logic
3. Convert extracted information into structured JSON format

## Sample OCR Output
Invoice No: INV-1023  
Date: 12/09/2024  
Vendor: ABC Technologies Pvt Ltd  
Total Amount: ₹18,500  
GST: ₹2,850  
Invoice Amount: ₹21,350  

## Structured Output (JSON)
```json
{
  "document_type": "invoice",
  "invoice_number": "INV-1023",
  "invoice_date": "2024-09-12",
  "vendor_name": "ABC Technologies Pvt Ltd",
  "amount_before_tax": 18500,
  "gst_amount": 2850,
  "total_amount": 21350,
  "currency": "INR"
}
