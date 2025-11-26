from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Basic security check - only allow safe mathematical expressions
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression):
            return jsonify({'error': 'Invalid characters in expression'}), 400
        
        # Evaluate the expression safely
        result = eval(expression)
        return jsonify({'result': result})
    
    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    except Exception as e:
        return jsonify({'error': 'Invalid mathematical expression'}), 400

if __name__ == '__main__':
    app.run(debug=True)