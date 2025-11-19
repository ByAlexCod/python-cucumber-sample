# language: fr

Fonctionnalité: Soumission d'un dossier
    Suite à l'écriture d'un dossier, l'utilisateur veut soumettre son dossier à un workflow de validation.

    Scénario: Soumettre un dossier change son état
        Etant donné un dossier rempli par un utilisateur A
        Quand L'utilisateur A soumet son dossier
        Alors Le dossier est visible dans la liste des dossiers à valider pour l'utilisateur B

    Scénario: Impossible de resoumettre un dossier
        Etant donné un dossier rempli par un utilisateur A
        Et un dossier soumis par l'utilisateur A
        Quand L'utilisateur A soumet son dossier
        Alors une erreur survient

    Scénario: Modification du sommaire
        Etant donné un dossier rempli par un utilisateur A
        Quand L'utilisateur A modifie le sommaire du dossier avec "SuperMotivation"
        Alors Le sommaire du dossier est "SuperMotivation"

    Scénario: Modification du sommaire sur un dossier déjà soumis
        Etant donné un dossier rempli par un utilisateur A
        Et un dossier soumis par l'utilisateur A
        Quand L'utilisateur A modifie le sommaire du dossier avec "SuperMotivation"
        Alors une erreur survient