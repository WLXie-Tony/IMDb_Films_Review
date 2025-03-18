# Movie_Review_Analysis

## Overview
This repository contains scripts and datasets for scraping, analyzing, and processing IMDb movie reviews. The project includes web scraping scripts, organized datasets, and large language model (LLM) analysis for processing user reviews.

---
## **Project Structure**
├── Dataset/                              # Contains structured data for IMDb movies
│   ├── Movie_Datas/                      # Processed datasets of movie information
│   ├── Movie_Reviews/                    # Scraped user reviews from IMDb
│   ├── URLs/                             # Stored IMDb movie URLs and metadata
├── LLM_Review_Analysis/                  # Large language model-based review analysis
├── Scraper_Code/                         # Web scraping scripts for extracting IMDb data
│   ├── 01_imdb_movie_urls_scraper.py     # Scrapes IMDb URLs from movie names
│   ├── 02_imdb_movie_details_scraper.py  # Extracts detailed movie information
│   ├── 03_imdb_movie_reviews_scraper.py  # Scrapes user reviews from IMDb
├── .gitignore                            # Files and folders to be ignored by Git
├── LICENSE                               # License information
├── README.md                             # Project documentation
├── configprogram.json                    # Configuration file for processing
├── main.py                               # Main execution script
├── tracking_token_generator.js           # Generates session tokens for web scraping

## **Features**

### **1. Web Scraping**
- **IMDb Movie URLs Scraper** (`01_imdb_movie_urls_scraper.py`)  
  Extracts IMDb URLs for a list of movies based on a predefined dataset.
- **Movie Details Scraper** (`02_imdb_movie_details_scraper.py`)  
  Gathers movie metadata, including IMDb rating, director, box office performance, and other key attributes.
- **User Reviews Scraper** (`03_imdb_movie_reviews_scraper.py`)  
  Scrapes user reviews along with ratings, timestamps, and review content.

### **2. Dataset Organization**
- `Dataset/Movie_Datas/` → Contains structured datasets of movie metadata.
- `Dataset/Movie_Reviews/` → Stores user reviews collected from IMDb.
- `Dataset/URLs/` → Saves extracted IMDb URLs.

### **3. LLM-Based Review Analysis**
- `LLM_Review_Analysis/` → Includes Jupyter notebooks and scripts for analyzing user reviews using large language models.

### **4. Configuration and Token Generation**
- `configprogram.json` → Stores parameters for running scripts.
- `tracking_token_generator.js` → Generates session tokens required for IMDb data scraping.

---

## **Usage**

### **1. Install Dependencies**
Ensure you have the necessary Python packages installed:
```bash
pip install -r requirements.txt

### **2. Configure Settings**
Modify the `configprogram.json` file to set your parameters:
```json
{
  "movies_list_path": "path/to/movies_list.csv",
  "output_directory": "Dataset/",
  "token_refresh_rate": 3600,
  "max_reviews_per_movie": 100
}

Data Description
Movie Metadata
The movie metadata includes:

Title
Release year
IMDb rating
Director(s) and cast
Genre
Runtime
Box office figures
Plot summary

Review Data
Each review includes:

User rating (1-10)
Review text
Submission date
Helpfulness votes
User ID (anonymized)


LLM Analysis Capabilities
The LLM-based review analysis can perform:

Sentiment analysis of reviews
Thematic clustering
Key aspects extraction (acting, plot, cinematography)
Review summarization
Trend analysis across time periods


Limitations

Data collection respects IMDb's robots.txt and usage policies
Rate limits are implemented to avoid server overload
This tool is intended for research purposes only


License
This project is licensed under the terms specified in the LICENSE file.

Contributors

WLXie-Tony


Acknowledgements

IMDb for providing a comprehensive movie database
Open source libraries used in this project
