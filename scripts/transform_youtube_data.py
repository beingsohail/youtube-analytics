from pyspark.sql import SparkSession
import os
import json

def transform_youtube_data():
    spark = SparkSession.builder \
        .appName("YouTube Data Transformation") \
        .getOrCreate()

    raw_path = "data/raw/youtube_raw_data.json"
    with open(raw_path, encoding='utf-8') as f:
        raw_json = json.load(f)

    video_items = raw_json['contents'] 

    flat_data = []
    for item in video_items:
        try:
            video = item.get('video', {})

            flat_data.append({
                'videoId': video.get('videoId'),
                'title': video.get('title'),
                'publishedTimeText': video.get('publishedTimeText'),
                'lengthSeconds': video.get('lengthSeconds'),
                'viewCount': video.get('stats', {}).get('views')
            })
        except Exception as e:
            print(f"Skipping video due to error: {e}")
            continue

    if not flat_data:
        print("No valid video data to transform. Check the source file.")
        return

    df = spark.createDataFrame(flat_data)

    os.makedirs("data/processed", exist_ok=True)
    df.write.csv("data/processed/youtube_transformed.csv", header=True, mode="overwrite")
    print("Transformed data saved to data/processed/youtube_transformed.csv")

    spark.stop()

if __name__ == "__main__":
    transform_youtube_data()
