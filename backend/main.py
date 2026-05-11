import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from db.clients import list_clients, upsert_client, delete_client

app = FastAPI(title="The Digital Mercenary API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)


class ClientPayload(BaseModel):
    name: str 
    omgeving: int
    token_live: str
    token_test: str


@app.get("/clients")
def route_list_clients():
    return list_clients()


@app.post("/clients", status_code=201)
def route_upsert_client(payload: ClientPayload):
    upsert_client(payload.name, payload.omgeving, payload.token_live, payload.token_test)
    return {"message": f"Client '{payload.name}' saved."}


@app.delete("/clients/{name}")
def route_delete_client(name: str):
    deleted = delete_client(name)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Client '{name}' not found.")
    return {"message": f"Client '{name}' deleted."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
