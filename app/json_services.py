import json
import os 
from typing import List

def load_data(filename: str) -> List[dict]:
    """Cette fonction permet de charger les tâches à partir du fichier JSON"""
    if not os.path.exists(filename):
        return []
    
    try:
        with open(f'{filename}', 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print("Erreur de format JSON. ", e)


def save_data(filename: str, data: List[dict]) -> None:
    try:
        with open(f"{filename}", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except FileExistsError:
        print("Erreur: le fichier n'existe pas")