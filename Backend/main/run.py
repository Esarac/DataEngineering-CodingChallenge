from app import create_app
from app.utils.db import db

app = create_app()
db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)