"""Standalone demo: fixed sample data, no persistence or external services."""
from flask import Flask, jsonify, render_template

app = Flask(__name__)
SOURCE = "events"
VERSION = "1.0.1"


@app.get("/healthz")
def health():
    """Identify this demo without exposing host, environment, or credentials."""
    return jsonify(status="ok", source=SOURCE, version=VERSION, synthetic=True)

ROWS = [
    {
        "label": "Synchronisation",
        "value": "09:10",
        "detail": "Exemple : source récupérée"
    },
    {
        "label": "Déploiement",
        "value": "09:12",
        "detail": "Exemple : application démarrée"
    },
    {
        "label": "Contrôle",
        "value": "09:13",
        "detail": "Exemple : vérification réussie"
    }
]


@app.get("/")
def home():
    """Render a visibly distinct demo for this Git source."""
    return render_template(
        "index.html", title="Demo Events", source=SOURCE,
        version=VERSION, accent="#ffbc73", description='Un journal d’événements, fourni par un second dépôt Git.', rows=ROWS,
    )
