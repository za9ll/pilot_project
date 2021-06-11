def calc_operation(a, b, operation):
    if operation == '+':
        return str(int(a) + int(b));
    elif operation == '-':
        return str(int(a) - int(b));
    elif operation == '*':
        return str(int(a) * int(b));
    elif operation == '/':
        if (b != '0'):
            return str(int(a) / int(b))
        else:
            return "Invalid operation";


q=66
w=6
e='/'
print (calc_operation(q,w,e))
