from typing import List, Dict, Any


def get_ods_themes() -> List[Dict[str, Any]]:
    return [
        {
            "number": 1,
            "name": "Fin de la pobreza",
            "color": "#E5243B",
            "slogan": "Poner fin a la pobreza en todas sus formas",
        },
        {
            "number": 2,
            "name": "Hambre cero",
            "color": "#DDA63A",
            "slogan": "Poner fin al hambre",
        },
        {
            "number": 3,
            "name": "Salud y bienestar",
            "color": "#4C9F38",
            "slogan": "Garantizar una vida sana",
        },
        {
            "number": 4,
            "name": "Educación de calidad",
            "color": "#C5192D",
            "slogan": "Educación inclusiva y de calidad",
        },
        {
            "number": 5,
            "name": "Igualdad de género",
            "color": "#FF3A21",
            "slogan": "Lograr la igualdad de género",
        },
        {
            "number": 6,
            "name": "Agua limpia y saneamiento",
            "color": "#26BDE2",
            "slogan": "Agua y saneamiento para todos",
        },
        {
            "number": 7,
            "name": "Energía asequible y no contaminante",
            "color": "#FCC30B",
            "slogan": "Energía limpia y asequible",
        },
        {
            "number": 8,
            "name": "Trabajo decente y crecimiento económico",
            "color": "#A21942",
            "slogan": "Trabajo decente para todos",
        },
        {
            "number": 9,
            "name": "Industria, innovación e infraestructura",
            "color": "#FD6925",
            "slogan": "Industria e innovación",
        },
        {
            "number": 10,
            "name": "Reducción de las desigualdades",
            "color": "#DD1367",
            "slogan": "Reducir la desigualdad",
        },
        {
            "number": 11,
            "name": "Ciudades y comunidades sostenibles",
            "color": "#FD9D24",
            "slogan": "Ciudades sostenibles",
        },
        {
            "number": 12,
            "name": "Producción y consumo responsables",
            "color": "#BF8B2E",
            "slogan": "Consumo responsable",
        },
        {
            "number": 13,
            "name": "Acción por el clima",
            "color": "#3F7E44",
            "slogan": "Acción por el clima",
        },
        {
            "number": 14,
            "name": "Vida submarina",
            "color": "#0A97D9",
            "slogan": "Proteger la vida submarina",
        },
        {
            "number": 15,
            "name": "Vida de ecosistemas terrestres",
            "color": "#56C02B",
            "slogan": "Proteger la vida terrestre",
        },
        {
            "number": 16,
            "name": "Paz, justicia e instituciones sólidas",
            "color": "#00689D",
            "slogan": "Paz e inclusión",
        },
        {
            "number": 17,
            "name": "Alianzas para lograr los objetivos",
            "color": "#19486A",
            "slogan": "Alianzas para el desarrollo",
        },
    ]


def get_theme(theme_id: int) -> Dict[str, Any]:
    for theme in get_ods_themes():
        if theme["number"] == theme_id:
            return theme
    raise ValueError(f"ODS {theme_id} no encontrado")
