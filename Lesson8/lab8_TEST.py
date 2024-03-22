from flask import Flask, jsonify, render_template
import sys
import lab6

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Портал написан на Flask"

@app.route('/configs')
def p_page1():
    return "тут должны быть имена хостов"

@app.route('/configs/hostname')
def p_page4():
    ip_list = lab6.get_ip()
    return render_template("page4.html",
                           ip_list=ip_list)
@app.route('/python')
def p_python():
    return jsonify(sys.path)

@app.route('/page2/<name1>/<name2>')
def p_page2(name1, name2):
    return "Зафиксировано обращение к " + name1 + ", " + name2

@app.route('/page3')
def p_page3():
    return render_template("page3.html",
                           my_string="Длинная тестовая строка",
                           my_list=["Элемент 1", "Элемент 2", "Элемент 3"]
        )

if __name__ == '__main__':
    app.run(debug=True)