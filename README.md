# Mes dîners malins

Une appli perso de menus de la semaine, sur le principe de Pimzi.

- **Mon profil** : un quiz en 9 étapes (magasin, nombre de repas et budget, régime, lactose, allergies, aliments détestés, type de repas et de cuisine, vibe, matériel, temps et niveau).
- **Dîners / Déjeuners / P'tit déj** : l'algorithme garde seulement les recettes compatibles, favorise celles qui collent à tes envies, puis remplace les plus chères jusqu'à passer sous le budget. Bouton « Changer » sur chaque repas.
- **Courses** : liste par rayon, paquets entiers à acheter, prix du magasin choisi, cases à cocher, copie de la liste, prix modifiables.

Les prix sont des estimations (prix de base × indice du magasin) : corrige-les dans « Ajuster les prix ».
Les illustrations sont dessinées automatiquement à partir des ingrédients de chaque recette.
Tout est enregistré dans le navigateur de l'appareil.

## Utiliser
Ouvre `index.html` dans un navigateur, ou active GitHub Pages (Settings → Pages).

## Modifier
Tout est dans `app.html` : `MAGASINS`, `PRODUITS` (fonction `p(...)`), `RECETTES` (quantités pour 1 personne).
Après une modification, lance `python3 build.py` pour régénérer `index.html`.
