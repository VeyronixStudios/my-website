from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Розділ "Про нас"
@app.route('/about')
def about():
    return render_template('about.html')

# Розділ "Проекти"
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Розділ "Блог"
@app.route('/blog')
def blog():
    return render_template('blog.html')

# Розділ "Галерея"
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Розділ "Особистий кабінет"
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Розділ "Контакти"
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Конкурси
@app.route('/contests')
def contests():
    return render_template('contests.html')

if __name__ == '__main__':
    app.run(debug=True)
