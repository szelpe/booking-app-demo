import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Parameters
NUM_YEARS = 5
START_YEAR = datetime.now().year - NUM_YEARS
ROOM_TYPES = ["Single", "Double", "Suite"]
STAR_RATINGS = [3, 4, 5]
COUNTRIES = ["USA", "UK", "Germany", "France", "Canada", "Australia", "Italy", "Spain"]
HOTEL_NAMES = ["Grand Plaza", "Ocean View", "Mountain Retreat", "City Lights Hotel", "Royal Stay"]

# Function to generate rand
# om date within a given year
def random_date(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

# Generate data
bookings = []

for year in range(START_YEAR, START_YEAR + NUM_YEARS):
    num_bookings = int(10 * (1.2 ** (year - START_YEAR)))  # Increasing bookings year over year
    
    for _ in range(num_bookings):
        checkin_date = random_date(year)
        num_nights = random.randint(1, 10)
        checkout_date = checkin_date + timedelta(days=num_nights)
        
        hotel_name = random.choice(HOTEL_NAMES)
        room_type = random.choice(ROOM_TYPES)
        star_rating = random.choice(STAR_RATINGS)
        
        base_price = 50 if room_type == "Single" else 100 if room_type == "Double" else 200
        price_multiplier = 1 + (star_rating - 3) * 0.2
        total_price = round(base_price * num_nights * price_multiplier * (1.05 ** (year - START_YEAR)) * random.uniform(0.9, 1.1), 2)  # Increasing price over years with randomness
        
        bookings.append([
            fake.uuid4(),  # booking_id
            random_date(year),  # booking_date
            checkin_date,  # checkin_date
            checkout_date,  # checkout_date
            fake.uuid4(),  # guest_id
            fake.name(),  # guest_name
            fake.email(),  # guest_email
            random.choice(COUNTRIES),  # guest_country
            fake.uuid4(),  # room_id
            room_type,  # room_type
            random.randint(1, 3),  # num_adults
            random.randint(0, 2),  # num_children
            num_nights,  # num_nights
            fake.sentence(nb_words=6),  # special_requests
            total_price,  # total_price
            fake.uuid4(),  # hotel_id
            hotel_name,  # hotel_name
            fake.city(),  # hotel_city
            random.choice(COUNTRIES),  # hotel_country
            star_rating  # star_rating
        ])

# Convert to DataFrame
columns = [
    "booking_id", "booking_date", "checkin_date", "checkout_date", "guest_id", "guest_name", "guest_email", "guest_country",
    "room_id", "room_type", "num_adults", "num_children", "num_nights", "special_requests", "total_price",
    "hotel_id", "hotel_name", "hotel_city", "hotel_country", "star_rating"
]
df = pd.DataFrame(bookings, columns=columns)

# Save to CSV
df.to_csv("hotel_bookings.csv", index=False)
