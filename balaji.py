from flask import Flask,render_template
fai=Flask(__name__)

@fai.route('/first')
def first():
    return render_template('first.html')

@fai.route('/second')
def second():
    return render_template('second.html')

if __name__=='__main__':
    fai.run(debug=True)