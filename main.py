from flask import Flask,request
import json
from veiws.timing_view import scheduler

app = Flask(__name__)


@app.route("/getz",methods=['GET'])
def get():
    print(">>>>>",666677)
    return json.dumps({"code":200,'msg':"66677"})



if __name__ == '__main__':
    app.run(host='123.249.3.67',port=5000,debug=True)





