from bbs import app


if __name__ == "__main__":
    app.run(host='0.0.0.0')
else:
    print("__name__ = %s" % __name__)

