from flask import Flask
app=Flask(_main_)
@app.route('/')
def hello():
    return "hello world"

app.hello()










