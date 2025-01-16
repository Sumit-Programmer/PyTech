from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Use render_template to load the HTML

# Route for executing Python code
@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data.get('code')

    try:
        # Use subprocess to execute the Python code securely
        result = subprocess.run(
            ['python3', '-c', code], 
            capture_output=True, text=True, timeout=5
        )
        output = result.stdout + result.stderr
    except Exception as e:
        output = f"Error: {str(e)}"

    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
