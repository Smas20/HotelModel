# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for


class Webserver:

    app = Flask(__name__, static_url_path='/static')

    @app.route("/", methods=['GET'])
    def index(  name='Лагуна Гуниб'):
        """загрузка главной страницы"""
        return render_template('index.html', name=name)

    if __name__ == '__main__':
        app.run(debug=True)


Webserver()
