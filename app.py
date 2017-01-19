from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

@app.route('/hello/')
@app.route('/hello/<name>')
def greeting(name=None):
    return render_template('hello.html', user=name)

@app.route('/photo')
def photo_index():
    return 'Here is photo index page!'

@app.route('/photo/<int:photo_id>')
def show_photo(photo_id):
    return 'Photo showing is No.%d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Now do login() and loging in'
    else:
        return 'Show the log page'

if __name__ == "__main__":
    app.run(debug=True)
