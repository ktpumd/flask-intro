
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def first_route():
    return jsonify({"message": "Hello KTP!"})
    
@app.route('/new')
def second_route():
    return jsonify({"message": "Bye KTP!"})

if(__name__ == '__main__'):
    app.run()
