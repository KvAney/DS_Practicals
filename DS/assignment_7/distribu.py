from multiprocessing import Pool
import requests

# URL of the web service
URL = "http://localhost:5000/data"

def add_data(data):
    response = requests.post(URL, json=data)
    return response.json()

if __name__ == '__main__':
    # Data to be added to the web service
    new_data = {"id": 4, "name": "Alice"}

    # Define the number of processes to use
    num_processes = 4

    # Create a process pool
    pool = Pool(num_processes)

    # Call the add_data function in parallel using the process pool
    results = pool.map(add_data, [new_data] * num_processes)

    # Print the results
    print(results)
