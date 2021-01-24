import random
import requests
from flask import Flask
from flask import request

server = Flask(__name__)

def balanced(s, i=0, cnt=0):
    if i == len(s): return cnt == 0
    if cnt < 0: return False
    if s[i] == "(": return  balanced(s, i + 1, cnt + 1)
    elif s[i] == ")": return  balanced(s, i + 1, cnt - 1)
    return balanced(s, i + 1, cnt)

@server.route("/solve", methods=["POST","GET"])
def solve():
	f = request.get_data()
	print("---->>>"+f.decode())
	
	f = requests.get('http://localhost:5000/input').text if len(f)<1 else f.decode()
	fi = f.replace("{","(").replace("[","(").replace("}",")").replace("]",")")
	result = "OK!" if balanced(fi) else "BAD INPUT :("
	
	return "INPUT: {} -- RESULT: {}\n".format(f,result)


if __name__ == "__main__":
    server.run(host="0.0.0.0",port="5001")
