from datetime import datetime
from urllib.request import urlopen as urlOpen
from Database import Database as db
from Database import Sanitizer as sanitze
from bs4 import BeautifulSoup as soup

# url constants
base_url = "https://www.huizenzoeker.nl/koop/"
province = "noord-brabant"
city = "made"
page = 1

# db.create_database()

try:
    while (True):
        url = base_url + province + "/" + city + "/" + str(page) + "/"
        page = page + 1

        web_soup = soup(urlOpen(url).read(), "html.parser")
        product_html = web_soup.find("table", {"class": "lijst"})

        house_container = product_html.tbody.findAll("tr", {"id": not None})
        for house in house_container:
            house_information = []
            house_information.insert(0, house.find("strong").text)  # straat
            house_information.insert(1, house.findAll("td")[1].contents[2][0:8].strip())  # postcode
            house_information.insert(2, house.findAll("td")[1].contents[2][8:].strip())  # plaats
            house_information.insert(3, house.findAll("td")[2].text)  # bouwjaar
            house_information.insert(4, house.findAll("td")[3].text)  # woon_oppervlakte
            house_information.insert(5, house.findAll("td")[4].text)  # perceel_oppervlakte
            house_information.insert(6, house.findAll("td")[5].text[2:10])  # prijs
            house_information.insert(7, datetime.today().strftime('%Y-%m-%d'))

            house_information = sanitze.sanitize(house_information)
            db.insert(house_information)
except:
    print("End of scraping")
