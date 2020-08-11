
# import necessary fuinctions from the Flask package
from flask import Flask, render_template, jsonify

# initialize the Flask app
app = Flask(__name__)

# route to access basic message
@app.route('/')
def first_route():
    return jsonify({"message": "Hello KTP!"})
    
# route to access our homepage
@app.route('/home')
def home_route():
    return render_template('index.html')

# Allows us to actually run the app
if(__name__ == '__main__'):
    app.run()
