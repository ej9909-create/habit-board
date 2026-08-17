# 🌟 Kids' Habit Board

A printable / tap-to-mark weekly habit board for young children. Positive acts earn a
green 👍, negatives a red 👎. One board = one week, grouped by time of day, with a reward
tally, printing, a scan-to-fill-from-photo flow, and week-by-week history.

The whole app is a **single self-contained HTML page** (`static/habit-board.html`) — plain
HTML/CSS/JS, no backend. All data is stored **privately in the visitor's own browser**
(localStorage + IndexedDB); nothing is uploaded. This Streamlit wrapper simply hosts that
page so it can be shared via a URL.

## Why a static file + iframe?
The app relies on `localStorage` and `IndexedDB`. Inlining the HTML into a component runs it
in an opaque-origin frame where IndexedDB can fail. Serving it as a **static file** gives it a
real origin, so storage works. See `streamlit_app.py`.

## Run locally
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```
Then open http://localhost:8501

## Deploy on Streamlit Community Cloud
1. Push this folder to a GitHub repo.
2. Go to https://share.streamlit.io → **Create app** → pick this repo.
3. Main file path: `streamlit_app.py`. Click **Deploy**.
4. Share the resulting `https://<name>.streamlit.app` link.

`.streamlit/config.toml` already enables static file serving (`enableStaticServing = true`),
which is required for the board to load.

## Files
| File | Purpose |
|---|---|
| `streamlit_app.py` | Streamlit host — embeds the board via an iframe |
| `static/habit-board.html` | **The app** (self-contained). Edit this to change the board. |
| `.streamlit/config.toml` | Enables static serving + theme |
| `requirements.txt` | Pinned Streamlit version |
| `habit-board.html` | Identical standalone copy (open directly in a browser, no server) |

> Editing the board: change `static/habit-board.html` (keep `habit-board.html` in sync if you
> want the standalone download to match).

## Note on data & feedback
Each tester's data lives in **their own browser on their own device** — great for privacy, but
it means data does not sync between devices or between testers. Testers can use the app's
**⚙️ Settings → Export / Import** backup to move their data. For shared/cloud data you'd need a
backend (not included).
