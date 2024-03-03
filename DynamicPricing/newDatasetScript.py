import csv
from datetime import datetime, timedelta
import random

# Function to calculate price based on deadline and number of pages
base_prices = {
        "PPT": {"deadline": 5, "price": 200, "pages": 10},
        "Docs": {"deadline": 3, "price": 100, "pages": 8},
        "Website": {"deadline": 7, "price": 1500, "pages": 5},
        "App": {"deadline": 10, "price": 2000, "pages": 3},
        "Figma": {"deadline": 3, "price": 500, "pages": 5},
        "Frontend": {"deadline": 7, "price": 1000, "pages": 4},
        "Backend": {"deadline": 7, "price": 1000, "pages": 4},
        "CaseStudy": {"deadline": 2, "price": 150, "pages": 6},
    }

price_range = {
        "PPT": (200, 800),
        "Docs": (100, 500),
        "Website": (1500, 3500),
        "App": (2000, 5000),
        "Figma": (500, 1500),
        "Frontend": (1000, 3000),
        "Backend": (1000, 3000),
        "CaseStudy": (150, 500),
    }
def calculate_price(service, deadline, no_of_pages):

    base_price = base_prices[service]["price"]
    base_deadline = base_prices[service]["deadline"]
    base_pages = base_prices[service]["pages"]

    if deadline < base_deadline:
        price_increase_due_to_deadline = (base_deadline - deadline) * 50
        base_price += price_increase_due_to_deadline

    if no_of_pages is not None:
        base_pages = no_of_pages if base_pages is None else base_pages
        if no_of_pages > base_pages:
            price_increase_due_to_pages = (no_of_pages - base_pages) * 25
            base_price += price_increase_due_to_pages

    base_price = max(min(base_price, price_range[service][1]), price_range[service][0])

    return base_price

# Function to generate a random date within a given range
def random_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Generate synthetic dataset with updated pricing
def generate_dataset(num_records):
    usernames = [f"user{i}" for i in range(1, num_records + 1)]
    service_providers = [f"provider{i}" for i in range(1, num_records + 1)]
    services = ["PPT", "Docs", "Website", "App", "Figma", "Frontend", "Backend", "CaseStudy"]
    topics = [f"Topic{i}" for i in range(1, num_records + 1)]

    today = datetime.today()
    end_date = today + timedelta(days=30)

    with open("generated_dataset_new.csv", mode="w", newline="") as csv_file:
        fieldnames = ["username", "service_provider_username", "service", "price", "no_of_pages", "topic", "date", "deadline"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(num_records):
            service = random.choice(services)
            deadline = random.randint(1, 15)

            if service in ["Figma", "Frontend", "Backend", "CaseStudy"]:
                no_of_pages = base_prices[service]["pages"]  # Corrected line
            else:
                no_of_pages = random.randint(1, 20) if service not in ["Website", "App"] else random.randint(3, 7)

            date = random_date(today, end_date)
            price = calculate_price(service, deadline, no_of_pages)

            writer.writerow({
                "username": usernames[i],
                "service_provider_username": service_providers[i],
                "service": service,
                "price": price,
                "no_of_pages": no_of_pages,
                "topic": topics[i],
                "date": date.strftime("%Y-%m-%d"),
                "deadline": (date + timedelta(days=deadline)).strftime("%Y-%m-%d")
            })

# Generate 10 records for demonstration
generate_dataset(10000)
print("Dataset generated successfully.")
