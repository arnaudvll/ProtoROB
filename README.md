# Projet de Porte à Reconnaissance Faciale

## Description du Projet

Nous formons une équipe composée de trois étudiants de CPE Lyon : Adrien Pouxviel, Arnaud Ville, et Clément Poirié. Notre objectif consiste à concrétiser le prototype d'une solution conformément à une liste de matériaux et de consignes prédéfinies.

La liste des éléments à utiliser se présente comme suit :

- Mise en œuvre d'une ESP32
- Intégration d'un capteur de distance
- Utilisation d'un moteur dynamixel
- Programmation avec le middleware ROS2
- Développement d'une application mobile

La durée allouée pour la réalisation de ce projet s'est étendue sur une période de 20 heures. Notre démarche consiste à élaborer une porte munie d'un système de reconnaissance faciale, permettant ainsi l'accès exclusif aux individus autorisés. La reconnaissance faciale constitue le mécanisme d'authentification nécessaire au déverrouillage de la porte. En outre, nous avons incorporé des fonctionnalités telles que le mode d'ouverture par détection de présence et le mode d'ouverture par commande via téléphone.

## Fonctionnalités

- **Reconnaissance Faciale :** Mise en œuvre d'un algorithme de reconnaissance faciale visant à identifier de manière précise les individus autorisés.
- **Capteur de Distance :** Intégration d'un capteur permettant de déterminer la présence ou l'absence d'une personne devant la porte.
- **Application Mobile IHR :** Conception d'une application mobile agissant en tant qu'interface homme-machine. Elle offre la possibilité d'ouvrir et de fermer la porte à distance, de visualiser en streaming le flux de la caméra, et de modifier le mode d'ouverture entre la reconnaissance faciale et la détection de présence.


## Technologies Utilisées

- **Langage de Programmation :** Python et arduino
- **Middleware :**  ROS2 humble
- **Bibliothèques :**
    - OpenCV pour la capture d'images et le traitement d'images.
    - face_recognition pour la détection et la reconnaissance faciale.

- **Matériel :**
    - Une caméra
    - Une plaque de PVC redimensionnée spécifiquement pour la création de la porte.
    - Des charnières élaborées et imprimées par nos soins à l'aide d'une imprimante 3D.
    - Un capteur de distance VL53L0X-V2.
    - Un moteur dynamixel Ax12.
    - Des legos 

## Le système

## Résultats