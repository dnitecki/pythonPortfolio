# -*- coding: utf-8 -*-
"""


@author: domin
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select 
import time
driver = webdriver.Chrome('C:\\Users\\domin\\Downloads\\chromedriver') 
driver.get('https://www.foragentsonly.com/login/')
driver.find_element_by_id('user1').send_keys('0212H') 
driver.find_element_by_id('password1').send_keys('Beata20$')
driver.find_element_by_id('image1').click()
select = Select(driver.find_element_by_id('QuoteStateList')) 
select.select_by_visible_text('Illinois')
driver.find_element_by_id('selectProductButton').click()
driver.find_element_by_xpath('//span[text()="Auto"]').click()
driver.find_element_by_xpath('//span[text()="Home (HO3)"]').click()
driver.find_element_by_id('quoteActionSelectButton').click()
time.sleep(3)
print(driver.current_window_handle) #CDwindow-08B49B8E57E3B45BBC03796FA7082116 - parent
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle) #Named Insured FAO Quoting

driver.find_element_by_id('NamedInsured_Embedded_Questions_List_FirstName').send_keys('Dominick')
driver.find_element_by_id('NamedInsured_Embedded_Questions_List_LastName').send_keys('Nitecki')
driver.find_element_by_id('NamedInsured_Embedded_Questions_List_DateOfBirth').send_keys('07051995')
select = Select(driver.find_element_by_id('NamedInsured_Embedded_Questions_List_Gender')) 
select.select_by_visible_text('Male')
driver.find_element_by_id('NamedInsured_Embedded_Questions_List_PrimaryEmailAddress').send_keys('dominick.nitecki95@gmail.com')
driver.find_element_by_id('NamedInsured_PhoneNumbers_List_0_Embedded_Questions_List_PhoneNumber').send_keys('6307650695')
driver.find_element_by_id('NamedInsured_Embedded_Questions_List_MailingAddress').send_keys('1N316 Papworth St')
driver.find_element_by_id('NamedInsured_Embedded_Questions_List_City').send_keys('Carol Stream')
driver.find_element_by_id('NamedInsured_Embedded_Questions_List_ZipCode').send_keys('60188')
select = Select(driver.find_element_by_id('NamedInsured_Embedded_Questions_List_CurrentResidence'))
select.select_by_visible_text('1 year or more') 
select = Select(driver.find_element_by_id('NamedInsured_Embedded_Questions_List_DisclosureProvided'))
select.select_by_visible_text('Yes') 
driver.find_element_by_xpath('//span[text()="PRODUCTS"]').click()
time.sleep(3)
driver.find_element_by_id('ProductsAA_Embedded_Questions_List_PolicyEffectiveDate').send_keys('06202020')
time.sleep(3)
driver.find_element_by_id('ProductsAA_Vehicles_List_0_Embedded_Questions_List_Vin').send_keys('YV1MS382352080306')
