# Sentiment-Analysis-Python-Flask

Sentiment Analysis Tool is a web application designed to analyze and visualize the sentiment of text input using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis model. This application provides a user-friendly interface to input text and receive detailed sentiment analysis results.

--Key Features--

-> Sentiment Classification: Determines the overall sentiment of the input text as Positive, Negative, or Neutral based on the VADER sentiment scores.
-> Sentiment Scores: Provides a breakdown of sentiment scores, including positive, negative, neutral, and compound scores.
-> Word Analysis: Identifies and categorizes individual words in the text into positive, negative, or neutral based on their sentiment scores.
-> Responsive Design: The application features a modern, animated design with a gradient background and smooth transitions to enhance user experience.

--Demo--
You can access a live demo of the application here.
Link: https://sentiment-analysis-python-flask.onrender.com

--Deployment--

The application is deployed on Render, a cloud-based platform that provides a simple way to deploy web applications. Render handles the hosting, scaling, and management of the application, making it accessible from anywhere with an internet connection.

--Installation--
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
