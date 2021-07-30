from flask import Flask

app = Flask(__name__)

@app.route('/')
def run_script():
    file = open(r'C:/Users/PC/Documents/intern/mypostureaid/app.py', 'r').read()
    return exec(file)

if __name__ == "__main__":
    app.run(debug=True)