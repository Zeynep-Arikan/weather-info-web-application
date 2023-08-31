import aiohttp
import asyncio
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime

async def get_weather(session, latitude, longitude):
    base_url = 'https://weather.com/tr-TR/weather/today/l/'
    url = base_url + f'{latitude},{longitude}'
    

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            html_content = await response.text()
            return html_content
        else:
            return None


async def get_weather_data(latitude, longitude):
     async with aiohttp.ClientSession() as session:
        html_content = await get_weather(session, latitude, longitude)
        if html_content:
            zeynep = BeautifulSoup(html_content, "html.parser")
            tree = etree.HTML(html_content)

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
        sunset_elements = tree.xpath('/html/body/div[1]/main/div[2]/main/div[4]/section/div/div[1]/div[2]/div/div/div/div[2]/p')
        if sunset_elements:
            sunset = sunset_elements[0].text
        else:
            sunset = "bos"
        


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
   
   
