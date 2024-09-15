from flask import Flask, render_template, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
import string

# Download VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

app = Flask(__name__)

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.json
        text = data.get('text', '')

        # Get sentiment scores
        sentiment_scores = sid.polarity_scores(text)
        compound = sentiment_scores['compound']

        # Determine overall sentiment
        if compound > 0.05:
            overall_sentiment = "Positive"
        elif compound < -0.05:
            overall_sentiment = "Negative"
        else:
            overall_sentiment = "Neutral"

        # Identify words contributing to sentiment
        positive_words = []
        negative_words = []
        neutral_words = []

        # Remove punctuation and split text into words
        translator = str.maketrans('', '', string.punctuation)
        words = [word.translate(translator).lower() for word in text.split()]

        for word in words:
            if word:  # Ensure the word is not empty
                word_score = sid.polarity_scores(word)['compound']
                if word_score > 0.05:
                    positive_words.append(word)
                elif word_score < -0.05:
                    negative_words.append(word)
                else:
                    neutral_words.append(word)

        return jsonify({
            "Overall Sentiment": overall_sentiment,
            "Sentiment Scores": sentiment_scores,
            "Positive Words": positive_words,
            "Negative Words": negative_words,
            "Neutral Words": neutral_words
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)