from selenium import webdriver
import os
# click button & input
from selenium.webdriver.common.keys import Keys
# selenium wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# headless
from selenium.webdriver.firefox.options import Options


#options = Options()
#options.headless = True

driver = webdriver.Firefox(
        #options=options,
        executable_path=r'C:\Users\MIKA\PycharmProjects\KMB_schedule\geckodriver.exe'
    )
# driver = webdriver.Firefox(options=options, executable_path=os.getcwd()+'//geckodriver')
driver.get("https://search.kmb.hk/KMBWebSite/index.aspx?lang=en")
# print("Headless Firefox Initialized")

# click route research
driver.find_element_by_css_selector('#imgRouteSearchIcon').click()

    # input route no. & click enter
input_route_no = driver.find_element_by_css_selector("input#txtRoute")
input_route_no.send_keys('E36')
input_route_no.send_keys(Keys.ENTER)

    # wait after enter E36
    # try:
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "tdStop7"))
)
    # finally:
    #   driver.quit()

    # click Stop
stop_name = driver.find_elements_by_css_selector("td.stopTd.imgHover span.fontSize13")
# print("how many stops:", len(stop_name))
for i in stop_name:
    j = i.get_attribute("textContent")
        # print(j)
    if j == "YOHO MALL I":
            # print("b")
        i.click()

    # wait after click stop
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "td.fontSize11"))
)
    # print("can wait")
    # find next bus
next_bus_tags = driver.find_elements_by_css_selector("td.fontSize11")
a = []
for count, i in enumerate(next_bus_tags):
    j = i.get_attribute("textContent")
        # print(j)
    a.append(j)
    if j == "Arrival Time":
        pos = count

print(f"YoHo Mall I : {a[pos+1]}")