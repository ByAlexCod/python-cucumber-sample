from dataclasses import dataclass
from enum import Enum, auto
from uuid import UUID, uuid5


class DossierStatus(Enum):
    CREATED = auto()
    SUBMITTED = auto()

@dataclass
class Dossier():
    id: UUID
    summary: str
    status: DossierStatus 

dossiers: list[Dossier] = []

def insert_dossier(dossier: Dossier):
    dossiers.append(dossier)

def select_dossier_by_id(id: UUID):
    return next(dossier for dossier in dossiers if dossier.id == id)

def update_dossier_status(id: UUID, new_status: DossierStatus) -> Dossier:
    next(dossier for dossier in dossiers if dossier.id == id).status = new_status

def select_dossiers_by_status(status: DossierStatus) -> list[Dossier]:
    return [dossier for dossier in dossiers if dossier.status == status]