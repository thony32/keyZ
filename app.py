from app import create_app

app = create_app()
app.config['DEBUG'] = True

if __name__ == "__main__":
    app.run(debug=True)