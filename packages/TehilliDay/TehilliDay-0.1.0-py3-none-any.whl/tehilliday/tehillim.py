import requests
import xml.etree.ElementTree as ET

class TehilliDay:
    def __init__(self):
        self.rss_url = "https://www.chabad.org/tools/rss/dailystudy_rss.xml"

    def get_daily_tehillim(self):
        response = requests.get(self.rss_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the XML
        root = ET.fromstring(response.content)

        # Find the relevant item
        for item in root.findall('.//item'):
            title = item.find('title').text
            if title and "Daily Tehilim - Psalms (Hebrew)" in title:
                description = item.find('description').text
                # Remove "Today's Tehillim:" from the description
                cleaned_description = description.replace("Today's Tehillim:", "").strip()
                return cleaned_description

        return "No Tehillim found for today."
