# Building GUI with the help of PyInstaller
# Assistance from :https://medium.com/@maziarizadi/pickle-your-model-in-python-2bbe7dba2bbb
#                  https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/
#                  https://docs.python.org/3/library/tkinter.html
                    

# importing neccessary libraries
import tkinter as tk
from tkinter import simpledialog, messagebox
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import pickle


# loading the Saved model and vectorizer
model = pickle.load(open('logistic_regression_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

def analyze_sentiment():
    review = text_entry.get("1.0", "end-1c")  # Get the review from the text entry widget
    processed_review = vectorizer.transform([review])  # Vectorize the review
    prediction = model.predict(processed_review)  # Predict sentiment
    result = "Positive" if prediction[0] == 1 else "Negative"
    messagebox.showinfo("Prediction", f"The review sentiment is: {result}")


# Setting up the GUI
root = tk.Tk()
root.title("Review Analysis")
root.geometry("400x200")

label = tk.Label(root, text="Enter your review:")
label.pack(pady=10)

text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

predict_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
predict_button.pack(pady=20)

root.mainloop()