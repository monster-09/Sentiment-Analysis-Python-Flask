# Sentiment-Analysis-Python-Flask

This is a simple sentiment analysis web application built using Flask. The application uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the NLTK library to analyze the sentiment of a given text. The application can classify the sentiment of the input text as Positive, Negative, or Neutral and provides sentiment scores along with the list of words contributing to each sentiment.

Demo
You can access a live demo of the application here.

Features
-> Analyze text to determine the overall sentiment (Positive, Negative, Neutral).
-> View sentiment scores.
-> Identify words contributing to each sentiment category (Positive, Negative, Neutral).

Installation
1. Open VS Code: Launch Visual Studio Code.
2. Open the Sentiment-Analysis-Python-Flask Folder in VS code
3. Open a Terminal in VS Code
4. Execute this command in terminal: 
Install Libraries: pip install Flask nltk
-> python app.py
5. Access the Application: Open your web browser and go to http://127.0.0.1:5000/ to access the Sentiment Analysis Tool.

--Usage--
*Enter Text:
-> On the homepage, enter the text you want to analyze in the text area provided.
*Analyze Sentiment:
-> Click the "Analyze Sentiment" button to see the results.
*View Results:
-> The application will display the overall sentiment (Positive, Negative, Neutral), sentiment scores, and lists of words contributing to each sentiment category.

--File Structure--
app.py: The main Flask application.
templates/index.html: The front-end of the application.
