# Aditya Shinde – Portfolio (Flask)
## Run in VS Code
1. Open the folder in VS Code, then open a terminal (Ctrl+`)
2. `python -m venv venv` then activate: Windows `venv\Scripts\activate` | Mac/Linux `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python app.py` → open http://127.0.0.1:5000

## Files you can replace
- Photo: `static/images/profile.jpg`
- Resume: `static/resume/Aditya_Shinde_Resume.pdf` (keep the same name, or update `resume_file` in app.py)

## Customize
- All text, skills, projects, education and links: the `PORTFOLIO` dict in `app.py`
- Colors: the `:root` variables at the top of `static/css/style.css`
- Project GitHub links: add a `github` key to a project in app.py and use it in `templates/index.html`
