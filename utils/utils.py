import re
import string

fake_news_first_remove_words = ["Read Also", "Claim", "Fact", "CLAIM:", "RATING:", "FACT-CHECK", "Claim:", "Rating:", "Fact:", "FACT:", "Ã¯Â¿Â½", "check", "CHECK"]
fake_news_second_remove_words = ["Ã¯Â¿Â½", "check", "CHECK", "Â", "Ã¢Â€Â˜", "Ã¢Â€Â™", "Â’ Â", "Â‘", "Â‘"]

news_cls_first_remove_words = ["â€™"]
news_cls_second_remove_words = ["Ã¯Â¿Â½", "check", "CHECK", "Â", "Ã¢Â€Â˜", "Ã¢Â€Â™", "Â’ Â", "Â‘", "Â‘"]

def fake_news_first_remove_words_from_text(text):
    for word in fake_news_first_remove_words:
        text = text.replace(word, "")
    return text

def fake_news_sec_remove_words_from_text_second(text):
    for word in fake_news_second_remove_words:
        text = text.replace(word, "")
    return text

def news_cls_first_remove_words_from_text(text):
    for word in news_cls_first_remove_words:
        text = text.replace(word, "")
    return text

def news_cls_sec_remove_words_from_text(text):
    for word in news_cls_second_remove_words:
        text = text.replace(word, "")
    return text

def clean_text(text):
    text = str(text).lower()
    text = re.sub('https?://\S+|www\.\S+', ' ', text) # Remove URL from string
    text = re.sub('<.*?>+', ' ', text) # Remove HTML Tags
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text) # Replace Punctuation with space
    text = re.sub('\n', ' ', text) # Replace NewLine with space
    text = re.sub(r'\w*\d\w*', ' ', text) # Remove alphanumeric
    text = text.replace('-', ' ')
    text = text.replace('’’', '').replace('’', '').replace('‘‘', '').replace('‘', '')
    text = ' '.join(text.split())  # Strip extra spaces
    return text