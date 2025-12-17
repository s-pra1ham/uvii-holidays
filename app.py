from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/deals')
def deals():
    return render_template('deals.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/visa-assistance')
def visa_assistance():
    return render_template('visa-and-assistance.html')


if __name__ == '__main__':
    app.run(debug=True)