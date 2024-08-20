from transformers import pipeline

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = pipeline("sentiment-analysis")

    def analyze_sentiment(self, text):
        return self.analyzer(text)

if __name__ == "__main__":
    sentiment_analyzer = SentimentAnalyzer()
    sentiment = sentiment_analyzer.analyze_sentiment("This is a fantastic project!")
    print("Sentiment:", sentiment)
