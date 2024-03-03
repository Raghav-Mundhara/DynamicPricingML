import random
from datetime import datetime, timedelta
import pandas as pd

def generate_dataset(num_entries):
    services = {
        1: {"name": "WebApp", "base_price": 1500, "base_screens": 4, "deadline": 7},
        2: {"name": "Frontend", "base_price": 1000, "base_screens": 5, "deadline": 5},
        3: {"name": "Backend", "base_price": 1000, "base_screens": 3, "deadline": 5},
        4: {"name": "Case Study", "base_price": 200, "base_screens": 4, "deadline": 2},
        5: {"name": "App", "base_price": 2000, "base_screens": 4, "deadline": 10},
        6: {"name": "Debugging", "base_price": 500, "base_screens": 3, "deadline": 2},
        7: {"name": "Figma", "base_price": 800, "base_screens": 10, "deadline": 4},
        8: {"name": "PPT", "base_price": 600, "base_screens": 15, "deadline": 2},
        9: {"name": "Doc", "base_price": 150, "base_screens": 5, "deadline": 1},
    }

    dataset = []

    for _ in range(num_entries):
        client_email = f"client{_}@example.com"
        freelancer_email = f"freelancer{_}@example.com"
        service_type = random.choice(list(services.keys()))
        base_price = services[service_type]["base_price"]
        base_screens = services[service_type]["base_screens"]
        base_deadline = services[service_type]["deadline"]

        # Randomly adjust the impact of deadline and no_of_pages_screens on price
        deadline_factor = random.uniform(0.5, 2.0)  # Adjust this range based on your preferences
        screens_factor = random.uniform(0.5, 2.0)  # Adjust this range based on your preferences

        # Introduce variability in both directions
        deadline = max(1, round(base_deadline * deadline_factor))
        price = max(1, round(base_price * screens_factor))
        no_of_pages_screens = max(1, round(base_screens * screens_factor))

        start_date = datetime.now() - timedelta(days=random.randint(0, 30))
        end_date = start_date + timedelta(days=deadline)

        title = f"{services[service_type]['name']} Project"
        description = f"Description for {services[service_type]['name']} project"

        dataset.append({
            "client_email": client_email,
            "freelancer_email": freelancer_email,
            "price": price,
            "service_type": services[service_type]["name"],
            "start_date": start_date.strftime("%Y-%m-%d"),
            "deadline": end_date.strftime("%Y-%m-%d"),
            "title": title,
            "description": description,
            "no_of_pages_screens": no_of_pages_screens,
        })

    return dataset

# Example usage
num_entries = 10000
generated_dataset = generate_dataset(num_entries)

# Convert the dataset to a DataFrame
df = pd.DataFrame(generated_dataset)

# Export the DataFrame to a CSV file
csv_filename = 'new_generated_dataset5.csv'
df.to_csv(csv_filename, index=False)

print(f"CSV file '{csv_filename}' has been created.")
