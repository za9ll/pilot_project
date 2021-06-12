from flask import Flask
app = Flask(__name__)

def division(a, b):
    if b !=0:
        return str(int(a / b))
    else:
        return 'division by zero'

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
		
# curl -H "Content-Type: application/json" http://:5000/count_up
@app.route("/count_up", methods=["POST"])
def count_up(d):
    if is_digit(d.get('left', None)):
        if is_digit(d.get('right', None)):
            if chek_data(d.get('operator', None)):
                d_operator = { '+': str(d['left'] + d['right']), '-': str(d['left'] - d['right']),'*': str(d['left'] * d['right']),'/': division(d['left'], d['right'])}
                if chek_data(d_operator.get(d['operator'], None)):
                    return d_operator[d['operator']]
                else:
                    return 'invalid operator'
            else:
                return 'invalid operator'
        else:
            return 'invalid operand "right"'
    else:
        return 'invalid operand "left"'
    
dic = {'left':1,'right':0,'operator':'+'}
print (count_up(dic))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
