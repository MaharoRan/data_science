
Contexte:
Avec la généralisation du télétravail et l’omniprésence des réseaux sociaux, les employés passent une partie significative de leur journée connectés à différentes plateformes numériques. Si ces outils peuvent parfois favoriser la communication et la créativité, ils peuvent aussi devenir une source de distraction.
Cette étude vise à identifier les facteurs de baisse de performance des salariés d'une entreprise. Elle analyse leur performance réelle en s'appuyant sur leurs habitudes au travail, leur temps consacré aux réseaux sociaux, leur mode de vie et leur type de métier.

Dataset:
Elle s'appuye sur le dataset social_media_vs_productivity, qui possède ces colonnes:
 0   age                             age des salariés
 1   gender                          leur genre
 2   job_type                        leir type de métier
 3   daily_social_media_time         le temps qu'ils passent sur les réseaux sociaux
 4   social_platform_preference      leur réseau social préféré
 5   number_of_notifications         leur nombre de notifications reçues par jour
 6   work_hours_per_day              leur temps de travail quotidien
 7   perceived_productivity_score    leur sentiment de productivité
 8   actual_productivity_score       leur productivité réelle
 9   stress_level                    leur niveau de stress
 10  sleep_hours                     leur temps de sommeil quotidien
 11  screen_time_before_sleep        leur temps de scroll avant de dormir quotidien
 12  breaks_during_work              leur nombre de pauses au travail
 13  uses_focus_apps                 leur utilisation ou non d'applications qui aident à se concentrer
 14  coffee_consumption_per_day      le nombre de café qu'ils boivent par jour
 15  days_feeling_burnout_per_month  leur nombre de jours ressentis en burnout par mois
 16  weekly_offline_hours            leur nombre d'heures deconnectés de tous résseaux par semaine
 17  job_satisfaction_score          leur satisfaction au travail

 Modèles utiliséset pré-entrainés dans l'EDA:
 Supervisés: -Random Forest
             -Graident Boosting Regressor
             -Support Vector Regressor
Non supervisé: -KMeans

Problématique métier: Comment prédire le niveau de productivité des employés à partir de leurs habitudes et leur style de vie?

Problématique ML non supervisé(Clustering): Segmentation selon des profils
L’analyse des clusters d’employés montre que la productivité réelle, la perception de productivité et la satisfaction au travail varient fortement entre les groupes, contrairement aux autres variables. Cela soulève la question suivante : comment la satisfaction et la perception de productivité influencent-elles la productivité réelle?

Conclusion métier:
L’étude révèle que les employés les plus satisfaits sont également ceux qui se perçoivent comme les plus productifs et qui présentent la productivité réelle la plus élevée. Les autres variables n’apportent pas de différence significative entre les groupes. Ainsi, pour segmenter efficacement les profils et améliorer la performance globale, il est crucial de se concentrer sur la satisfaction et la perception de productivité. Cela suggère que les actions visant à augmenter le bien-être et la satisfaction des employés peuvent directement accroître leur productivité réelle.

API:
Pour lancer l'api RandomForest: uvicorn api_random_forest:app --reload 

Test Random Forest:
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
{
    "prediction_actual_productivity_score": 2.738151278388584
}
Le vrai actual_productivity_score: 2.446927
Donc pour Random Forest, la différence d'erreur pour cette prédiction est 0,29. C'est assez précis.