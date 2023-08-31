import requests as rq


def get_data_from_api(url):
    headers = {
        "accept": "application/json",
        "X-CSRF-TOKEN": ""  # Add your CSRF token here
    }
    
    response = rq.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        datas = response.json()
        countries_data = []  # A list to store country data
        
        for data in datas["data"]:
            code_pays = data["iso"]
            pays = data["name"]
            countries_data.append((code_pays, pays))
        
        return countries_data
    else:
        print("Failed to fetch data")
        return None


if __name__ == '__main__':
    url = "https://covid-api.com/api/regions"
    countries_data = get_data_from_api(url)
    
    if countries_data:
        for code_pays, pays in countries_data:
            print("Country Code:", code_pays)
            print("Country Name:", pays)
