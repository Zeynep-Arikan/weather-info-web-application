async def get_weather(session,latitude, longitude):
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