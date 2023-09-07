def obhavo(city):
    import requests
    import json

    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "28e4eef4d2mshe43bd705a73de23p1a673cjsne2e4f1b61a97",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data=json.loads(response.text)

    harorat=(data['current_observation']['condition']['temperature']-32)*5/9
    shahar=data['location']['city']
    davlat=data['location']['country']
    kun_botishi=data['current_observation']['astronomy']['sunset']
    kun_chiqishi = data['current_observation']['astronomy']['sunrise']
    result=f"🏢<b> Davlat: {davlat} 🇺🇿</b>\n\n" \
           f"🕌 <b>Viloyat:{shahar}  🕍</b>\n\n" \
           f"🌡<b> Temperatura : {'{:.2f}'.format(harorat)} 🌡</b>\n\n"\
           f"🌖<b> Quyosh chiqish vaqti :{kun_chiqishi}  🌅</b>\n\n" \
           f"🌒<b> Quyosh botish vaqti :{kun_botishi}  🎆</b>\n\n"
    return result

#russian

def погода(city):
    import requests
    import json

    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "28e4eef4d2mshe43bd705a73de23p1a673cjsne2e4f1b61a97",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data=json.loads(response.text)

    температура=(data['current_observation']['condition']['temperature']-32)*5/9
    регион=data['location']['city']
    Статут=data['location']['country']
    kun_botishi=data['current_observation']['astronomy']['sunset']
    kun_chiqishi = data['current_observation']['astronomy']['sunrise']
    result_ru=f"🏢<b> Статут: {Статут} 🇺🇿</b>\n\n" \
           f"🕌 <b>регион:{регион}  🕍</b>\n\n" \
           f"🌡<b> Temperatura : {'{:.2f}'.format(температура)} 🌡</b>\n\n"\
           f"🌖<b> время солнца :{kun_chiqishi}  🌅</b>\n\n" \
           f"🌒<b> время заката :{kun_botishi}  🎆</b>\n\n"
    return result_ru




#english
def weather(city):
    import requests
    import json

    url = "https://yahoo-weather5.p.rapidapi.com/weather"

    querystring = {"location": city, "format": "json", "u": "f"}

    headers = {
        "X-RapidAPI-Key": "28e4eef4d2mshe43bd705a73de23p1a673cjsne2e4f1b61a97",
        "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data=json.loads(response.text)

    Temperatura=(data['current_observation']['condition']['temperature']-32)*5/9
    Region=data['location']['city']
    state=data['location']['country']
    Sunset=data['current_observation']['astronomy']['sunset']
    Sunting = data['current_observation']['astronomy']['sunrise']
    result_en=f"🏢 State: {state} 🇺🇿\n\n" \
           f"🕌 Region:{Region}  🕍\n\n" \
           f"🌡 Temperatura : {'{:.2f}'.format(Temperatura)} 🌡</b>\n\n"\
           f"🌖 Sunting time :{Sunting}  🌅\n\n" \
           f"🌒  Sunset time:{Sunset}  🎆\n\n"
    return result_en

