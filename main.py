from contextlib import asynccontextmanager

from pydantic import BaseModel

from fastapi import FastAPI

from client.client import MCPClient

mcp_client = {}
SERVER_FILE_PATH = "./server/server.py"

@asynccontextmanager
async def lifespan(app: FastAPI):
    mcp_client["client"] = MCPClient()
    await mcp_client["client"].connect_to_server(SERVER_FILE_PATH)
    yield
    await mcp_client["client"].cleanup()

app = FastAPI(lifespan=lifespan)

class QueryModel(BaseModel):
    query: str

@app.post("/query-response")
async def process_query(inp: QueryModel):
    response = await mcp_client["client"].process_query(query=inp.query)
    return {
        "response": response
    }
