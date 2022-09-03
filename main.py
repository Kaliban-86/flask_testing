from flask import Flask, render_template, request
from parser_hh import to_pars_hh
app = Flask(__name__)


@app.route('/')
def wor_to_res():
    result = 'result'

    return render_template('main.html', result=result)


@app.route('/run/', methods=(['GET']))
def run_get():
    return render_template('form.html')


@app.route('/run/', methods=(['POST']))
def run_post():
    text = request.form['input_text']
    pars_res = to_pars_hh(text)
    text = pars_res['average_salary']
    return render_template('second.html', text=text)


if __name__ == '__main__':
    app.run(debug=True)
