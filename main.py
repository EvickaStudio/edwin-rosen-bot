import os
import time
import requests
import logging
from dotenv import load_dotenv
from requests.exceptions import RequestException

# Load the .env file
load_dotenv()

# Get the webhook link
webhook_link = os.getenv("DISCORD_WEBHOOK")

# URL of the site to monitor
url = "https://edwinrosen.de/faceless/pwa/1/catalog/products?type=Ticket"

# Initial state of the website
initial_state = None

counter = 0

# Header accept json only
headers = {
    "accept": "application/json"
}

# Set up logging to console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Starting monitor")
logging.info("Monitoring " + url)
logging.info("Using Discord webhook: " + webhook_link)
logging.info("Press Ctrl+C to stop the monitor")

session = requests.Session()

while True:
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        counter += 1

        if initial_state is None:
            # Set the initial state of the website
            initial_state = response.json()
            logging.info("Initial state set")
        elif initial_state != response.json():
            # If the current state of the website is not equal to the initial state, the website has changed
            discord_data = {
                "content": "Da hat sich wohl was verändert!\nEventuell gibt es neue Tickets! \n\n" + str(response.json())
            }
            response = session.post(webhook_link, data=discord_data, timeout=10)
            response.raise_for_status()

            # Log the change
            logging.info("Website has changed")

            # Update the initial state
            initial_state = response.json()

        # Wait for a while before the next request
        logging.info(f"Waiting 60 seconds before the next request (Current requests: {counter})")
        time.sleep(60)

    except RequestException as e:
        # Log the exception
        logging.error("Error occurred: " + str(e))

        # Wait for a while before the next request
        time.sleep(60)
