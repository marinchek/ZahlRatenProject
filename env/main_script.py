from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Retrieve form data
    username = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    
    # Add your function logic here to process the registration
    
    return "Registration successful!"  # Or redirect to another page

if __name__ == '__main__':
    app.run(debug=True)