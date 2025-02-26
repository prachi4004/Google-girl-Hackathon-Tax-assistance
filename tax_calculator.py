import re

def calculate_tax(extracted_text):
    salary_match = re.search(r'Salary:\s*\₹?([\d,]+)', extracted_text)
    deductions_match = re.search(r'Deductions:\s*\₹?([\d,]+)', extracted_text)
    tax_deducted_match = re.search(r'Tax Deducted:\s*\₹?([\d,]+)', extracted_text)

    salary = int(salary_match.group(1).replace(',', '')) if salary_match else 0
    deductions = int(deductions_match.group(1).replace(',', '')) if deductions_match else 0
    tax_deducted = int(tax_deducted_match.group(1).replace(',', '')) if tax_deducted_match else 0

    taxable_income = max(0, salary - deductions)
    tax_liability = max(0, taxable_income * 0.1 - tax_deducted)

    return {
        "Salary": salary,
        "Deductions": deductions,
        "Tax Deducted": tax_deducted,
        "Tax Liability": tax_liability
    }
