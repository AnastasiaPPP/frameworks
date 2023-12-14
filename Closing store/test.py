from flask import Flask, render_template

app = Flask(__name__)


@app.route('/base/')
@app.route('/')
def show_main():
    return render_template('base.html')


@app.route('/men_clothes/')
def show_men():
    context = {'title': 'Мужская одежда'}
    return render_template('men_clothes.html', **context)


@app.route('/women_clothes/')
def show_women():
    context = {'title': 'Женская одежда'}
    return render_template('women_clothes.html', **context)



if __name__ == '__main__':
    app.run()