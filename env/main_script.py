from flask import Flask, render_template, request
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
 
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    # Retrieve form data
    username = request.form['username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    button = request.form['button']
    print(button)
    # Add your function logic here to process the registration
    
    return "Registration successful!"  # Or redirect to another page

if __name__ == '__main__':
    app.run(debug=True)