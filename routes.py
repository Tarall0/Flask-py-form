from flask import Flask, render_template, request
from form import ContactForm
app = Flask(__name__) 

app.secret_key = 'development key'

@app.route('/', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        return 'form posted'

    return render_template('contact.html', form=form)


