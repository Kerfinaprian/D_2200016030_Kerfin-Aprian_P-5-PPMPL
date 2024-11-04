from locust import HttpUser, task, between, constant_pacing
import random

class APIUser(HttpUser):
    wait_time = constant_pacing(1)  

    
    @task(1)
    def get_all_items(self):
        self.client.get("/items", name="GET /items (all items)")

    @task(2)
    def get_item_by_id(self):
        
        item_id = random.randint(1, len(self.client.get("/items").json()) if self.client.get("/items").status_code == 200 else 1)
        self.client.get(f"/items/{item_id}", name="GET /items/{id}")

    @task(1)
    def create_item(self):
        item_name = f"Item {random.randint(1, 1000)}"
        self.client.post("/items", json={"name": item_name}, name="POST /items")

  
    @task(1)
    def update_item(self):
        item_id = random.randint(1, len(self.client.get("/items").json()) if self.client.get("/items").status_code == 200 else 1)
        self.client.put(f"/items/{item_id}", json={"name": f"Updated Item {item_id}"}, name="PUT /items/{id}")

    @task(1)
    def delete_item(self):
        item_id = random.randint(1, len(self.client.get("/items").json()) if self.client.get("/items").status_code == 200 else 1)
        self.client.delete(f"/items/{item_id}", name="DELETE /items/{id}")
