import csv
import random

# Price range dictionary
price_range = {
    "PPT": (200, 800),
    "Docs": (100, 500),
    "Website": (1500, 3500),
    "App": (2000, 5000),
    "Frontend": (1400, 3000),
    "Backend": (1200, 3000),
    "Figma": (700, 2000),
}

# Function to convert duration to days
def convert_to_days(duration):
    if 'months' in duration:
        return int(duration.split()[0]) * 30
    elif 'weeks' in duration:
        return int(duration.split()[0]) * 7
    else:
        return int(duration.split()[0])

# Generate dataset
def generate_dataset():
    freelancers = ["raghav@gmail.com", "nishtha@gmail.com", "kaushik@gmail.com", "anushka@gmail.com", "test@gmail.com"]
    services = ["App", "Frontend", "Backend", "Figma", "Website", "Docs", "PPT"]

    with open('freelancer_services.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['freelancer_id', 'service', 'project_name', 'client_rating', 'project_duration', 'earnings'])

        for _ in range(5000):  # Generate 50 rows
            freelancer_id = random.choice(freelancers)
            service = random.choice(services)
            project_name = f"{service}Project{_ + 1}"
            client_rating = round(random.uniform(3.5, 5.0), 1)
            project_duration = f"{random.randint(1, 6)} days"
            earnings = random.randint(price_range[service][0], price_range[service][1])

            writer.writerow([freelancer_id, service, project_name, client_rating, project_duration, earnings])

if __name__ == "__main__":
    generate_dataset()
