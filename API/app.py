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

@app.get("/superheroesMarvel")
def get_superheroes_marvel():
    rows = ["Ironman", "Thor", "Hulk", "Capitan America", "Viuda Negra", "Doctor Strange", "Antman", "SpiderMan"]
    return rows

@app.get("/cursosPlatzi")
def get_cursos_platzi():
    rows = ["Backend", "Frontend", "Data Science", "Machine Learning", "Deep Learning", "Python", "JavaScript"]
    return rows


