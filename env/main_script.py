from flask import Flask, render_template, request, redirect, url_for
 
# WSGI Application
# Provide template folder name
# The default folder name should be "templates" else need to mention custom folder name
app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')
 
@app.route('/')
def index():
    return render_template('login.html')



@app.route('/game', methods=['POST'])
def game():
    return render_template('game.html')



@app.route('/register', methods=['POST'])
def register():
    # Retrieve form data
    # username = request.form['username']
    # password1 = request.form['password1']
    # password2 = request.form['password2']
    # button = request.form['button']
    # Add your function logic here to process the registration
    
    return render_template('register.html')  # Or redirect to another page

# def go_to_other_page():
#     return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)