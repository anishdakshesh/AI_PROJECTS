import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to scrape vehicle information from a website
def scrape_vehicle_info(vehicle_name, vehicle_model):
    # Example URL for vehicle comparison website (replace with an actual website)
    url = f"https://example.com/vehicle-comparison?name={vehicle_name}&model={vehicle_model}"
    
    # Send a GET request to the website
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract relevant information from the website (replace with actual scraping logic)
        make = soup.find('span', class_='make').text
        year = soup.find('span', class_='year').text
        price = soup.find('span', class_='price').text

        return {
            'Name': vehicle_name,
            'Model': vehicle_model,
            'Make': make,
            'Year': year,
            'Price': price,
        }
    else:
        print(f"Failed to retrieve data for {vehicle_name} {vehicle_model}")
        return None

# Function to compare two vehicles
def compare_vehicles(vehicle1, vehicle2):
    comparison_data = [vehicle1, vehicle2]
    comparison_table = pd.DataFrame(comparison_data)
    return comparison_table

# Get the number of vehicles from the user
num_vehicles = int(input("Enter the number of vehicles to compare: "))

vehicles = []

# Input vehicle information from the user
for i in range(num_vehicles):
    vehicle_name = input(f"Enter the name of vehicle {i+1}: ")
    vehicle_model = input(f"Enter the model of vehicle {i+1}: ")
    
    vehicle_info = scrape_vehicle_info(vehicle_name, vehicle_model)
    if vehicle_info:
        vehicles.append(vehicle_info)

# Compare the vehicles and display the comparison table
if len(vehicles) >= 2:
    comparison_table = compare_vehicles(vehicles[0], vehicles[1])
    print("\nComparison Table:")
    print(comparison_table)
else:
    print("Insufficient data to compare vehicles.")
