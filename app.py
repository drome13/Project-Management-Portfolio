from flask import Flask, render_template

app = Flask(__name__)

#define route for home page
@app.route('/')
def home():
    return render_template('index.html')


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
