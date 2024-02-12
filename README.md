# Cryptocurrency News Scraper and Telegram Notifier

This project is designed to scrape the latest cryptocurrency news from a specified news website and send a summarized notification to a Telegram chat. It utilizes Python with BeautifulSoup for web scraping and the Telegram Bot API for notifications.

## Features

- Scrapes cryptocurrency news from a predefined news source.
- Summarizes the news article with title and summary.
- Sends the news summary to a specified Telegram chat.

## Prerequisites

Before you can run this script, you need to have Python installed on your system along with some additional modules:

- BeautifulSoup4
- Requests

You can install these dependencies using pip:

pip install beautifulsoup4 requests

Additionally, you'll need to set up a Telegram Bot:

1. Use [BotFather](https://t.me/botfather) to create a new Telegram bot and obtain your bot's API token.
2. Find your Telegram chat ID using a service like @userinfobot.

## Installation

1. Clone this repository to your local machine:

git clone https://yourrepositorylink.com/project.git

2. Navigate to the project directory:

cd path/to/project

3. Install the required Python packages:

pip install -r requirements.txt

## Configuration

1. Open the `config.py` file in the project directory (create one if it doesn't exist).
2. Add your Telegram bot token and chat ID to the file:

```python
TELEGRAM_BOT_TOKEN = 'your_bot_token_here'
TELEGRAM_CHAT_ID = 'your_chat_id_here'
