from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfD3DaZZV40IilKxFz1-UhuK45zRzw4RZPlcL7AIlCUfbGWNQ/viewform?usp=sf_link"
SPAREROOM = "https://www.spareroom.co.uk/flatshare/?search_id=1066887200&"

response = requests.get(SPAREROOM)
spareroom_webpage = response.text
soup = BeautifulSoup(spareroom_webpage, "html.parser")
listings = soup.find_all(name="article", class_="panel-listing-result")
addresses = []
prices = []
links = []

for listing in listings:
    address = listing.find(name="span", class_="listingLocation").text
    addresses.append(address)
    price = listing.find(name="strong", class_="listingPrice").text
    prices.append(price)
    link = listing.find("a", href=True)["href"]
    links.append(link)

print(addresses)
print(prices)
print(links)

number_of_listings = len(prices)

chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#new_form_button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a")

for i in range(0,number_of_listings):
    driver.get(FORM_URL)

    address_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    time.sleep(2)
    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])
    submit_button.click()
    time.sleep(2)
