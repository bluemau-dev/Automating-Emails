import json
import random

def load_quote():
    # Opens JSON File of Quotes
    with open("src/quotes.json", "r", encoding="utf-8-sig") as f:
        quotes = json.load(f)

    # Length of JSON List
    length = len(quotes)

    # Gets Random Quote
    RANDOM_QUOTE = random.randrange(length)
    GENERATED_QUOTE = quotes[RANDOM_QUOTE]

    # Gets Quote + Author
    QUOTE = GENERATED_QUOTE['quoteText']
    QUOTE_AUTHOR = GENERATED_QUOTE['quoteAuthor']
    return QUOTE, QUOTE_AUTHOR

