from app import create_app, db
from app.models import Count, User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Count': Count}


if __name__ == "__main__":
   app.run(ssl_context="adhoc")

