Voici une reformulation des phrases pour votre fichier README :

---

J'ai développé deux fonctions afin de faciliter la gestion des noms de fichiers. Dans la vie quotidienne, il est souvent nécessaire de supprimer certaines chaînes de caractères des noms de fichiers, surtout lorsque ces derniers sont trop longs.

Les fonctions sont disponibles dans le fichier file_management.ipynb. Voici une description de chacune d'entre elles :

**1. `supp_prefix(chemin_dossier, chaine_a_supprimer)`**

Cette fonction permet de supprimer une chaîne de caractères spécifique du début des noms de fichiers dans un dossier donné. Elle prend deux paramètres :
- Le premier paramètre est le chemin du dossier où vous souhaitez effectuer les modifications de fichiers.
- Le second paramètre est la chaîne de caractères à supprimer du début du nom de fichier.

Par exemple :
```python
supp_prefix('./', 'screen-capture')
```
Cette commande cible les fichiers dans le dossier './' et supprime la chaîne 'screen-capture' du début de chaque nom de fichier. Pour cela, elle utilise la méthode de découpage (slicing) du nom de fichier en fonction de la longueur de la chaîne à supprimer.

**2. `supp_string(chemin_dossier, chaine_a_supprimer)`**

Cette fonction fonctionne de manière similaire à `supp_prefix()`, mais elle supprime la chaîne de caractères spécifiée où qu'elle se trouve dans le nom du fichier. Encore une fois, elle prend deux paramètres :
- Le premier paramètre est le chemin du dossier où vous souhaitez effectuer les modifications de fichiers.
- Le second paramètre est la chaîne de caractères à supprimer du nom de fichier.

Par exemple :
```python
supp_string('./', 'example')
```
Cette commande supprime toutes les occurrences de la chaîne 'example' dans le nom de chaque fichier du dossier spécifié.

--- 

J'ai simplifié et clarifié les descriptions des fonctions pour aider les utilisateurs à comprendre leur fonctionnement et leur utilité.
