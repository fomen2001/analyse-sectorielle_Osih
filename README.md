# analyse-sectorielle_Osih
Projet 2 – Analyse sectorielle prédictive
Segmentation et prévision de la demande – Olist
1. Formulation de la problématique
Ce projet s’inscrit dans le secteur du e-commerce, caractérisé par des volumes de données transactionnelles importants, une forte concurrence et des enjeux majeurs de fidélisation client. Les données Olist sont relationnelles, temporelles et orientées comportement client.

Problématique :
Comment segmenter les clients de la plateforme Olist à partir de leurs comportements d’achat et prédire l’évolution du chiffre d’affaires et de la demande par segment afin d’optimiser les décisions marketing et commerciales ?
2. Structuration et exploration des données
Les données proviennent de plusieurs fichiers CSV interconnectés : clients, commandes, produits, paiements et avis.

Étapes clés :
- Jointure des tables via les clés métier
- Nettoyage des valeurs manquantes et aberrantes
- Conversion des dates et création de variables temporelles
- Analyse exploratoire : saisonnalité, géographie, satisfaction client, délais de livraison
3. Construction de modèles prédictifs
Segmentation client :
- Construction de variables agrégées (RFM, panier moyen, délai, satisfaction)
- Clustering via K-Means et DBSCAN

Modélisation supervisée :
- Régression pour prédire le chiffre d’affaires
- Classification pour identifier les clients à forte valeur

Séries temporelles :
- Modèle VAR pour anticiper l’évolution de la demande par segment
4. Analyse sectorielle et interprétation métier
Analyse des facteurs influents sur la valeur client et la performance du e-commerce : logistique, satisfaction, catégories produits et comportements de paiement.

Les résultats des modèles sont interprétés à l’aide de métriques de performance et de visualisations orientées métier.
5. Recommandations stratégiques
Les recommandations visent à améliorer la rentabilité et la fidélisation client :
- Ciblage marketing par segment
- Optimisation logistique pour les segments sensibles aux délais
- Actions de réactivation des clients à risque
- Mise en place de tableaux de bord décisionnels


1) Comment expliquer tes modèles (structure “jury + métier”)

Pour chaque modèle, tu peux suivre ce canevas (toujours le même) :

Objectif (quoi je prédis ? pourquoi c’est utile ?)

Entrées (features) (quelles variables expliquent la décision ?)

Modèle (algorithme + raison du choix)

Métriques (comment j’évalue ?)

Résultats (performance + limites)

Interprétation (quels facteurs influencent ?)

Décision métier (que faire concrètement ?)

2) Interpréter les sorties (régression, classification, clustering, VAR)
A) Régression (ex : prédire monetary / CA)

À dire :

RMSE = erreur moyenne en “€” (ou unité monétaire)

MAE = erreur moyenne “simple”

R² = part de variance expliquée

Interprétation utilisateur :

“Ton CA attendu est X, avec une incertitude moyenne ~RMSE”

“Les facteurs qui augmentent le CA : fréquence ↑, panier moyen ↑, récence ↓…”

B) Classification (ex : high_value)

À dire :

F1 = compromis precision/recall

ROC-AUC = capacité de tri global

Interprétation utilisateur :

“Probabilité d’être high-value = p”

“Seuil de décision : 0.5 (ou optimal)”

“Pourquoi : fréquence élevée, récence faible, panier élevé…”

C) Clustering (segmentation)

À dire :

Silhouette / DBI = qualité géométrique

Mais le vrai résultat = profil métier des segments

Interprétation utilisateur :

Segment = “VIP / à risque / opportunité / insatisfaits”

Actions recommandées par segment

D) VAR (prévisions multivariées)

À dire :

modèle pour prévoir plusieurs variables inter-dépendantes

utile pour anticiper “CA + volume + délais” par segment

Interprétation utilisateur :

prévision CA/commandes sur 3 mois