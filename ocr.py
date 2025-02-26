import pdfplumber
import re

def extract_text_from_pdf(pdf_path):
    """Extracts text from Form 16 PDFs accurately."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # Debugging: Print extracted text to verify contents
    print("\n===== Extracted Text =====\n")
    print(text)  
    print("\n=========================\n")
    
    return text

def extract_financial_details(text):
    """Extracts Salary, Deductions, and Tax Deducted using improved regex."""
    details = {"Salary": 0, "Deductions": 0, "Tax Deducted": 0, "Tax Liability": 0}

    # **Regex to extract values correctly**
    salary_match = re.search(r"Salary\s+as\s+per\s+provisions.*?\s+([\d,]+\.\d+)", text, re.DOTALL | re.IGNORECASE)
    deductions_match = re.search(r"Aggregate\s+of\s+deductible\s+amount.*?\s+([\d,]+\.\d+)", text, re.DOTALL | re.IGNORECASE)
    tax_deducted_matches = re.findall(r"Total\s*\(Rs.\)\s+([\d,]+\.\d+)", text, re.DOTALL | re.IGNORECASE)

    # Assign extracted values to details dictionary
    if salary_match:
        details["Salary"] = float(salary_match.group(1).replace(",", "").strip())

    if deductions_match:
        details["Deductions"] = float(deductions_match.group(1).replace(",", "").strip())

    # Tax Deducted: Select the **smaller** of the extracted values
    if tax_deducted_matches:
        extracted_values = [float(value.replace(",", "").strip()) for value in tax_deducted_matches]
        details["Tax Deducted"] = min(extracted_values)  # Pick the smaller value (₹483,740)

    # **Ensure Tax Deducted is not mistakenly taking Salary**
    if details["Tax Deducted"] > details["Salary"]:  
        details["Tax Deducted"] = 0  # Reset incorrect value  

    # **Fix Tax Liability Calculation**
    taxable_income = max(0, details["Salary"] - details["Deductions"])

    # Apply basic tax calculation (assuming 10% tax rate as an example)
    tax_rate = 0.2 if taxable_income > 1000000 else 0.1  # Higher tax for higher income
    estimated_tax_payable = taxable_income * tax_rate

    # Calculate final tax liability
    details["Tax Liability"] = max(0, estimated_tax_payable - details["Tax Deducted"])

    return details
