import connexion

from connexion.resolver import RestyResolver


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='ng45/openapi/')
    app.add_api('ng45.yaml', resolver=RestyResolver('ng45.api'))
    app.run(host='127.0.0.1', port=8080)
