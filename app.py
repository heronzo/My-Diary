from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/create_entry')
def create_entry():
    return render_template('create-entry.html')
@app.route('/entries')
def entries():
    return render_template('entries.html')
@app.route('/details')
def entry_details():
    return render_template('entry-details.html')
if __name__=='__main__':
    app.run(debug=True)