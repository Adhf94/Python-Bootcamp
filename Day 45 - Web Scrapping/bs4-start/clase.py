from bs4 import BeautifulSoup
import lxml
#sometimes the html parser doesnt work, so you will have to install the lxml module, and pass it as a string as parser
#to the beautifullsoup class
#Se agregó el parametro de encoding para poder leer el html
with open("website.html", encoding="utf-8") as content:
    data = content.read()

soup = BeautifulSoup(data, "html.parser")
#We can get hold of the tags, and strings inside tags

#HMTL TAG
print(soup.title)
#nombre del tag
print(soup.title.name)
#String del TAG html
print(soup.title.string)

#Si se quiere buscar TODOS los elementos de un TAG, se usa el metodo find_all
print(soup.find_all("li"))

#Si se quiere el html indentado, se usa el metodo pretify.
#print(soup.prettify())

#Si se quiere conseguir los atributos de un tag en especifico se usa el metodo GET

all_anchor_tags = soup.find_all("a")
for tag in all_anchor_tags:
    print(tag.get("href"))
#Cuando hay muchas tags de un elemento, se requiere buscar por sus atributos.
#Ejemplo, classes o ID, Se usa el metodo find.
heading = soup.find(name="h1", id="name")
#para saber el nombre del tag = heading.name
#para saber el texto (sin string) heading.getText()
#para saber el valor de un atributo, heading.get("class")
print(heading)

#Cuando se busca algo muy en especifico, como por ejemplo un tag dentro de varias tags, se puede usar el metodo select_one
#Este metodo usa como parametros, el selector de CSS.
#Tambien puede usar selectores de HTML

#usando CSS selectors
company_url = soup.select_one(selector="p a", )
print(company_url)
#Usando ID hmtl selectors
name = soup.select_one(selector="#name")
print(name)
#Usando Class html selectors
heading_class = soup.select(".heading")
#el metodo select, guarda los valores en una lista
print(heading_class)