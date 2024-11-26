IMDb Movie Scraper
Overview
This project consists of a set of scripts for scraping data from IMDb, including:

URLs for movies
Movie details such as ratings, directors, and box office performance
User reviews and ratings for each movie
The project is designed to handle large datasets and save the scraped data in Excel or CSV formats for further analysis.

Features
Scrape IMDb URLs
Use imdb_movie_urls_scraper.py to fetch IMDb URLs for a list of movies from an input dataset.

Scrape Movie Details
Use imdb_movie_details_scraper.py to extract details such as ratings, directors, box office performance, and more.

Scrape User Reviews
Use imdb_movie_reviews_scraper.py to fetch user reviews, including review text, ratings, and metadata.

Session Management
tracking_token_generator.js dynamically generates session tokens required for making authenticated requests to IMDb.

Project Structure
bash
Copy code
├── scripts/
│   ├── imdb_movie_urls_scraper.py      # Scrapes IMDb URLs from a list of movie names
│   ├── imdb_movie_details_scraper.py   # Scrapes details for movies
│   ├── imdb_movie_reviews_scraper.py   # Scrapes user reviews and ratings
│   └── tracking_token_generator.js     # Generates tokens for session management
├── data/
│   ├── Box_Mojo_2007-2015.xlsx         # Input file with movie names
│   ├── IMDb_Movie_URLs.xlsx            # Output file with scraped IMDb URLs
│   ├── IMDb_Movie_Details.csv          # Output file with scraped movie details
│   └── IMDb_Reviews_with_Details.xls   # Output file with scraped reviews
├── docs/
│   └── instructions.md                 # Additional instructions or usage tips
├── requirements.txt                    # Python dependencies
├── .gitignore                          # Files to ignore in Git
└── README.md                           # This file
Setup Instructions
1. Prerequisites
Install Python (version >= 3.8)
Install Chrome browser and download the corresponding version of chromedriver
Install the required Python libraries:
bash
Copy code
pip install -r requirements.txt
2. File Preparation
Prepare the input dataset with movie names (e.g., Box_Mojo_2007-2015.xlsx).
Ensure the dataset contains at least one column with movie titles (e.g., Release Group).
3. Run Scripts
Step 1: Scrape IMDb URLs

bash
Copy code
python scripts/imdb_movie_urls_scraper.py
Input: Excel file with movie titles.
Output: Excel file with movie titles and their corresponding IMDb URLs.

Step 2: Scrape Movie Details

bash
Copy code
python scripts/imdb_movie_details_scraper.py
Input: Excel file with IMDb URLs.
Output: CSV file containing movie details.

Step 3: Scrape User Reviews

bash
Copy code
python scripts/imdb_movie_reviews_scraper.py
Input: CSV file with IMDb movie details.
Output: Excel file with user reviews.

Key Components
imdb_movie_urls_scraper.py

Scrapes IMDb URLs for a list of movies using Selenium.
imdb_movie_details_scraper.py

Extracts metadata like title, director, and box office performance from IMDb.
imdb_movie_reviews_scraper.py

Fetches user reviews, including their ratings, review dates, and upvotes.
tracking_token_generator.js

Generates session tokens for accessing IMDb's data dynamically.
Example Usage
To scrape URLs, run the following command:

bash
Copy code
python scripts/imdb_movie_urls_scraper.py
Make sure the input file (Box_Mojo_2007-2015.xlsx) is placed in the data/ folder. The output file (IMDb_Movie_URLs.xlsx) will also be saved in the data/ folder.

Known Issues
IMDb might block requests if too many are made in a short time. Use appropriate time delays (time.sleep()) in your scripts.
Make sure to keep chromedriver updated to avoid compatibility issues with Chrome.
Contributing
Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request with a detailed description of your changes.
