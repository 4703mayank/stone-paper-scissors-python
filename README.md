
# Stone · Paper · Scissors — Python (CLI & Web)

A clean-from-scratch implementation of the classic game in **pure Python** with:
- **CLI version** (`cli.py`)
- **Reusable game logic** (`game.py`)
- **Web app** using **Streamlit** (`app.py`)

## Quickstart

### 1) Run the CLI
```bash
python cli.py
```

### 2) Run the Web App (Streamlit)
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Deploy Options

### A) Streamlit Community Cloud (easiest)
1. Push this folder to a **public GitHub repo**.
2. Go to https://share.streamlit.io (Streamlit Community Cloud).
3. Connect your GitHub repo and choose `app.py` as the entry file.
4. Deploy. You're done!

### B) Render (free web service)
1. Push to GitHub.
2. Create a **Web Service** on https://render.com.
3. Runtime: **Python 3.x**
4. Start command:
   ```bash
   streamlit run app.py --server.address 0.0.0.0 --server.port $PORT
   ```

### C) PythonAnywhere (simple for Python)
1. Upload this project or pull from GitHub.
2. Create a **Web app** and point a **WSGI** wrapper to run Streamlit via a bash script **OR** deploy the CLI version as a console app.
   - For a quick web deploy on PythonAnywhere, consider using **Flask** (not included here). Streamlit works best on Streamlit Cloud/Render.

---

## Project Structure
```
.
├─ app.py               # Streamlit web UI
├─ cli.py               # Terminal/console game
├─ game.py              # Core game logic (imported by both)
├─ requirements.txt     # Python deps
└─ README.md
```

## Notes
- The logic lives in `game.py` so tests or other UIs can reuse it.
- Customize emoji/assets freely — logic stays the same.
