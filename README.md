# python-gherkin

Ce projet est un exemple d'utilisation de behave (cucumber) en python.

Présentation disponible [ici](https://www.figma.com/slides/1ZP1nLztSxddvMicJYEEFw/Gherkin?node-id=1-705&t=1HLsq5X7AVcTuKyZ-1)


## Installer le projet

### Pré-requis
### Pré-requis

Pour travailler sur ce projet, vous aurez besoin de Python et d'un gestionnaire de dépendances. Les instructions ci-dessous sont écrites pour Windows (PowerShell), mais s'appliquent de façon similaire sur macOS/Linux en adaptant les commandes de shell.

- Python 3.12 ou supérieur
	- Installez Python depuis https://www.python.org/downloads/ (ou via le Microsoft Store). Lors de l'installation sur Windows, cochez "Add Python to PATH" ou utilisez l'exécutable Python explicite.
	- Vérifier l'installation :

		```powershell
		python --version
		```

- PDM (recommandé) — gestionnaire de dépendances moderne basé sur pyproject.toml
	- Recommandé : installer PDM via pipx pour une installation isolée :

		```powershell
		python -m pip install --user pipx; python -m pipx ensurepath
		# Fermez et rouvrez votre terminal PowerShell si nécessaire
		pipx install pdm
		```

	- Alternative (si vous ne voulez pas utiliser pipx) :

		```powershell
		python -m pip install --user pdm
		```

	- Vérifier PDM :

		```powershell
		pdm --version
		```

- Optionnel — si vous ne pouvez pas utiliser PDM
	- Créez un environnement virtuel classique et utilisez pip :

		```powershell
		python -m venv .venv
		.\.venv\Scripts\Activate.ps1
		pip install -r requirements.txt   # si le projet fournit un requirements.txt
		```

	Note : ce projet utilise `pyproject.toml` et est conçu pour PDM. Si vous utilisez la méthode pip/venv, certaines commandes ou workflows décrits ici devront être adaptés manuellement.

- Remarques et dépannage rapide
	- Après `pipx ensurepath`, redémarrez PowerShell pour que les chemins prennent effet.
	- Si `pdm sync` échoue, essayez `pdm install` ou vérifier la connexion réseau et le contenu de `pyproject.toml`.
	- Commandes utiles pour vérifier l'environnement :

		```powershell
		python --version
		pdm --version
		pdm info   # affiche des informations sur l'environnement PDM
		```

Avec ces pré-requis en place vous pourrez ensuite suivre la section "Cloner le projet" et exécuter `pdm sync` pour installer les dépendances définies dans `pyproject.toml`.

### Cloner le projet
`git clone https://github.com/ByAlexCod/python-cucumber-sample`

### Installer les packages
`pdm sync`

### Lancer les tests cucumber
`pdm run behave`

Cette commande lancera les tests écrit en cucumber qui sont présents dans ./features/*