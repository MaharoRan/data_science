
# Analyse de la Productivité des Employés : Impact des Réseaux Sociaux et du Style de Vie

## Contexte du Projet

Avec la généralisation du télétravail et l'omniprésence des réseaux sociaux, les employés passent une partie significative de leur journée connectés à différentes plateformes numériques. Si ces outils peuvent parfois favoriser la communication et la créativité, ils peuvent aussi devenir une source de distraction impactant directement la performance au travail.

Cette étude vise à identifier les facteurs de baisse de performance des salariés en analysant leur productivité réelle à partir de leurs habitudes de travail, leur temps consacré aux réseaux sociaux, leur mode de vie et leur type de métier.

## Problématique

### Problématique Métier

Comment prédire le niveau de productivité des employés à partir de leurs habitudes et leur style de vie ?

### Problématique ML (Non Supervisé)

L'analyse des clusters d'employés montre que la productivité réelle, la perception de productivité et la satisfaction au travail varient fortement entre les groupes, contrairement aux autres variables. Cela soulève la question : comment la satisfaction et la perception de productivité influencent-elles la productivité réelle ?

## Dataset : social_media_vs_productivity

Le dataset comprend 18 variables :

**Variables démographiques et professionnelles**

- `age` : Âge des salariés
- `gender` : Genre
- `job_type` : Type de métier
- `work_hours_per_day` : Temps de travail quotidien

**Variables réseaux sociaux**

- `daily_social_media_time` : Temps quotidien sur les réseaux sociaux
- `social_platform_preference` : Réseau social préféré
- `number_of_notifications` : Notifications reçues par jour
- `weekly_offline_hours` : Heures déconnectées par semaine

**Variables productivité**

- `perceived_productivity_score` : Sentiment de productivité
- `actual_productivity_score` : **Productivité réelle (variable cible)**
- `job_satisfaction_score` : Satisfaction au travail
- `stress_level` : Niveau de stress
- `days_feeling_burnout_per_month` : Jours de burnout par mois

**Variables style de vie**

- `sleep_hours` : Temps de sommeil quotidien
- `screen_time_before_sleep` : Temps d'écran avant de dormir
- `breaks_during_work` : Nombre de pauses au travail
- `uses_focus_apps` : Utilisation d'apps de concentration
- `coffee_consumption_per_day` : Cafés consommés par jour

## Modèles Utilisés

### Modèles Supervisés (Régression)

**Random Forest Regressor**

- Algorithme d'ensemble basé sur des arbres de décision
- Excellente capacité à capturer les relations non-linéaires
- Robuste face aux outliers

**Gradient Boosting Regressor**

- Méthode d'ensemble séquentielle
- Optimisation itérative des erreurs
- Haute précision sur datasets complexes

**Support Vector Regressor (SVR)**

- Approche géométrique de la régression
- Efficace en haute dimension

### Modèle Non Supervisé

**KMeans Clustering**

- Segmentation des employés en groupes homogènes
- Identification de profils types selon leurs habitudes

## Performance des Modèles

### Random Forest - Exemple de Prédiction

```json
Input:
{
  "age": 36,
  "gender": "Female",
  "job_type": "Education",
  "daily_social_media_time": 4.089168,
  "social_platform_preference": "Twitter",
  "number_of_notifications": 49,
  "work_hours_per_day": 6.560467,
  "perceived_productivity_score": 2.681830,
  "stress_level": 4.0,
  "sleep_hours": 6.325507,
  "screen_time_before_sleep": 0.747998,
  "breaks_during_work": 4,
  "coffee_consumption_per_day": 4,
  "days_feeling_burnout_per_month": 29,
  "weekly_offline_hours": 8.419648,
  "job_satisfaction_score": 3.444376
}

Output:
{
    "prediction_actual_productivity_score": 2.738151278388584
}
```

**Valeur réelle** : 2.446927
**Erreur absolue** : 0.29

L'erreur de 0.29 démontre une précision satisfaisante pour une utilisation en production.

## Conclusions Métier

### Découvertes Principales

L'étude révèle que les employés les plus satisfaits sont également ceux qui se perçoivent comme les plus productifs et qui présentent la productivité réelle la plus élevée. Les autres variables (temps sur réseaux sociaux, notifications, heures de travail) n'apportent pas de différence significative entre les groupes.

Pour améliorer la performance globale, il est crucial de se concentrer sur la satisfaction et la perception de productivité. Cela suggère que les actions visant à augmenter le bien-être et la satisfaction des employés peuvent directement accroître leur productivité réelle.

### Recommandations

**Pour les RH**

- Privilégier les initiatives augmentant la satisfaction au travail
- Développer des programmes de reconnaissance
- Créer un environnement favorisant la perception positive de contribution

## Déploiement de l'API

### Lancement

(lancer dans 3 terminals)

```bash
uvicorn api_random_forest:app --reload --port 8000
uvicorn api_gradient_boosting:app --reload --port 8001
uvicorn api_svr:app --reload --port 8002
```

### Utilisation

**Endpoint** : `POST /predict`

L'API accepte les 17 variables explicatives en JSON et retourne la prédiction de productivité.

## Technologies

- **Python** : Langage principal
- **Scikit-learn** : Modèles ML
- **Pandas / NumPy** : Manipulation de données
- **FastAPI** : API REST
- **Uvicorn** : Serveur ASGI
- **Matplotlib / Seaborn** : Visualisation

## Méthodologie

1. **EDA** : Analyse statistique, visualisations, corrélations
2. **Preprocessing** : Traitement des valeurs manquantes, encodage, normalisation
3. **Modélisation** : Entraînement, validation croisée, optimisation
4. **Évaluation** : Métriques (RMSE, MAE, R²), feature importance
5. **Déploiement** : API REST avec documentation Swagger

   **Note** : Cette analyse démontre que l'amélioration de la productivité passe d'abord par l'amélioration du bien-être et de la satisfaction des employés, plutôt que par des mesures restrictives sur l'utilisation des outils numériques
