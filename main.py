from fastapi import FastAPI, Request

import uvicorn
import requests
import httpx
from settings import setting

app = FastAPI()


@app.get('/')
def root():
    return {"message": "welcome to my application"}


@app.get('/api/hello')
async def SayHello(request: Request, visitors_name: str = None):
    if not visitors_name:
        return {"message": "Hello Dear, welcome to my application."}
    get_location_url = f'{setting.api_url}?token={setting.token}'
    client_ip = request.client.host
    print(client_ip)
    location = requests.get(get_location_url).json()
    get_temp_url = f'{setting.temp_url}?q={location["city"]}&appid={setting.api_key}'

    async with httpx.AsyncClient() as client:
        response = await client.get(get_temp_url)
        temp_info = response.json()

    temperature = temp_info['main']['temp']

    return {
        "client_ip": client_ip,
        'location': location['city'],
        "message": f"hello {visitors_name} the temperature is {temperature} degrees in {location['city']}",


    }


if __name__ == '__main__':
    uvicorn.run(app="main:app", port=8000, host="0.0.0.0")
