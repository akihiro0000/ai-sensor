#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return
  
if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=True)
