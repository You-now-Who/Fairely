from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    content = request.get_json()
    print(content)
    return jsonify(content)

@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date": "12/12/2020", 
        "programming":"python"
        }

@app.route('/home')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)