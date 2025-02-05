### **Hotel Booking Data Analysis Tasks**

A hotel chain has provided a dataset containing booking details from the past five years. They are interested in analyzing trends, optimizing revenue, and improving customer experience. Your task is to process the data and extract insights using PostgreSQL.

#### **1. Import the CSV into PostgreSQL**

The hotel chain needs to store this dataset in their PostgreSQL database for further analysis. Your task is to:
- Load the CSV file into a PostgreSQL table.
- Ensure the import process is efficient and correctly handles large datasets.

#### **2. Define the Correct Column Types**

To ensure accurate queries and better performance, the company wants to enforce proper data types and consistency. You need to:
- Define appropriate column types such as dates, numbers, and unique identifiers.
- Convert any values stored as text into their correct types.
- Ensure the dataset maintains integrity by applying constraints where necessary.

#### **3. Calculate Key Business Metrics**

The management team is looking for a high-level overview of key performance indicators. They need you to calculate:

- The total revenue generated from bookings.
- The average duration of stays across all bookings.
- The number of bookings per country.
- The average revenue per night per hotel

#### **4. Perform Advanced Aggregations**

To understand the performance of different hotel locations and room types, the team needs deeper insights. Your task is to:

- Analyze revenue and booking counts by hotel, room type, and guest country.
- Provide reports that summarize data at multiple levels of granularity.
- Allow flexible reporting by ensuring different grouping combinations are available.

#### **5. Evaluate Booking and Revenue Variability Across Multiple Factors**

The finance team wants to understand how different factors impact hotel performance by analyzing revenue and booking trends across independent dimensions. Your task is to:

- Compare total revenue and booking counts across **room types, star ratings, and guest countries**.
- Identify variations in performance by analyzing **combinations of these factors, including all possible interactions**.
- Help the finance team determine whether higher-star hotels consistently generate more revenue regardless of room type or country of origin.

#### **6. Analyze Booking Trends Over Time**

The operations team is looking for insights into seasonal trends and booking behaviors. They need reports on:

- Year-over-year revenue trends to measure growth.
- The most popular booking months over the past five years.
- 💪 The average lead time between booking and check-in.
- 💪 The most common check-in days of the week.


#### **Optional Extra: Extract Guest Preferences and Trends**

> The taks below requires more advanced skills not covered in this course.

The marketing team wants to understand guest preferences to create targeted offers. They need to:

- Identify common special requests made by guests.
- Aggregate these preferences based on hotel location and room type.
- Provide insights on which services guests frequently request.
