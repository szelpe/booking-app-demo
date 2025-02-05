CREATE TABLE hotel_bookings (
    booking_id TEXT PRIMARY KEY,
    booking_date TEXT NOT NULL,
    checkin_date TEXT NOT NULL,
    checkout_date TEXT NOT NULL,
    guest_id TEXT NOT NULL,
    guest_name TEXT NOT NULL,
    guest_email TEXT NOT NULL,
    guest_country TEXT NOT NULL,
    room_id TEXT NOT NULL,
    room_type TEXT NOT NULL,
    num_adults TEXT NOT NULL,
    num_children TEXT NOT NULL,
    num_nights TEXT NOT NULL,
    special_requests TEXT,
    total_price TEXT NOT NULL,
    hotel_id TEXT NOT NULL,
    hotel_name TEXT NOT NULL,
    hotel_city TEXT NOT NULL,
    hotel_country TEXT NOT NULL,
    star_rating TEXT NOT NULL
);

-- Example Import
COPY hotel_bookings FROM PROGRAM 'curl "https://raw.githubusercontent.com/szelpe/booking-app-demo/refs/heads/master/data-generator/hotel_bookings.csv"'
(DELIMITER ',')
