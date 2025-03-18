# Movie_Review_Analysis

## Overview
This project consists of a set of scripts for scraping data from IMDb, including:
- URLs for movies
- Movie details such as ratings, directors, and box office performance
- User reviews and ratings for each movie

The project is designed to handle large datasets and save the scraped data in Excel or CSV formats for further analysis.

---

## Features
1. **Scrape IMDb URLs**  
   Use `imdb_movie_urls_scraper.py` to fetch IMDb URLs for a list of movies from an input dataset.
   
2. **Scrape Movie Details**  
   Use `imdb_movie_details_scraper.py` to extract details such as ratings, directors, box office performance, and more.

3. **Scrape User Reviews**  
   Use `imdb_movie_reviews_scraper.py` to fetch user reviews, including review text, ratings, and metadata.

4. **Session Management**  
   `tracking_token_generator.js` dynamically generates session tokens required for making authenticated requests to IMDb.

---

## Project Structure
```plaintext
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
