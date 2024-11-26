from flask import Flask, render_template, request, jsonify
from chatbot import analyze_input, get_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    # 分析用户输入并获取回应
    intent = analyze_input(message)
    response = get_response(intent)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
