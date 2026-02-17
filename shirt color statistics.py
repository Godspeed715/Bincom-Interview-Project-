import requests
from collections import Counter
from bs4 import BeautifulSoup
from statistics import mode, mean, median, variance
import psycopg2

# The URL to the HTML file on Google Drive
FILE_ID = "1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf"
URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"
WEEKDAYS = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
COLORS=[]

# Send a GET request to the URL
response = requests.get(URL)

# Check if the GET request was successful
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(response.text, "html.parser")
    td_tag = soup.find_all("td")

    # Loop to store all colors in a single array
    for i in td_tag:
        color = i.text
        if color not in WEEKDAYS:
            new_colors = i.text.split(', ')
            COLORS = COLORS + new_colors

    # Uses counter to get the frequencies of the colors
    counts = Counter(COLORS)

    # 1. Calculate the mean color
    MEAN_COLOR_FREQ = mean(counts.values())
    MEAN_COLOR = min(counts, key=lambda c: abs(counts[c] - MEAN_COLOR_FREQ))
    print(MEAN_COLOR)

    # 2. Calculate the most common color
    MOST_COLOR = mode(COLORS)
    print("Mostly worn throughout the week: ",MOST_COLOR)

    # 3. Median Color
    median_color = median(sorted(COLORS))
    print("Median color: ", median_color)

    # 4. Variance of Colors
    variance = variance(counts.values())
    print("Variance: ", variance)

    # 5. Probability of picking RED
    prob_red = COLORS.count("RED") / len(COLORS)
    print("Probability of choosing red: ", prob_red)

    # 6. Save Colors to a postgresql database

    colors = ["RED", "BLUE", "RED", "GREEN", "RED", "BLUE", "BLACK"]

    # Count frequencies
    counts = Counter(colors)

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="colors_db",
        user="postgres",
        password="your_password",
        port="5432"
    )

    cur = conn.cursor()

    # Create table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS color_frequency (
            id SERIAL PRIMARY KEY,
            color VARCHAR(50) UNIQUE NOT NULL, 
            frequency INT
        )
    """)

    # Inserts data
    for color, freq in counts.items():
        cur.execute("""
            INSERT INTO color_frequency (color, frequency)
            VALUES (%s, %s)
            ON CONFLICT (color) 
            DO UPDATE SET frequency = EXCLUDED.frequency;
        """, (color, freq))

    # Save changes
    conn.commit()

    # Close connection
    cur.close()
    conn.close()

    print("Data saved successfully.")

else:
    print(f"Failed to fetch content. Status code: {response.status_code}")