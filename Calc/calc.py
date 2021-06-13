#!flask/bin/python
from flask import Flask, request

app = Flask(__name__)

def division(a, b):
    if b !=0:
        return str(int(a / b))
    else:
        return 'division by zero \n'

def chek_data(value):
    if value != None:
        return True
    else:
        return False

def is_digit(num):
    if chek_data(num) and isinstance(num, int):
        return True
    else:
        return False

#def chek_operator(trans):
@app.route("/count_up", methods=["POST"])
def count_up():
    d = request.json    
    if is_digit(d.get('left', None)):
        if is_digit(d.get('right', None)):
            if chek_data(d.get('operator', None)):
                d_operator = { '+': str(d['left'] + d['right']), '-': str(d['left'] - d['right']),'*': str(d['left'] * d['right']),'/': division(d['left'], d['right'])}
                if chek_data(d_operator.get(d['operator'], None)):
                    return d_operator[d['operator']] + '\n'
                else:
                    return 'invalid operator \n'
            else:
                return 'invalid operator \n'
        else:
            return 'invalid operand "right" \n'
    else:
        return 'invalid operand "left" \n'
    
