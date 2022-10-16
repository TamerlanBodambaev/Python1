import uid
from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse, FileResponse

class person:
    def __init__(self, name, age):
        self.name= name
        self.age= age
        self.id = str(uuid.uuid4())
        
# conditional database - a set of Person objects
people = [Person("Tom",38), Person("Bob",42), Person("Sam",28)]

# to search for a user in the people list
def find_person(id):
    for person in people:
        if person.id == id:
            return person
        return None
    
app= FastAPI()

@app.get("/")
async def main():
    return FileResponse("public/index.html")

@app.get("/api/users")
def get_people():
    return people

@app.get("/api/users/{id}")
def get_person(id):
    # get user by id
    person = find_person(id)
    print(person)
    # if not found, send status code and error message
    if person==None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={ "message": "User not found" }
            )
    #if the user is found, send it
    return person

@app.post("/api/users")
def create_person(data = body()):
    person = Person(data["name"], data["age"])
    # add an object to the people list
    people.append(person)
    return person

@app.put("/api/users")
def edit_person(data = body()):
    # get user by id
    person = find_person(data["id"])
    # if not found, send status code and error message
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={ "message": "User not found" }
            )
    # if the user is found, change his data and send it back to the client
    person.age = data["age"]
    person.name = data["name"]
    return person

@app.delete("/api/users/{id}")
def delete_person(id):
    # get user by id
    person = find_person(id)
    # if not found, send status code and error message
    if person == None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={ "message": "User not found" }
            )
    # if the user is found, delete it
    people.remove(person)
    return person
