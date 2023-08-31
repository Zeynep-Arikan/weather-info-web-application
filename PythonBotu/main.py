import asyncio

import aiohttp
from weather_helper import get_weather_data, get_weather
from database_helper import connect_to_database, create_table_if_not_exists, update_weather_data

async def main():
    while True:
        host = 'localhost'
        user = 'root'
        password = 'sevval157'
        database = 'havadurumu'

        connection = connect_to_database(host, user, password, database)
        cursor = connection.cursor()

        cursor.execute('SELECT id, name, plate, latitude, longitude FROM Cities')
        cities = cursor.fetchall()

        create_table_if_not_exists(cursor)
    
        async with aiohttp.ClientSession(headers={'Accept-Encoding': 'gzip'}) as session:
            tasks = [get_weather_data(latitude, longitude) for _, _, _, latitude, longitude in cities]
            get_weather = await asyncio.gather(*tasks)

        for index, city in enumerate(cities):
            _, name, _, _, _ = city
            temperature_box, sky_status, up_down, day_night, current_date, lastupdatetime, sunrise, specific, humidity, windspeeds, night, sunset = get_weather[index]
            print(f'{name}: Tarih={current_date} Guncelleme zamani={lastupdatetime}: Sicaklik={temperature_box}: Gokyuzu={sky_status}: Yuksek/dusuk={up_down}: Ruzgar={windspeeds}km/s: Gunduz={day_night}: Gece={night} Gun dogumu={sunrise}: Gun Batimi={sunset} Basinc={specific}: Nem={humidity}')

        # # Veritabanına verileri ekle
        # #     insert_query =f'''
        # #         INSERT INTO YeniDurum (Name, GuncellemeZamani, Sicaklik, Gokyuzu, YuksekDusuk, Ruzgar, Gunduz,Gece,GunDogumu,GunBatimi, Basinc, Nem)
        # #         VALUES  ('{name}',' {lastupdatetime}', '{temperature_box}', '{sky_status}', '{up_down}', '{windspeeds}', '{day_night}', '{night}', '{sunrise}', '{sunset}', '{specific}', '{humidity}')
        # #         '''
        # #     cursor.execute(insert_query)
    

            update_weather_data(cursor, name, lastupdatetime, temperature_box, sky_status, up_down, windspeeds, day_night, night, sunrise, sunset, specific, humidity)

        
        connection.commit()
        cursor.close()
        connection.close()
        print("calisiyor")
        await asyncio.sleep(300)  # 300 saniye yani 5 dakika bekle

     

if __name__ == '__main__':
    asyncio.run(main())
