from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="Ecommerce Comparison (Minimal)")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Mock store product catalogs
STORES = {
    "storeA": [
        {"id": "a1", "name": "SuperPhone X", "price": 799.99, "url": "https://storeA/product/a1"},
        {"id": "a2", "name": "Headphones Pro", "price": 199.99, "url": "https://storeA/product/a2"},
        {"id": "a3", "name": "Coffee Maker 3000", "price": 99.99, "url": "https://storeA/product/a3"},
    ],
    "storeB": [
        {"id": "b1", "name": "SuperPhone X (128GB)", "price": 749.99, "url": "https://storeB/product/b1"},
        {"id": "b2", "name": "Headphones Pro", "price": 189.00, "url": "https://storeB/product/b2"},
        {"id": "b3", "name": "Coffee Maker 3000", "price": 109.00, "url": "https://storeB/product/b3"},
    ],
    "storeC": [
        {"id": "c1", "name": "SuperPhone X", "price": 779.00, "url": "https://storeC/product/c1"},
        {"id": "c2", "name": "Headphones Pro", "price": 205.00, "url": "https://storeC/product/c2"},
    ],
}


class CompareRequest(BaseModel):
    products: List[str]
    stores: List[str]


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "stores": list(STORES.keys())})


@app.get("/api/mock/{store}")
async def mock_store(store: str):
    data = STORES.get(store)
    if data is None:
        return JSONResponse({"error": "store not found"}, status_code=404)
    return {"store": store, "products": data}


@app.post("/api/compare")
async def compare(req: CompareRequest):
    results = []
    for q in req.products:
        query = q.strip()
        candidates = []
        best = None
        for s in req.stores:
            catalog = STORES.get(s, [])
            for item in catalog:
                # naive substring matching; replace with fuzzy matching for production
                if query.lower() in item["name"].lower():
                    match = {"store": s, "id": item["id"], "name": item["name"], "price": item["price"], "url": item["url"]}
                    candidates.append(match)
                    if best is None or item["price"] < best["price"]:
                        best = match
        results.append({"query": query, "matches": candidates, "best": best})
    return {"results": results}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
