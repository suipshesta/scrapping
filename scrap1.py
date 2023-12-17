import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

def scrape_weather_data(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        

        # Extract the relevant weather data (modify this based on the structure of the website)
        temperature_data = soup.find_all('span', class_='wu-value wu-value-to')
        print(temperature_data)
        # Create a list to store the extracted data
        # data_list = []

        # for temp in temperature_data:
        #     data_list.append(float(temp.get_text()))

        # Extract the temperature value
        for temp_element in temperature_data:
            temperature_value = temp_element.get_text(strip=True)
            print("Temperature:", temperature_value)

        return temperature_data
    else:
        print(f"Error: Unable to fetch data. Status code {response.status_code}")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Temperature'])
        for temp in data:
            writer.writerow([temp])

def plot_data(data):
    plt.plot(data)
    plt.xlabel('Data Points')
    plt.ylabel('Temperature')
    plt.title('Weather Data Visualization')
    plt.show()

if __name__ == "__main__":
    # URL of the website with weather data (replace it with the actual URL)
    weather_url = 'https://www.wunderground.com/'

    # Scrape weather data
    weather_data = scrape_weather_data(weather_url)

    # if weather_data:
    #     # Save data to CSV file
    #     csv_filename = 'weather_data.csv'
    #     save_to_csv(weather_data, csv_filename)

    #     # Plot the data
    #     plot_data(weather_data)
