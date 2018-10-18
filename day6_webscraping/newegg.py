import bs4
from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup

my_url='https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uclient=Req(my_url)
page_html=uclient.read()
uclient.close()

page_soup = soup(page_html, "html.parser")

containers=page_soup.findAll("div",{"class":"item-container"})

filename = "products_newegg.csv"
f = open(filename, "w")

headers = "Brand, Product_name\n"
f.write(headers)


for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text

	print("Brand: " + brand)
	print("Product Name: " + product_name)

	f.write(brand + "," + product_name.replace(",","|") + "\n")

f.close()
