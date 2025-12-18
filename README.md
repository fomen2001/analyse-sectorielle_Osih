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
