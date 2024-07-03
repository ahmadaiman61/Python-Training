import os
import subprocess
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://bms.pekab40.com.my/site/login")

username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "LoginForm[user_name]")))
username.send_keys("HIJRAAPROJECT3")

password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "LoginForm[password]")))
password.send_keys("pEKAHIJRAA2024")

login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "login-button")))
login.click()

search_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "fa.fa-search.fa-fw")))
search_icon.click()

ic_numbers = ["720720115611", "661016115127", "730323086051", "781110065089", "781225115357"]
result_dict = {}

for ic in ic_numbers:
        ic_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "membersearch-search_value")))
        ic_input.clear()
        ic_input.send_keys(ic)

        search_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-sm.btn-primary")))
        search_button.click()

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-bordered table-hover']//tbody//tr")))
        row = driver.find_element(By.XPATH, "//table[@class='table table-bordered table-hover']//tbody//tr")

        entitlement_balance = row.find_element(By.XPATH, "./td[6]").text.strip()

        details_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='View']")))
        details_button.click()

        name_element = driver.find_element(By.XPATH, "//th[contains(text(), 'Name')]/following-sibling::td/div[@class='kv-attribute']")
        name = name_element.text

        phonenumber_element = driver.find_element(By.XPATH, "//th[contains(text(), 'Mobile phone number 1')]/following-sibling::td/div[@class='kv-attribute']")
        phonenumber = phonenumber_element.text

        result_dict[ic] = {
            'IC Number': ic,
            'Entitlement Balance': entitlement_balance,
            'Name': name,
            'Phone Number': phonenumber
        }

        search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "fa.fa-search.fa-fw")))
        search.click()

df = pd.DataFrame(result_dict.values())

excel_file = "result.xlsx"
df.to_excel(excel_file, index=False)

print("Data exported to", excel_file)

# Open the Excel file
try:
    if os.name == 'nt':  # For Windows
        os.startfile(excel_file)
    elif os.name == 'posix':  # For macOS
        subprocess.call(['open', excel_file])
    else:  # For Linux
        subprocess.call(['xdg-open', excel_file])
except Exception as e:
    print("Error opening Excel file:", e)

# Auto-adjust column widths using openpyxl
wb = load_workbook(excel_file)
ws = wb.active
for column in ws.columns:
    max_length = 0
    column_letter = column[0].column_letter
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2) * 1.2  # Adjusted width based on content length
    ws.column_dimensions[column_letter].width = adjusted_width
wb.save(excel_file)

driver.quit()
