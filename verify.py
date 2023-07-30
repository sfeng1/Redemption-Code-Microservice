from flask import Flask, request
from UX import *

# creating a Flask app
app = Flask(__name__)
codelook = None

# on the terminal type: curl http://127.0.0.1:5000/
@app.route('/code', methods=['GET'])
def codever():
    codelook = request.args.get('code')
    data = str(codelook)
    return_result = code_verify(data)

    if return_result is None:
        return_result = "Not Valid"
    else:
        return_result = "Valid"

    return return_result

if __name__ == '__main__':
    app.run()


