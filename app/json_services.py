import json
from typing import List

def load_data(filename: str) -> List[dict]:
    """Cette fonction permet de charger les tâches à partir du fichier JSON"""
    try:
        with open(f'{filename}.json', 'r', encoding='utf-8') as f:
            return json.load(f)

    except FileNotFoundError:
        print("Erreur: le fichier n'existe pas")
    except json.JSONDecodeError as e:
        print("Erreur de format JSON", e)