import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

# Chemin du modèle RandomForest
MODEL_PATH = "random_forest_california.pkl"
model = joblib.load(MODEL_PATH)

# Appel de FastAPI pour créer l'API de prédiction de productivité des salariés
app = FastAPI(title="Productivity Prediction API", version="1.0")

# Définition du modèle de données pour les fonctionnalités d'entrée de l'API
class ProductivityFeatures(BaseModel):
    age: float = Field(..., description="Age du salarié")
    gender: str = Field(..., description="Genre du salarié(Homme ou Femme)")
    job_type: str = Field(..., description="Type de job du salarié")
    daily_social_media_time: float = Field(..., description="Temps quotidien passé sur les réseaux sociaux(en heures)")
    social_platform_preference: str = Field(..., description="Préférence de plateforme sociale du salarié")
    number_of_notifications: int = Field(..., description="Nombre de notifications quotidiennes du salarié")
    work_hours_per_day: float = Field(..., description="Nombre d'heures de travail quotidiennes du salarié")
    perceived_productivity_score: float = Field(..., description="Score perçu de productivité du salarié")
    stress_level: float = Field(..., description="Niveau de stress du salarié")
    sleep_hours: float = Field(..., description="Nombre d'heures de sommeil du salarié")
    screen_time_before_sleep: float = Field(..., description="Temps d'écran avant de dormir du salarié(en heures)")
    breaks_during_work: int = Field(..., description="Nombre de pauses pendant le travail du salarié")
    coffee_consumption_per_day: int = Field(..., description="Consommation de café par jour du salarié(en tasses)")
    days_feeling_burnout_per_month: int = Field(..., description="Nombre de jours ressentant du burnout par mois du salarié")
    weekly_offline_hours: float = Field(..., description="Nombre d'heures hebdomadaires passées hors ligne du salarié")
    job_satisfaction_score: float = Field(..., description="Score de satisfaction au travail du salarié")

# Requete pour vérifier que l'API est opérationnelle
@app.get("/productivity")
def productivity():
    return {"status": "ok"}

# Requete pour la prédiction du score dz productivité réel du salarié
@app.post("/predict")
def predict(payload: ProductivityFeatures):
    X = pd.DataFrame([payload.model_dump()])
    y_pred = model.predict(X)[0]

    return {
        "prediction_actual_productivity_score": float(y_pred)
    }