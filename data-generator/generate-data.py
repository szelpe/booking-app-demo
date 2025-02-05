import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key= os.environ.get("OPENAI_API_KEY")
)
fake = Faker()

# Parameters
NUM_YEARS = 5
START_YEAR = datetime.now().year - NUM_YEARS
ROOM_TYPES = ["Single", "Double", "Suite"]
STAR_RATINGS = [3, 4, 5]
COUNTRIES = ["USA", "UK", "Germany", "France", "Canada", "Australia", "Italy", "Spain"]
HOTEL_NAMES = ["Grand Plaza", "Ocean View", "Mountain Retreat", "City Lights Hotel", "Royal Stay"]
COUNTRIES = {
    "USA": ["New York", "Los Angeles", "Chicago", "San Francisco", "Miami"],
    "UK": ["London", "Manchester", "Edinburgh", "Birmingham", "Glasgow"],
    "Germany": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne"],
    "France": ["Paris", "Lyon", "Marseille", "Nice", "Bordeaux"],
    "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"],
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
    "Italy": ["Rome", "Milan", "Florence", "Venice", "Naples"],
    "Spain": ["Madrid", "Barcelona", "Valencia", "Seville", "Bilbao"]
}

# Function to generate rand
# om date within a given year
def random_date(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    return fake.date_between(start_date=start_date, end_date=end_date)

def generate_special_request(booking_context):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant generating realistic special requests for hotel bookings. The special request should be a short and simple sentence that may contain typos due to hotel guests booking fast."},
            {"role": "user", "content": f"Given the following booking details, generate a realistic special request: {booking_context}"}
        ]
    )
    print(response.choices[0].message.content)
    return response.choices[0].message.content

# Generate data
bookings = []

for year in range(START_YEAR, START_YEAR + NUM_YEARS):
    num_bookings = int(1 * (1.2 ** (year - START_YEAR)))  # Increasing bookings year over year
    
    for _ in range(num_bookings):
        checkin_date = random_date(year)
        num_nights = random.randint(1, 10)
        checkout_date = checkin_date + timedelta(days=num_nights)
        
        hotel_name = random.choice(HOTEL_NAMES)
        room_type = random.choice(ROOM_TYPES)
        star_rating = random.choice(STAR_RATINGS)
        hotel_country = random.choice(list(COUNTRIES.keys()))
        hotel_city = random.choice(COUNTRIES[hotel_country])
        num_adults = random.randint(1, 3)
        num_children = random.randint(0, 2)

        base_price = 50 if room_type == "Single" else 100 if room_type == "Double" else 200
        price_multiplier = 1 + (star_rating - 3) * 0.2
        total_price = round(base_price * num_nights * price_multiplier * (1.05 ** (year - START_YEAR)) * random.uniform(0.9, 1.1), 2)  # Increasing price over years with randomness
        
        booking_context = (
            f"Hotel: {hotel_name}, City: {hotel_city}, Country: {hotel_country}, Room Type: {room_type}, "
            f"Star Rating: {star_rating}, Stay Duration: {num_nights} nights, Check-in: {checkin_date}, "
            f"Check-out: {checkout_date}, Adults: {num_adults}, Children: {num_children}."
        )
        special_request = generate_special_request(booking_context)

        bookings.append([
            fake.uuid4(),  # booking_id
            random_date(year),  # booking_date
            checkin_date,  # checkin_date
            checkout_date,  # checkout_date
            fake.uuid4(),  # guest_id
            fake.name(),  # guest_name
            fake.email(),  # guest_email
            random.choice(list(COUNTRIES.keys())),  # guest_country
            fake.uuid4(),  # room_id
            room_type,  # room_type
            num_adults,  # num_adults
            num_children,  # num_children
            num_nights,  # num_nights
            special_request,  # special_requests
            total_price,  # total_price
            fake.uuid4(),  # hotel_id
            hotel_name,  # hotel_name
            hotel_city,  # hotel_city
            hotel_country,  # hotel_country
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
