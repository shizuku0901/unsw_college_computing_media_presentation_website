from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder = 'template',
        static_folder = 'statistic'
    )
    from blueprints.welcome import welcome_bp
    from blueprints.tips import tips_bp
    from blueprints.facility import facility_bp
    from blueprints.record import record_bp

    app.register_blueprint(welcome_bp)
    app.register_blueprint(tips_bp)
    app.register_blueprint(facility_bp)
    app.register_blueprint(record_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=5001)