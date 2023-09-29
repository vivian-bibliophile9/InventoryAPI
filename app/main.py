from fastapi import FastAPI


#This creates the main application.
app = FastAPI()


#This is an example of a API route.
#On whatever URL this app is hosted on, for example 127.0.0.1
#127.0.0.1/ will return with this JSON message 
@app.get("/")
async def root():
    return {"message": "Hello World"}


#CRUD stuff

@app.get("/item/{id}")
async def getItem(id: int):
    return

@app.post("/add")
async def addItem():
    return

@app.patch("/edit/{id}")
async def editItem(id: int):
    return

@app.delete("/remove/{id}")
async def removeItem(id: int):
    return
