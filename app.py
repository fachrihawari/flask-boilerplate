from . import create_app

app = create_app()

# Run app
if __name__ == 'main':
    app.run()