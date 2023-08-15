# jogoteca-flask-alura
Curso da plataforma Alura : 
   Flask: crie um webapp com python


# Create a virtualenv
```bash
python -m venv .\venv\alura
```
# Enable virtualvenv
```bash
.\venv\alura\Scripts\Activate.ps1
```

# Install Flask
```bash
pip install flask==2.0.2
```

# Run in PowerShell
Enable variables
```bash
$env:FLASK_ENV = "development"

$env:FLASK_APP=app.py

flask run
```