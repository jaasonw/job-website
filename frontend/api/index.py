from shillelagh.backends.apsw.db import connect
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/python")
def hello_world():
    connection = connect(":memory:")
    cursor = connection.cursor()

    SQL = """
    SELECT Company
    FROM "https://docs.google.com/spreadsheets/d/1Rp1yFWi6yJMhUGq2fkfGUhkmteScma5r9XkUEbqhq14/edit#gid=0"
    """
    rows = [row for row in cursor.execute(SQL)]
    return {"rows": rows}