from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pag1')
def index():
    return render_template('pag1.html')

@app.route('/pag2')
def index():
    return render_template('pag2.html')

@app.route('/pag3')
def index():
    return render_template('pag3.html')

if __name__ == '__main__':
    app.run(debug=True)


