from .models import Product
import pandas as pd

data = pd.read_csv("static/data/Phones_amazon.csv")

for index in data.index:
    phone = Product(name=data['name'][index], brand=data['brand'][index], 
                    bestLink=data['bestLink'][index], price=data['price'][index],
                    image=data['imageLink'][index],
                    description=data['description'][index])
    phone.save()

print("Data saved!!!")