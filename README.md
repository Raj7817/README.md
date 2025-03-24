# Twitter Scraping Tool

## Overview
This is a Python-based tool to scrape Twitter data using keywords or hashtags, store it in MongoDB, and provide options to download the data as CSV or JSON files. Built with Streamlit for an interactive GUI.

## Prerequisites
- Python 3.8+
- MongoDB installed and running
- Git

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/twitter_scraper.git
   cd twitter_scraper

2.Install dependencies: bash -  pip install -r requirements.txt

3. Start MongoDB: bash -    mongod
Usage

1. Run the application:
bash
streamlit run app.py

2. Access the tool:
Open your browser at http://localhost:8501
Enter a keyword/hashtag
Select date range
Set tweet limit
Click "Scrape Tweets"
Choose to save to MongoDB or download as CSV/JSON

Features

Keyword/hashtag-based Twitter scraping
Custom date range selection
Tweet count limitation
MongoDB storage
CSV and JSON export options
Interactive Streamlit interface

Project Structure
text


twitter_scraper/
├── scraper.py         # Twitter scraping logic
├── database.py        # MongoDB operations
├── app.py            # Streamlit GUI
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation

Workflow

Input search parameters in the sidebar
Scrape tweets using snscrape
Display results in a table
Store in MongoDB or download data

Dependencies

snscrape==0.6.2.20230320
pandas==2.0.0
pymongo==4.3.3
streamlit==1.20.0

Contributing

Feel free to fork this repository and submit pull requests with improvements!

License
MIT License

![image](https://github.com/user-attachments/assets/fc0a7393-d5de-4e96-be5c-8cfa89060c2a)

