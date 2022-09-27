
from functools import total_ordering
from itertools import product
from ajio import getAjio
from flipkart import getFlipkart
from meesho import getMeesho
from myntra import getMynta
from snapdeal import getSnapdeal
from amazon import getAmazon
import json

def final_data(keyword,page):
    total =[]


    #amazon=getAmazon(keyword)
    #total.append(json.loads(json.dumps(amazon)))

    
    flipkart=getFlipkart(keyword)
    myntra= getMynta(keyword,page)
    ajio = getAjio(keyword)

    
    total.append(json.loads(json.dumps(flipkart)))
    
    #meesho=getMeesho(keyword)
   
    total.append(json.loads(json.dumps(myntra)))
    #snapdael=getSnapdeal(keyword)
    
    total.append(json.loads(json.dumps(ajio)))
    
    #total.append(json.loads(json.dumps(meesho)))
    
    #total.append(json.loads(json.dumps(snapdael)))
    
    products=[]
    for i in total:
        for x in i['products']:
            products.append(x)


    return {'products':products}
    
