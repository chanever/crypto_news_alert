import feedparser
from newspaper import Article
import requests
from nltk.tokenize import sent_tokenize

# Ensure nltk's punkt tokenizer is downloaded (needed for sent_tokenize)
import nltk
nltk.download('punkt')

def send_to_telegram(bot_token, chat_id, title, url, summary, extended_summary):
    base_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    message = f"Title: {title}\nURL: {url}\nSummary: {summary}\nExtended Summary: {extended_summary}"
    response = requests.post(base_url, data={'chat_id': chat_id, 'text': message})
    print("Message sent with status code:", response.status_code)

def extract_news_from_rss(feed_url):
    feed = feedparser.parse(feed_url)
    news_items = []

    for entry in feed.entries[:1]:  # Adjust as needed
        title = entry.title
        summary = entry.summary
        article_url = entry.link
        extended_summary = extract_extended_summary(article_url, summary)
        news_items.append((title, article_url, summary, extended_summary))
    
    return news_items

def extract_extended_summary(url, initial_summary):
    article = Article(url)
    article.download()
    article.parse()
    
    # Tokenize the article text into sentences
    all_sentences = sent_tokenize(article.text)
    
    # Find a continuation to form a 10 sentence summary including the initial summary
    initial_sentences = sent_tokenize(initial_summary)
    num_additional_sentences_needed = 10 - len(initial_sentences)
    extended_summary_sentences = initial_sentences + all_sentences[:num_additional_sentences_needed]
    extended_summary = ' '.join(extended_summary_sentences)
    
    return extended_summary

if __name__ == "__main__":
    bot_token = 'fill this area'
    chat_id = 'fill this area'
    feed_url = "https://www.coindesk.com/feed"  # Example, adjust as needed

    news_items = extract_news_from_rss(feed_url)
    for title, url, summary, extended_summary in news_items:
        send_to_telegram(bot_token, chat_id, title, url, summary, extended_summary)
