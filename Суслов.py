from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def hom():
    return render_template('index.html')

@app.route('/page1.html')
def z1p():
    return render_template('page1.html')

@app.route('/page2.html')
def z2p():
    return render_template('page2.html')

@app.route('/page3.html')
def z3p():
    return render_template('page3.html')


if __name__ == '__main__':
    app.run(debug=True)