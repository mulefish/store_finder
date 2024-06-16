from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/stores')
def index():
    return render_template('store_finder.html')

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)