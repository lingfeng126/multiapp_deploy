from fastapi import FastAPI
from pymysql import Connect
app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "xadmin"}

@app.get("/db")
def read_item():
    conn = Connect(user='root', password="123456", host="db", port=3306, database='test')
    cur = conn.cursor()
    cur.execute("select count(*) from test;")
    return {"records": cur.fetchone()[0]}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": f"xadmin: {item_id}", "q": q}
