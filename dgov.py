from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

actions = ActionChains(driver)
driver.get("https://dgcs.gos.pk/index.php?#colleges-table")
time.sleep(2)
driver.maximize_window()
region_dropdown = driver.find_element(By.ID,'region')
region_select = Select(region_dropdown)
region_select.select_by_visible_text('KARACHI')
time.sleep(2)

district_dropdown = driver.find_element(By.ID,'district')

district_select = Select(district_dropdown)

district_select.select_by_value('11')

time.sleep(30)


dat = []
for o in range(1,34):
    th =[]
    for i in range(1,10):
        #.........................................table_heads........................................
        xpath = "/html/body/section[5]/div/div[4]/table/thead/tr/th[" + str(i) + "]"
        table_head = driver.find_element(By.XPATH, xpath)
        th.append(table_head.text)
        dat.append(th)
        body = []
        #.........................................table_data........................................
        xpath_td = "/html/body/section[5]/div/div[4]/table/tbody/tr[" + str(o) + "]/td[" + str(i) + "]"
        td = driver.find_element(By.XPATH, xpath_td)
        body.append(td.text)
        dat.append(body)
        
        #...........................................link............................................
    href_lt = []
    href_link_xpath = "/html/body/section[5]/div/div[4]/table/tbody/tr[" + str(o) + "]/td[10]/a"
    href_link = driver.find_element(By.XPATH, href_link_xpath)
    href = href_link.get_attribute("href")
    href_lt.append(href)
    dat.append(href_lt)

df = pd.DataFrame(dat)
print(df)