from flask import Flask, render_template
app=Flask(__name__) 

app.config['DEBUG']=True

@app.route('/') # decorator
def home():
    # return 'Hello World'
    return render_template('index.html')