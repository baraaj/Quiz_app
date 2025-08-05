from app import app
if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, host='192.168.1.73', port=5000)

#http://192.168.1.73/