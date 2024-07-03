# import pandas as pd

# export = pd.read_excel('testlist.xlsx', header=None)
# mylist = ['{}'.format(item) for item in export.iloc[:, 0]]
# print(mylist)

import os
import subprocess
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import load_workbook
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, WebDriverException

def scrape_data():
    try:
        driver = webdriver.Chrome()
        driver.get("https://bms.pekab40.com.my/site/login")

        username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "LoginForm[user_name]")))
        username.send_keys("HIJRAAPROJECT3")

        password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "LoginForm[password]")))
        password.send_keys("pEKAHIJRAA2024")

        login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "login-button")))
        login.click()

        search_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "fa.fa-search.fa-fw")))
        search_icon.click()

        ic_numbers = [
    '500423115338', '501126115053', '510105115251', '510311115041', '510324115059', '510411115081', '510517115186', '510529115079', '510610115068', '510620115088',
    '510811115013', '510912115127', '511105065201', '511212115016', '520228115162', '520305115036', '520308115138', '520409115145', '520527115293', '520627115143',
    '521031065135', '521106115353', '530103115010', '530126115267', '530128115009', '530218115125', '530326115026', '530403115020', '530608115104', '530613115221',
    '530814065152', '531205115307', '531208065106', '540106115162', '540106115234', '540112115353', '540306115204', '540310115119', '540721115121', '540725115508',
    '540827115066', '550128115357', '550301115263', '550420115039', '550525115078', '550703115127', '550706115165', '550714115093', '550716115126', '550818115004',
    '550822115349', '550911115172', '550915115161', '550922065297', '551130115035', '551202115107', '551230115286', '560207035020', '560217115091', '560311016495',
    '560506085079', '560603115487', '560605115210', '560802115084', '560920115325', '560922115038', '561012065494', '570327115147', '570520115464', '570526115019',
    '570604115226', '570611115099', '570709115273', '570716115271', '570804115108', '570810115235', '571005115173', '571029115135', '571113035656', '571115115035',
    '571122115009', '571224115042', '580127115221', '580205115391', '580214115238', '580323115296', '580504115025', '580527115191', '580607115175', '580718115047',
    '580725115336', '580811115113', '590120115316', '590122065009', '590207115036', '590522115220', '590619115091', '590701115402', '590713115258', '590723115366',
    '590726085967', '590920115197', '591108055183', '600107115131', '600119115286', '600322115396', '600328115135', '600422115158', '600504115397', '600510115422',
    '600512115194', '600520115047', '600613115230', '600621115177', '600722115133', '600727115159', '600729115187', '600819115383', '600910115050', '600913115267',
    '600926085247', '601020035053', '601203115275', '610125016267', '610202115235', '610526115493', '610614115071', '610624115091', '610710115223', '610828115181',
    '611110115144', '611216025614', '620129115181', '620203115041', '620321115149', '620325115031', '620326115404', '620413115453', '620501115023', '620518115177',
    '620802106681', '620809115214', '620831115261', '620916015649', '621009115202', '621120115104', '621215115035', '630331115053', '630402115377', '630516115199',
    '630602115363', '630802715611', '630810105215', '630914115194', '631018115035', '631022115177', '631121115164', '631219115146', '631226115339', '640102115753',
    '640113115265', '640206115328', '640220115391', '640225115008', '640226106912', '640323115298', '640325115080', '640501115793', '640614115482', '640705115082',
    '640806115145', '640810115105', '640920115034', '641029115259', '641029115267', '650102115912', '650104115940', '650119065528', '650121115176', '650126115239',
    '650131115081', '650611115224', '650620115007', '650625115057', '650903115234', '650917115243', '660102115057', '660102116711', '660121115159', '660219115181',
    '660301715047', '660325115169', '660330115059', '660330115163', '660401115233', '660602115088', '660616115070', '660719115284', '660822115012', '660823065096',
    '660906115001', '660906115247', '661104115100', '661105115137', '661215115082', '670105115684', '670209115435', '670219115252', '670226115023', '670405115491',
    '670602115052', '670730115188', '670730115292', '670901016038', '671001065461', '671028115019', '671106115007', '671112115003', '671220065111', '680101115248',
    '680101117075', '680130115140', '680206115359', '680311115297', '680317115300', '680329115017', '680422115097', '680428115098', '680515035184', '680601115113',
    '680615105311', '680705115476', '680709115465', '680719065510', '680720115343', '680813115334', '680820115455', '681013115023', '690109115671', '690301115137',
    '690401115230', '690413035983', '690415115223', '690531115298', '690607115287', '690617115221', '690701115056', '690715115225', '690810115565', '691019115111',
    '700101115163', '700108115107', '700109115088', '700116035588', '700126035549', '700214115143', '700218115044', '700318115084', '700402115028', '700408115336',
    '700417115100', '700607115291', '700613115263', '700614115441', '700615115056', '700713115375', '700731115176', '700808115175', '700821115073', '701003115308',
    '701007115049', '701022115071', '710106035559', '710209065240', '710211035163', '710308115063', '710507115015', '710526115387', '710630065025', '710702035379',
    '710811115327', '710813115427', '710926115247', '711015115099', '711016115349', '711215115018', '720102115091', '720106115865', '720207115434', '720305115104',
    '720318115445', '720401115278', '720419065627', '720423115287', '720516115163', '720516115454', '720621035149', '720710115423', '720715115019', '720725115389',
    '720818115513', '721022115117', '730103116079', '730103116458', '730110115533', '730120115350', '730212115059', '730218115471', '730304115419', '730309115119',
    '730410115025', '730420115029', '730425035845', '730501115805', '730507115451', '730609115196', '730621115121', '730727115306', '730829115315', '731010115186',
    '731029115098', '731115115297', '731211115174', '731228115082', '740101116939', '740103115833', '740131065183', '740202115265', '740203115128', '740219115368',
    '740311115432', '740401115276', '740408115092', '740425115035', '740603016575', '740622115165', '740625115443', '740629115299', '740629115432', '740705115291',
    '740714115509', '740810115103', '740811115105', '740811115439', '740819115097', '740821115264', '740823115161', '740901136209', '740920115008', '740920115147',
    '740925065265', '741003115259', '741031115168', '741104115063', '741108115159', '741209115166', '750103115330', '750124115081', '750214115317', '750221115200',
    '750310045259', '750322115154', '750322115453', '750430115434', '750503115241', '750505115173', '750610115001', '750624115096', '750802145205', '750831035208',
    '750911115275', '750922115043', '751027115084', '751107035615', '751128065100', '751215115081', '760216035897', '760304125059', '760427115221', '760501065649',
    '760519115210', '760526055084', '760630115243', '760721035679', '761110115551', '761221055299', '770101117445', '770109115751', '770110115003', '770111065503',
    '770121115471', '770301065651', '770320115394', '770329115454', '770407115119', '770411115381', '770519115201', '770629115165', '770713115096', '770729115445',
    '770815115505', '771015115253', '771022115219', '771217115569', '780102117913', '780110115918', '780111115936', '780210115579', '780327115505', '780411115233',
    '780412115665', '780422115183', '780509115290', '780611115131', '780614115209', '780701115661', '780829115169', '781014115541', '781015035607', '781017065463',
    '781029115288', '781103115113', '781109115173', '781125115181', '781127115193', '781201115205', '781223115142', '781227115166', '781227115342', '790102116215',
    '790108115416', '790112115259', '790122016297', '790209115183', '790302065053', '790310115559', '790326115473', '790407115205', '790517115230', '790610115331',
    '790612115271', '790921115478', '791006025887', '791013115039', '791024115261', '791103115315', '791214115393', '791219115149', '800211115269', '800403115255',
    '800414115365', '800415115391', '800508115374', '800511115535', '800601115547', '800626115420', '800704015338', '800706115439', '800724115213', '800827115443',
    '800903115227', '800920115114', '801031115055', '801110115635', '801116115695', '801126105079', '801208115270', '801209045403', '801210115288', '810121115635',
    '810316115109', '810321065070', '810429115113', '810515115435', '810821115230', '810829115366', '810830125019', '811002115055', '811207115542', '820112115739',
    '820129115639', '820204115437', '820504115252', '820601115174', '820625115136', '820712115265', '820718115039', '820821115096', '820924065108', '821009115137',
    '821025115735', '821119115445', '830223115319', '830523115337', '830612115144', '830722115217', '831018115453', '831025065685', '831124035414', '831206115039'
]

        
        result_dict = {}
        counter = 0

        for ic in ic_numbers:
            try:
                ic_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "membersearch-search_value")))
                ic_input.clear()
                ic_input.send_keys(ic)
                counter += 1
                print(f"Running for the {counter} times and current ic number is {ic}")
            except NoSuchElementException:
                print(f"Cannot enter search for IC number {ic}. Skipping to the next one.")
                continue

            retry_count = 3
            while retry_count > 0:
                try:
                    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-sm.btn-primary")))
                    search_button.click()
                    break  # Break out of the retry loop if successful
                except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
                    if isinstance(e, StaleElementReferenceException):
                        print("StaleElementReferenceException occurred. Retrying...")
                    elif isinstance(e, NoSuchElementException):
                        print("NoSuchElementException occurred. Retrying...")
                    elif isinstance(e, TimeoutException):
                        print("TimeoutException occurred. Retrying...")
                    retry_count -= 1

            if retry_count == 0:
                print("Failed to click the search button after retrying. Skipping to the next IC number.")
                continue

            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-bordered table-hover']//tbody//tr")))
                row = driver.find_element(By.XPATH, "//table[@class='table table-bordered table-hover']//tbody//tr")

                entitlement_balance = row.find_element(By.XPATH, "./td[6]").text.strip()

                details_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='View']")))
                details_button.click()
            except (NoSuchElementException, TimeoutException):
                print(f"No data found for IC number {ic}. Skipping to the next one.")
                continue

            try:
                name_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//th[contains(text(), 'Name')]/following-sibling::td/div[@class='kv-attribute']")))
                name = name_element.text

                phonenumber_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//th[contains(text(), 'Mobile phone number 1')]/following-sibling::td/div[@class='kv-attribute']")))
                phonenumber = phonenumber_element.text

                result_dict[ic] = {
                    'IC Number': ic,
                    'Entitlement Balance': entitlement_balance,
                    'Name': name,
                    'Phone Number': phonenumber
                }

                search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "fa.fa-search.fa-fw")))
                search.click()

            except TimeoutException:
                print(f"Element not found for IC number {ic}. Skipping to the next one.")
                search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "fa.fa-search.fa-fw")))
                search.click()
                continue

        return result_dict

    except WebDriverException as e:
        print("An error occurred with the WebDriver:", e)
        return None

    except Exception as e:
        print("An unexpected error occurred during scraping:", e)
        return None

    finally:
        try:
            driver.quit()
        except:
            pass

def export_to_excel(data):
    if data:
        try:
            df = pd.DataFrame(data.values())
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

        except Exception as e:
            print("An error occurred during exporting to Excel:", e)
    else:
        print("No data to export.")

# Main scraping and exporting process
scraped_data = scrape_data()
export_to_excel(scraped_data)

