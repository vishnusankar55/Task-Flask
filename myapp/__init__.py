from flask import Flask
def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .admin import admin
        from .user import user
        app.register_blueprint(admin.admin_bp)
        app.register_blueprint(user.user_bp)
        return app

def register_blueprint(app,bp):
    app.register_blueprint(bp)
    return  None