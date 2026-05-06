import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except:
        return []


def salvar_tarefas(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            lista,
            arquivo,
            ensure_ascii=False,
            indent=4
        )