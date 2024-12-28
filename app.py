from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.json.get('expression', '')
        result = eval(expression)  # Be cautious with `eval` in production; sanitize inputs!
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)
