import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Load dataset of fiction and non-fiction texts
data_df = pd.read_csv('./dataset.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data_df['text'], data_df['category'], random_state=42)

# Create a TF-IDF vectorizer to convert text to numerical features
vectorizer = TfidfVectorizer(stop_words='english')

# Fit the vectorizer to the training data and transform the training and testing data
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Train a Naive Bayes classifier on the training data
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train_vectors, y_train)

# Predict the categories of the testing data
y_pred = nb_classifier.predict(X_test_vectors)

# Determine the majority category of the list of strings
list_of_strings = ["The Lord of the Rings", "1984", "To Kill a Mockingbird", "A Brief History of Time", "The Catcher in the Rye", "The Great Gatsby"]
vectorized_strings = vectorizer.transform(list_of_strings)
string_predictions = nb_classifier.predict(vectorized_strings)
fiction_count = sum(string_prediction == 'Fiction' for string_prediction in string_predictions)
nonfiction_count = sum(string_prediction == 'Non-Fiction' for string_prediction in string_predictions)

if fiction_count > nonfiction_count:
    print("The majority of the list belongs to fiction.")
elif fiction_count < nonfiction_count:
    print("The majority of the list belongs to non-fiction.")
else:
    print("The list is evenly split between fiction and non-fiction.")
