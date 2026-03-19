from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myList = [10,20,30,40,50]
    return render_template('index.html', myList=myList  )




if __name__ == ('__main__'):
    app.run(host='127.0.0.1', port=5500, debug=True)
