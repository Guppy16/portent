import json
from datetime import datetime


def get_labelled_news_data(fname):

    try:
        with open(fname, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        return []

    news_items = []
    for item in data:

        if not item["categories"]:
            continue

        # Get the publication date string.
        pub_date_str = item.get("pub_date", "")

        # Parse the pub_date string into a datetime object.
        # Expected format: "2024-01-01T00:25:32+0000"
        try:
            # Note: The format "%z" expects a colon in the timezone offset in some Python versions.
            # If your string does not have a colon (i.e. "+0000" instead of "+00:00"), you can use:
            pub_date = datetime.strptime(pub_date_str, "%Y-%m-%dT%H:%M:%S%z")
        except Exception as e:
            print(f"Error parsing date '{pub_date_str}': {e}")
            pub_date = None

        # Create a news item dictionary.
        news_item = {"content": item, "date": pub_date}
        news_items.append(news_item)
    return news_items
