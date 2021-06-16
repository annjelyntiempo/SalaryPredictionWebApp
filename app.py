#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pickle

from flask import Flask, request, jsonify, render_template


# In[2]:


model = pickle.load(open('salaryregressionmodel.pkl', 'rb'))


# In[3]:


app = Flask(__name__, template_folder='templates')


# In[4]:


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return(render_template('index.html'))
    if request.method == 'POST':
        yearsnum = request.form['yearsnum']
        yearsnum = float(yearsnum)
        
        prediction = model.predict([[yearsnum]])
    
        return render_template('index.html', result=prediction[0])


# In[5]:


if __name__ == '__main__':
    app.run(host="128.134.65.180")


# In[ ]:




