import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows


@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows 


@app.get("/cursosPlatzi")
def get_cursos():
    rows = ["Docker", "Bash", "Flash", "Linux", "Ingles", "Python", "JS"]
    return rows 

@app.get("/cursosBen")
def get_cursos_Ben():
    rows = ["Docker", "Bash", "Flash", "Linux", "Ingles", "Python", "JS"]
    return rows 