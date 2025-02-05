CREATE TABLE hotel_bookings_raw (
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
COPY hotel_bookings_raw FROM PROGRAM 'curl "https://raw.githubusercontent.com/szelpe/booking-app-demo/refs/heads/master/data-generator/hotel_bookings.csv"'
WITH (FORMAT csv, DELIMITER ',', HEADER);

SELECT 
    booking_id::UUID AS booking_id,
    booking_date::DATE AS booking_date,
    checkin_date::DATE AS checkin_date,
    checkout_date::DATE AS checkout_date,
    guest_id::UUID AS guest_id,
    guest_name::TEXT AS guest_name,
    guest_email::TEXT AS guest_email,
    guest_country::TEXT AS guest_country,
    room_id::UUID AS room_id,
    room_type::TEXT AS room_type,
    num_adults::INT AS num_adults,
    num_children::INT AS num_children,
    num_nights::INT AS num_nights,
    special_requests::TEXT AS special_requests,
    total_price::DECIMAL(10,2) AS total_price,
    hotel_id::UUID AS hotel_id,
    hotel_name::TEXT AS hotel_name,
    hotel_city::TEXT AS hotel_city,
    hotel_country::TEXT AS hotel_country,
    star_rating::INT AS star_rating
FROM hotel_bookings_raw;
