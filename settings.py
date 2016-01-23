import os


DATABASE_SETTINGS = dict(host="127.0.0.1", username="root", password="x", database="test")

APP_SETTINGS = {
    "template_path": os.path.join(os.getcwd(), "templates"),
    "static_path": os.path.join(os.getcwd(), "static")
}
