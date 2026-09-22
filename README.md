# Wi‑Fi Password Viewer (Windows)

Petit script Python qui liste les profils Wi‑Fi enregistrés sur un ordinateur Windows et affiche les détails du profil choisi. Si Windows autorise l’accès à la clé, celle-ci apparaît en clair dans les résultats.

> À utiliser uniquement sur votre propre ordinateur ou avec l’autorisation explicite de son propriétaire. Une clé Wi‑Fi affichée est une information sensible : ne la publiez pas et ne partagez pas de capture d’écran contenant cette clé.

## Fonctionnement

Le script s’appuie sur `netsh`, l’outil réseau intégré à Windows :

1. Il récupère la liste des profils Wi‑Fi enregistrés.
2. Il affiche les profils détectés et demande d’en choisir un par numéro.
3. Il affiche les détails du profil choisi avec `key=clear`. Cela peut révéler le mot de passe enregistré.

Le script reconnaît les libellés de profils en anglais et en français. L’accès à la clé dépend des droits Windows et de la configuration de la machine.

## Prérequis

- Windows avec `netsh` disponible.
- Python 3.7 ou plus récent.
- Un profil Wi‑Fi déjà enregistré sur l’ordinateur.

Aucune dépendance Python externe n’est nécessaire.

## Utilisation

Ouvrez PowerShell ou l’invite de commandes dans le dossier du script, puis lancez :

```powershell
python passwd_viewer.py
```

Choisissez le numéro correspondant au profil voulu. Les résultats s’affichent dans la console. Si la clé ne s’affiche pas, relancez le terminal avec les droits nécessaires et vérifiez que le profil est bien enregistré sur cet ordinateur.

## Sécurité et confidentialité

- N’utilisez pas ce script pour consulter les réseaux enregistrés sur l’appareil d’une autre personne sans autorisation.
- Ne publiez jamais les résultats de la commande, une capture d’écran ou un journal contenant une clé Wi‑Fi.
- Si vous partagez le dépôt, partagez uniquement le code source, jamais les mots de passe récupérés.
- Utilisez un dépôt privé si le projet contient ensuite des exemples ou des captures réelles, après avoir retiré toute donnée sensible.

## Limites

- Ce script est conçu pour Windows ; il ne fonctionne pas tel quel sur Linux ou macOS.
- Il affiche les informations disponibles pour le profil sélectionné et ne modifie pas les paramètres du réseau.
- Une saisie qui n’est pas un numéro peut interrompre le script ; choisissez un numéro affiché dans la liste.

## Licence

Ce projet est distribué sous la licence MIT. Consultez le fichier [LICENSE](LICENSE) pour le texte complet.
