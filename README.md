# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MUZAMMIL AHMED

*INTERN ID*: CT04DM174

*DOMAIN*: Python Programming 

 *DURATION*: 4 WEEEKS

*MENTOR*: NEELA SANTOSH

##This project is a simple yet effective demonstration of how to integrate real-world data using a public API (OpenWeatherMap) and convert it into meaningful visual insights using Python's data visualization 

libraries. The idea was born from the need to simplify how we understand multi-day weather trends — particularly for use cases such as smart irrigation systems, travel planning, climate analysis, and educational 

visualization.

The application retrieves 5-day weather forecast data for any specified city and displays two key metrics — temperature and humidity — over time. By transforming raw JSON data into readable plots, it enhances 

user comprehension and decision-making.

**Project Overview**

In today’s data-driven world, being able to interpret weather data visually is essential for planning, research, and development in areas such as agriculture, irrigation systems, smart city planning, and more. 

**This project was created as a demonstration of:**

API integration using Python

Parsing and transforming JSON data from web services

Visualizing time-series data using industry-standard plotting libraries (Seaborn & Matplotlib)

Building a lightweight and script-based dashboard to monitor temperature and humidity trends

**This project is ideal for:**

Developers exploring APIs and data visualization

Hackathon participants building smart irrigation or environmental monitoring tools

Students and learners getting hands-on experience with Python scripting and plotting libraries

**Features**

Fetches 5-day weather forecast for any city via the OpenWeatherMap API

Visualizes temperature (°C) and humidity (%) on time-series line charts

Uses datetime conversion to present readable timestamps

Uses Seaborn for clean and professional chart styling

Lightweight and runs as a single Python script (no web framework required)

**Technologies Used**

Python 3.7+

Requests (for HTTP API calls)

Seaborn (for enhanced statistical plots)

Matplotlib (for plot rendering)

**Setup Instructions**

1.Clone this repository:

2.Install required dependencies:

pip install requests matplotlib seaborn

3.Get your free OpenWeatherMap API key:

Sign up at https://openweathermap.org/api

Navigate to your API keys section and copy your key

4.Open the Python file weather_dashboard.py and update this line with your key:

API_KEY = 'your_openweathermap_api_key'

5.Run the script in the terminal:

python weather_dashboard.py

6.A graph window will pop up showing temperature and humidity trends over the next 5 days (in 3-hour intervals).

**Screenshot Preview**



**Use Cases**
 
IoT & Smart Farming: Visualize temperature and humidity to optimize irrigation systems

Research & Reports: Use real data in visual form for climate-related studies

API Practice: Hands-on example for learning to fetch, parse, and use JSON API data

Educational Projects: Great for students learning Python and data visualization

**Learning Outcomes**
 
Understand how to authenticate and interact with public APIs

Learn JSON parsing and data extraction in Python

Develop skills in visualizing time-series data

Build basic data dashboards without needing a web framework

Learn to structure Python scripts for clean output



**Limitations**

City input must be hardcoded; no user input or GUI yet

Does not handle API request failures or missing data robustly

Only supports one city at a time

Does not include weather condition icons or descriptions

Designed for personal/educational use, not production-grade

**TODO (Future Enhancements)**

Add weather icons and descriptions to the graph

Build a web-based version using Streamlit

Add dropdown to select different cities dynamically

Save charts as PNG or PDF

Add error handling for invalid city or API limits

**Contributing**

Contributions are welcome!

If you have ideas to improve the project, feel free to fork the repository and submit a pull request. Please ensure any changes follow the existing code style and include comments for clarity.

**Acknowledgments**

OpenWeatherMap (https://openweathermap.org/) — for their free and reliable weather API

The Python community — for extensive documentation and support

Seaborn and Matplotlib — for making data beautiful and understandable

Visual Studio Code — for providing a great development environment

**Author**

Built by M.VENKATA SAI KUMAR

Connect on LinkedIn:https://www.linkedin.com/in/venkata-sai-kumar-masanam-56458a27b?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3Bra0oyh%2B%2BTAaU%2B49O2Q2esg%3D%3D

Feel free to reach out with suggestions or collaboration ideas!
