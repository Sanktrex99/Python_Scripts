# get all information from wikipedia of any language
import wikipedia
import time

#Taking user input
key=input("Enter your Search Keyword")
lng=input("Enter the language code in which the information you want to see")
wikipedia.set_lang("lng")
#Displays information of article

print(wikipedia.summary(key,sentences=5))
time.sleep(10)
print(wikipedia.search(key))

time.sleep(3)
art=input("Select the specific Title to be shown")

pg=wikipedia.page(key)
print("Do you want to see images in the article? /n It may take additional data")
ans=input("type Y for yes and N for no!!")
if ans=='Y':
    print(pg.content)
    print(pg.images[0])
else:
    print(pg.content)
