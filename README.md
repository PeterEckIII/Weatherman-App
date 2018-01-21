# Weatherman-App
An app that delivers current weather conditions and ten-day forecast information when given a zip code

# Beginnings with Selenium
Originally my focus was to create a weather app by any means, and having familiarity with selenium webdriver I figured I would begin there. After building the app, I realized the initiation of a web session was eating into a lot of my memory, and the launching of a browser was not doing me any favors, so I researched the BeautifulSoup and requests libraries and realized the performance was much better.

# Pulling Current Weather Conditions
The first part of the app pulls the location of the search, current conditions (partly sunny, cloudy, etc.), and current weather data such as temperature, humidity, wind speed, and precipitation. After that, the project began to get more complicated.

# The 10-Day Forecast
The current weather conditions were found and printed rather easily, with .find methods being called on the class names of the <div> elements I was searching for. When it came to the 10-day forecast, I noticed I would have to dig deeper into each <div> to find its child elements. This part of the program really tested my frame of mind, thinking about several nested for loops and trying to keep track of everything from a variable standpoint as well. 
  
# Moving Forward
This app isn't done yet, as I'd like to clean up a lot of the code, breakout the program into definitive functions to increase readability, and maybe explore different methods of reaching the element I'm looking for in the nested for loops. 
