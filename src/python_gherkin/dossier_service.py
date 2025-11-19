from python_gherkin.dossier_data import Dossier, DossierStatus, insert_dossier, select_dossier_by_id, select_dossiers_by_status, update_dossier_status
from uuid import UUID, uuid4


def create_dossier(summary: str) -> UUID:
    dossier = Dossier(
        id=uuid4(),
        summary=summary,
        status=DossierStatus.CREATED
    )

    insert_dossier(dossier)

    return dossier.id

def update_summary(id: UUID, summary: str):
    dossier = select_dossier_by_id(id)
    if dossier.status != DossierStatus.CREATED:
        raise Exception("Impossible de modifier un dossier qui n'est pas en édition")
    dossier.summary = summary

def submit_dossier(id: UUID) -> None:
    if select_dossier_by_id(id).status == DossierStatus.SUBMITTED:
        raise Exception("Impossible de soumettre le dossier à nouveau.")
    update_dossier_status(id, DossierStatus.SUBMITTED)


def read_submitted_dossiers() -> list[Dossier]:
    return select_dossiers_by_status(DossierStatus.SUBMITTED)


def get_dossier(id: UUID) -> Dossier:
    return select_dossier_by_id(id)