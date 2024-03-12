from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/categories/')
def categories():
    categories_list = {"Одежда": "clothes.html", "Обувь": "shoes.html", "Куртки": "jackets.html"}
    return render_template('categories.html', categories_list=categories_list)


@app.route('/clothes/')
def clothes():
    clothes_list = [
        {'name': 'Футболка', 'price': 340},
        {'name': 'Брюки', 'price': 600},
        {'name': 'Носки', 'price': 100}
    ]
    return render_template('clothes.html', list=clothes_list)


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {'name': 'Кроссовки', 'price': 5000},
        {'name': 'Кеды', 'price': 2300},
        {'name': 'Туфли', 'price': 23000}
    ]
    return render_template('shoes.html', list=shoes_list)


@app.route('/jackets/')
def jackets():
    jackets_list = [
        {'name': 'Кожанная', 'price': 34000},
        {'name': 'Ветровка', 'price': 2500},
        {'name': 'Зимняя', 'price': 12400}
    ]
    return render_template('jackets.html', list=jackets_list)



@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)