from flask import Flask, render_template
import Registers
import ALU
import cu
import RAM

Control = cu.CU("programa1.cpufm")

app = Flask(__name__)

ToPrint = Control.exec()

@app.route('/')
def index():
    return render_template('index.html', toPrint = ToPrint)

if __name__ == '__main__':
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True