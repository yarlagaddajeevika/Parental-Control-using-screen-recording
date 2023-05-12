import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import history as his

#Load the model and get the pattern
def model():
    # Load dataset of keywords and categories
    data_df = pd.read_csv('./dataset.csv')

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data_df['text'], data_df['category'], random_state=42)

    # Create a TF-IDF vectorizer to convert keywords to numerical features
    vectorizer = TfidfVectorizer(stop_words='english')

    # # Fit the vectorizer to the training data and transform the training and testing data
    X_train_vectors = vectorizer.fit_transform(X_train)
    X_test_vectors = vectorizer.transform(X_test)

    # # Train a Naive Bayes classifier on the training data
    nb_classifier = MultinomialNB()
    nb_classifier.fit(X_train_vectors, y_train)

    #get the list of titles
    titles = his.getAllTitles()

    # Extract the keywords from the list of titles
    keywords = []
    for title in titles:
        words = title.split()
        for word in words:
            keywords.append(word.lower())

    # # Convert the keywords to a list and transform them using the vectorizer
    vectorized_keywords = vectorizer.transform([' '.join(keywords)])

    # # Predict the category of the keywords
    prediction = nb_classifier.predict(vectorized_keywords)

    # Open the file for writing
    with open('myfile.txt', 'a') as f:
        # Write data to the file
        f.write(f"""Summary:\nPattern of watching:\nYour kid spent most of the day watching {prediction[0]}""")
 
    # # Output the result on to terminal
    if prediction[0] == 'Fiction':
        print("The majority of the titles belong to fiction.")
    else:
        print("The majority of the titles belong to non-fiction.")
        
