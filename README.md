# Ecommerce Comparison App (Minimal)

This repository contains a minimal ecommerce comparison app: a FastAPI backend with a small frontend served via Jinja2 templates. It demonstrates comparing product prices across mock stores and can be extended to fetch real store data.

Quick start

1. Create a Python virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the app:

```bash
uvicorn main:app --reload
```

3. Open http://127.0.0.1:8000 in your browser.

What is included

- `main.py` — FastAPI backend with mock store endpoints and a compare API.
- `templates/index.html` — simple frontend to enter product names and choose stores to compare.
- `static/style.css` — small stylesheet.
- `requirements.txt` — Python dependencies.

Next steps

- Hook real store APIs or scrapers for live pricing.
- Add authentication and user-saved watchlists.
- Add product image matching and fuzzy matching improvements.

If you want, I can also scaffold a React frontend or add Docker support next.
# ecommerce-comparison-app
