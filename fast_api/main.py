from fastapi import FastAPI

# create app
app=FastAPI()


# hello world
@app.get('/')
def helloworld():
    return {'message':'hello world'}