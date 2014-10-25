from flask import Flask
import qna

app = Flask(__name__)


@app.route('/')
def hello_world():
    sList = [1,2,3,4]
    return 'Hello World!' + str(sList[0])


@app.route('/data/<name>')
def getName(name):
    return str(name)


@app.route('/qna/list')
def qnaList():
    return qna.qnaList()

if __name__ == '__main__':
    app.run(debug=True)