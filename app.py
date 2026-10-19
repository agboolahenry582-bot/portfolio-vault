from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Portfolio Vault - Agboola Henry</title>
<style>
body{font-family:Arial;background:#0f172a;color:#e2e8f0;margin:0;padding:0}
header{background:#1e293b;padding:40px;text-align:center}
h1{color:#38bdf8;margin:0;font-size:42px}
p.sub{color:#94a3b8;margin-top:10px}
.container{max-width:900px;margin:40px auto;padding:20px}
.card{background:#1e293b;border-radius:12px;padding:25px;margin-bottom:20px;border:1px solid #334155}
h2{color:#38bdf8}
a.btn{display:inline-block;background:#38bdf8;color:#000;padding:12px 20px;border-radius:8px;text-decoration:none;font-weight:bold;margin-top:15px}
a.btn:hover{background:#0ea5e9}
.footer{text-align:center;color:#64748b;padding:30px}
</style>
</head>
<body>
<header>
<h1>Portfolio Vault</h1>
<p class="sub">Agboola Henry - Projects | Skills | Achievements</p>
</header>
<div class="container">
<div class="card">
<h2>About Me</h2>
<p>Welcome to my Portfolio Vault! I'm a passionate developer building secure and scalable web applications. This vault contains my best works.</p>
<a class="btn" href="https://github.com/agboolahenry582-bot">View My GitHub</a>
</div>
<div class="card">
<h2>Projects</h2>
<p>✔ Portfolio Vault - Secure Flask App</p>
<p>✔ Deployed on Render / Heroku</p>
<p>✔ Built with Python, Flask, Gunicorn</p>
</div>
<div class="card">
<h2>Contact</h2>
<p>Email: agboolahenry582@gmail.com</p>
<p>GitHub: agboolahenry582-bot</p>
</div>
</div>
<div class="footer">© 2026 Agboola Henry - Portfolio Vault</div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
