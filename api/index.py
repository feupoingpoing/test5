from flask import Flask, render_template, request


app = Flask(__name__)

comments = []

@app.route('/')
def index():
    return render_template('index.html',comments=comments)
   
@app.route('/post', methods=['GET','POST'])
def post():
    if request.method =='POST':
        comment = request.form.get('comment')
        if comment != "":
            comments.append(comment)
    return render_template('post.html', comments=comments)

if __name__ == "__main__":
    app.run(debug=True)