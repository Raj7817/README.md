 database.py
from pymongo import MongoClient
import datetime

def store_in_mongo(df, keyword):
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client['twitter_data']
        collection = db['tweets']
        
        document = {
            "Scraped Word": keyword,
            "Scraped Date": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "Scraped Data": df.to_dict('records')
        }
        
        result = collection.insert_one(document)
        return result.inserted_id
    
    except Exception as e:
        raise Exception(f"Error storing in MongoDB: {str(e)}")
