from bs4 import BeautifulSoup
import requests

def get_quote():

    res = requests.get('https://wisdomquotes.com/quote-of-the-day/')
    soup = BeautifulSoup(res.text, 'html.parser')

    div_quote = soup.find('blockquote', {'class': 'quotescollection-quote'})
    quote = div_quote.find('p')
    text = quote.get_text()

    return ("Dave's bot: \"{}".format(text))
