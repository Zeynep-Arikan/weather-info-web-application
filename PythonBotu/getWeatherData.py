import datetime
import aiohttp
from bs4 import BeautifulSoup
import requests
from lxml import etree

from getWeather import get_weather


async def get_weather_data(latitude, longitude):
     async with aiohttp.ClientSession() as session:
        html_content = await get_weather(session, latitude, longitude)
        if html_content:
            zeynep = BeautifulSoup(html_content, "html.parser")
            tree = etree.HTML(html_content)
            
            
    


        # # Parse the HTML content
        # html_content = response.text
        # tree = etree.HTML(html_content)

        # zeynep = BeautifulSoup(response.text,"html.parser")
       
        # Hava sıcaklığını al
        temparature_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/span/text()')

        if temparature_elements:
            temperature_box = temparature_elements[0]
        else:
            temperature_box = "Null"  
    
        temperature_box = tree.xpath('/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/span/text()')[0]
        #Gokyuzu durumu
        sky_status =zeynep.find('div', class_="CurrentConditions--phraseValue--mZC_p").text
        #yuksek/dusuk oranı
        up_down = tree.xpath('/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/div[2]/span[1]/text()')[0]
        #ruzgar 
        windspeed_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[4]/section/div/div[2]/div[2]/div[2]/span/span[2]')

        if windspeed_elements and windspeed_elements[0].text:
            windspeeds = windspeed_elements[0].text
        else:
            windspeeds = "Null" 

        #gunduz
        day_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/div[2]/span[1]/text()')
        if day_elements:
            day_night= day_elements[0]
        else:
            day_night = "Null" 
        
        #gece 
        night_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]/div[2]/span[2]/text()')
        if night_elements:
            night = night_elements[0]
        else:
            night = "Null"
        
        #tarih çek
        current_date = datetime.now().strftime('%Y-%m-%d')
        #guncellenme zamanı
        lastupdatetime = zeynep.find('span',class_="CurrentConditions--timestamp--1ybTk").text
        #gun doğumu 

        # sunrise =zeynep.find('p', class_="TwcSunChart--dateValue--2WK2q").text
        sunrise = zeynep.find('p',class_="TwcSunChart--dateValue--2WK2q").text
        
        
        #gun batimi
       
       
        sunset_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[6]/section/div/div[1]/div[2]/div/div/div/div[2]/svg')
        if sunset_elements:
            sunset= sunset_elements
        else:
            sunset = "Null" 

        # if sunset_elements and sunset_elements[0].text:
        #         sunset = sunset_elements[0].text
        # else:
        #         sunset= "Yazmiyor"

        #     # Diğer işlemler buraya eklenebilir
            
        
    
        

        
        # sunset_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[6]/section/div/div[1]/div[2]/div/div/div/div[2]/p')
        # if sunset_elements and sunset_elements[0].text:
        #     sunset = sunset_elements[0].text
        # else:
        #     sunset = "Null"

    

        # basinç
        specific_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[4]/section/div/div[2]/div[5]/div[2]/span/text()')

        if specific_elements:
            specific = specific_elements[0]
        else:
            specific = "Null"  


         #nem 
        humidity_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[4]/section/div/div[2]/div[3]/div[2]/span')

        if humidity_elements and humidity_elements[0].text:
            humidity = humidity_elements[0].text
        else:
            humidity = "Null" 
        


        return temperature_box, sky_status, up_down,day_night,current_date,lastupdatetime,sunrise,specific,humidity,windspeeds,night,sunset
   
   