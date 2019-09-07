from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
#create index function
def index():
    template = 'index.html'
    return render_template(template)
                                  


#testserver
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

