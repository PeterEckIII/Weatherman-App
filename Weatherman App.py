import requests
from bs4 import BeautifulSoup


def get_zipcode() -> int:
    """Retrieve a zipcode (5 character integer) from user input"""

    while True:
        zipcode = input("Please enter your five-digit zipcode to find the forecast in your area: ")

        try:
            int(zipcode)

            if len(zipcode) == 5:
                break  # We've got a zipcode!
            else:
                print("That's not exactly 5 characters in length!\n")
        except:
            print("That's not a number!\n")

    return int(zipcode)


def get_weather_data(zip_code):
    """Return the soup object to find HTML elements"""

    query = 'search?q='
    zip_code = get_zipcode()
    weather_statement = '+weather'
    url = 'https://bing.com/' + query + str(zip_code) + weather_statement
    r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_location_and_date(soup):
    """Process the soup object and return location and date of search"""
    
    soup = get_weather_data(zip_code=get_zipcode())

    location = soup.find("div", {"class": "wtr_locTitle wtr_nowrap wtr_ellipses"})

    date_requested = soup.find("div", {"class": "b_meta"})

    return location, date_requested


def get_current(soup):
    """Process the soup object and return current conditions, temperature, precipitation, wind speed, and humidity"""

    soup = get_weather_data(zip_code=get_zipcode())

    current_conditions = soup.find("div", {"class": "wtr_caption"})

    temperature = soup.find("div", {"class": "wtr_currTemp b_focusTextLarge"})

    precipitation = soup.find("div", {"class": "wtr_currPerci"})

    wind_speed = soup.find("div", {"class": "wtr_currWind"})

    humidity = soup.find("div", {"class": "wtr_currHumi"})

    return current_conditions, temperature, precipitation, wind_speed, humidity


def get_ten_day(html):
    """Find the forecast for every day for 10 days following the search"""

    soup = get_weather_data(zip_code=get_zipcode())

    # Looking in the child nodes under the wtr_innerScroll class
    forecast_element = soup.find_all("div", {"class": "wtr_innerScroll"})
    for child in forecast_element:
        children = child.find_all("div", {"class": "wtr_forecastDay wtr_noselect"})
        for kids in children:
            target = kids.find_all("div", {"class": "vpc"})

            # Pulls the day of the week in date format (Sep 21)
            for date_class in target:
                obj = date_class.find_all("div", {"class": "wtr_weekday"})
                for day in obj:
                    weekday = day.find_all("span", {"class": "wtr_nowrap b_promoteText"})
                    for date in weekday:
                        return date.text

            # Pulls the high temperature for that date
            for high_temp_element in target:
                line = high_temp_element.find_all("div", {"class": "wtr_high"})
                for high_temperature in line:
                    high_temp = high_temperature.find_all("span")
                    for temp in high_temp:
                        return temp.text

            # Pulls the low temperature for that date
            for low_temp_element in target:
                item = low_temp_element.find_all("div", {"class": "wtr_low"})
                for low_temperature in item:
                    low_temp = low_temperature.find_all("span")
                    for degrees in low_temp:
                        return degrees.text

            # Pulls the chance of precipitation
            for precip in target:
                new = precip.find_all("div", {"class": "wtr_daypreci"})
                for percent_precip in new:
                    perc_perc = percent_precip.find_all("span")[1:2]
                    for pre in perc_perc:
                        print("Chance of Precipitation: " + pre.text + "\n")
                    for precip_type in perc_perc:
                        if precip_type.find_all("span")[0:1] == "wtr_snowIcon":
                            snow_chance = "Chance of Snow: "
                        elif precip_type.find_all("span")[0:1] == "wtr_rainIcon":
                            rain_chance = "Chance of Rain: " + pre.text


def output():
    """Print the output of the above functions in a readable way"""
    
    print("\n")
    print("The weather for " + location.text + "\n" + date_requested.text)
    print("Current Conditions: " + current_conditions.text)
    print("Temperature: " + temperature.text + "°F")
    print(precipitation.text)
    print(wind_speed.text)
    print(humidity.text + "\n")
    print("Your 10-Day Forecast: " + "\n")
    print(date.text + ":")
    print("High: " + temp.text + "F")
    print("Low: " + tamp.text + "F")
    print("Chance of Precipitation: " + pre.text + "\n")
    

def main():
    zip_code = get_zipcode()

    raw_data = get_weather_data(zip_code)
    location = get_location_and_date(raw_data)
    current = get_current(raw_data)
    ten_day = get_ten_day(raw_data)

    output


if __name__ == "__main__":
    main()
