import numpy as np
import tkinter as tk
from tkinter import messagebox
from keras.models import load_model
from keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences


word_index = imdb.get_word_index()
model = load_model('model.h5')


def analyze_comment():
    sentence = entry.get() 
    this_sentence = sentence.lower().split(' ')
    print(this_sentence)
    
    try:
       
        for i in range(len(this_sentence)):
            this_sentence[i] = word_index[this_sentence[i].lower()]  
    except KeyError:
        messagebox.showerror("Error", "Some words are not in the vocabulary.")
        return

   
    this_sentence = np.array([this_sentence])
    this_sentence = pad_sequences(this_sentence, maxlen=250)
    
    
    yp = model.predict(this_sentence)
    yp = yp[0][0]
    
    print(yp)
    if yp > 1: 
        result = "This is a good comment!"
    else:
        result = "This is a bad comment!"
    
    messagebox.showinfo("Result", result)


root = tk.Tk()
root.title("Sentiment Analysis")


tk.Label(root, text="Please insert your comment here:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Analyze Comment", command=analyze_comment).pack(pady=20)


root.mainloop()
