from fastapi import FastAPI

app=FastAPI()

# /users/1 
# /posts/2
# /users/100/orders/200

# 로 응답이 {"user_id":1}
# {"post_id":2}
# {"user_id":100, "orders_id":200}

@app.get("/users/{user_id}")
def read_item(user_id:int):
    return {"user_id":user_id}

@app.get("/posts/{post_id}")
def read_item(post_id:int):
    return {"post_id":post_id}

@app.get("/users/{user_id}/orders/{order_id}")
def read_item(user_id:int, order_id:int):
    return {"user_id":user_id, "orders_id":order_id}


