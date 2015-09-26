# the main Flask application
from core_logic import create_core_app

app = create_core_app(root='core_logic')

if __name__ == "__main__":
    app.run(**app.config['INIT'])
