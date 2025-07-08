import requests


API_key = "615400a040f8fb121e3af5c55ca9c223"
def get_data(place, forecats_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecats_days
    filtered_data = filtered_data[:nr_values]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict['weather'][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data(place="Tokyo"))