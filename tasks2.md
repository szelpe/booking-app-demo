# Additional Hotel Booking Data Analysis Tasks

## Identify Top-Performing Hotels by Revenue and Bookings  

The management wants to rank hotels based on their total revenue and total number of bookings. Your task is to:  

- Rank hotels within each country based on total revenue.  
- Rank hotels within each country based on total bookings.  
- Compare whether the revenue ranking aligns with the booking ranking.

## Calculate Cumulative Revenue Over Time for Each Hotel  

The finance team wants to track revenue trends over time. Your task is to:

- Calculate the **cumulative revenue** for each hotel across all months.  
- Ensure that the data is ordered chronologically by booking date.  
- Provide a rolling sum of revenue per hotel to help track revenue growth.

## Year-Over-Year Revenue Growth Analysis  

The operations team needs insights into how revenue has changed over the years. Your task is to:  
- Extract the **year** from the booking date and group revenue by hotel and year.  
- Use `LAG()` to calculate the previous year’s revenue for each hotel.  
- Compute the **YoY growth percentage** to analyze revenue trends.  
- Identify which hotels experienced the highest growth or decline.