from app import app

app = app.me

if __name__ == "__main__":
    app.run(debug=True, port=10003, host="0.0.0.0")