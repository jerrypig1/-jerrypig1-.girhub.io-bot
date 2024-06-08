from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python', methods=['POST'])
def run_python():
    result = "Hello from Python!"
    return result

if __name__ == '__main__':
    app.run(debug=True)
