
#### **3. Calculate Key Business Metrics**

```sql
-- Total revenue generated from bookings
SELECT SUM(total_price) AS total_revenue
FROM hotel_bookings;

-- Average duration of stays across all bookings
SELECT AVG(num_nights) AS average_stay_duration
FROM hotel_bookings;

-- Number of bookings per country
SELECT guest_country, COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY guest_country
ORDER BY total_bookings DESC;

-- Average revenue per booking
SELECT AVG(total_price) AS average_revenue_per_booking
FROM hotel_bookings;
```


#### **4. Perform Advanced Aggregations**

```sql
-- Analyze revenue and booking counts by hotel, room type, and guest country
SELECT 
    hotel_name, 
    room_type, 
    guest_country, 
    COUNT(*) AS total_bookings, 
    SUM(total_price) AS total_revenue
FROM hotel_bookings
GROUP BY hotel_name, room_type, guest_country
ORDER BY total_revenue DESC;

-- Provide reports that summarize data at multiple levels of granularity
SELECT 
    hotel_name, 
    room_type, 
    COUNT(*) AS total_bookings, 
    SUM(total_price) AS total_revenue
FROM hotel_bookings
GROUP BY ROLLUP (hotel_name, room_type)
ORDER BY hotel_name, room_type;

-- Allow flexible reporting by ensuring different grouping combinations are available
SELECT 
    hotel_name, 
    room_type, 
    guest_country, 
    COUNT(*) AS total_bookings, 
    SUM(total_price) AS total_revenue
FROM hotel_bookings
GROUP BY GROUPING SETS (
    (hotel_name, room_type, guest_country), 
    (hotel_name, room_type), 
    (hotel_name),
    ()
)
ORDER BY hotel_name, room_type, guest_country;
```


#### **5. Evaluate Booking and Revenue Variability Across Multiple Factors**

```sql
-- Compare total revenue and booking counts across room types, star ratings, and guest countries
SELECT 
    room_type, 
    star_rating, 
    guest_country, 
    COUNT(*) AS total_bookings, 
    SUM(total_price) AS total_revenue
FROM hotel_bookings
GROUP BY CUBE (room_type, star_rating, guest_country)
ORDER BY total_revenue DESC;

-- Identify variations in performance by analyzing combinations of these factors
SELECT 
    room_type, 
    star_rating, 
    guest_country, 
    COUNT(*) AS total_bookings, 
    SUM(total_price) AS total_revenue,
    AVG(total_price) AS avg_revenue_per_booking
FROM hotel_bookings
GROUP BY CUBE (room_type, star_rating, guest_country)
ORDER BY room_type, star_rating, guest_country;

-- Determine if higher-star hotels consistently generate more revenue regardless of room type or country of origin
SELECT 
    star_rating, 
    COUNT(*) AS total_bookings, 
    SUM(total_price) AS total_revenue,
    AVG(total_price) AS avg_revenue_per_booking
FROM hotel_bookings
GROUP BY CUBE (star_rating, room_type, guest_country)
ORDER BY star_rating DESC, total_revenue DESC;
```

#### **6. Analyze Booking Trends Over Time**

```sql
-- The most popular booking months over the past five years
SELECT 
    EXTRACT(YEAR FROM booking_date) AS year,
    EXTRACT(MONTH FROM booking_date) AS month,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY year, month
ORDER BY year DESC, total_bookings DESC;

-- Year-over-year revenue trends to measure growth
SELECT 
    EXTRACT(YEAR FROM booking_date) AS year,
    SUM(total_price) AS total_revenue
FROM hotel_bookings
GROUP BY year
ORDER BY year DESC;

-- The average lead time between booking and check-in
SELECT 
    AVG(EXTRACT(DAY FROM (checkin_date - booking_date))) AS avg_lead_time
FROM hotel_bookings;

-- The most common check-in days of the week
SELECT 
    TO_CHAR(checkin_date, 'Day') AS checkin_day,
    COUNT(*) AS total_bookings
FROM hotel_bookings
GROUP BY checkin_day
ORDER BY total_bookings DESC;
```