Movie_Review_Analysis
Overview
This repository contains scripts and datasets for scraping, analyzing, and processing IMDb movie reviews. The project includes:

Web scraping scripts for collecting IMDb movie data and user reviews.
Organized datasets containing structured metadata and user review information.
Large language model (LLM) analysis for processing and extracting insights from reviews.
Project Structure
graphql
Copy
Edit
├── Dataset/                               # Contains structured IMDb movie data
│   ├── Movie_Datas/                       # Processed datasets of movie metadata
│   ├── Movie_Reviews/                     # Scraped user reviews from IMDb
│   ├── URLs/                              # IMDb movie URLs and metadata
├── LLM_Review_Analysis/                   # Large language model-based review analysis
├── Scraper_Code/                          # Web scraping scripts for extracting IMDb data
│   ├── 01_imdb_movie_urls_scraper.py      # Scrapes IMDb URLs from movie names
│   ├── 02_imdb_movie_details_scraper.py   # Extracts detailed movie metadata
│   ├── 03_imdb_movie_reviews_scraper.py   # Scrapes user reviews from IMDb
├── .gitignore                             # Files and folders ignored by Git
├── LICENSE                                # License information
├── README.md                              # Project documentation
├── configprogram.json                     # Configuration file for processing
├── main.py                                # Main execution script
├── tracking_token_generator.js            # Generates session tokens for web scraping
Features
1. Web Scraping
IMDb Movie URLs Scraper (01_imdb_movie_urls_scraper.py)
Extracts IMDb URLs for a predefined list of movies.
Movie Details Scraper (02_imdb_movie_details_scraper.py)
Collects key metadata such as:
IMDb rating
Director(s) and cast
Box office performance
Genre, runtime, and plot summary
User Reviews Scraper (03_imdb_movie_reviews_scraper.py)
Scrapes user reviews along with:
Ratings (1-10)
Review text
Submission date
Helpfulness votes
Anonymized User IDs
2. Dataset Organization
Dataset/Movie_Datas/ → Processed structured datasets of movie metadata.
Dataset/Movie_Reviews/ → Stores user reviews collected from IMDb.
Dataset/URLs/ → Saves extracted IMDb URLs for further analysis.
3. LLM-Based Review Analysis
LLM_Review_Analysis/ → Contains Jupyter notebooks and scripts for analyzing IMDb reviews using large language models (LLMs).
Capabilities include:
Sentiment Analysis: Categorizing reviews into positive, neutral, and negative sentiments.
Thematic Clustering: Identifying major themes in user reviews.
Key Aspects Extraction: Analyzing user opinions on acting, plot, cinematography, and more.
Review Summarization: Generating concise summaries of user feedback.
Trend Analysis: Examining sentiment and topic trends across different time periods.
4. Configuration and Token Generation
configprogram.json → Stores configurable parameters for running scripts.
tracking_token_generator.js → Generates session tokens required for IMDb data scraping.
Data Description
Movie Metadata
The dataset includes key attributes for each movie, such as:

Title
Release Year
IMDb Rating
Director(s) & Cast
Genre & Runtime
Box Office Figures
Plot Summary
Review Data
Each collected review contains:

User Rating (1-10)
Review Text
Submission Date
Helpfulness Votes
Anonymized User ID
Limitations
Data collection respects IMDb's robots.txt and usage policies.
Rate limits are implemented to prevent server overload.
This project is intended for research purposes only.
License
This project is licensed under the terms specified in the LICENSE file.

Contributors
WLXie-Tony
Acknowledgements
IMDb for providing a comprehensive movie database.
Open-source libraries used in this project.
Note:
This repository is actively maintained. Contributions and improvements are welcome!
