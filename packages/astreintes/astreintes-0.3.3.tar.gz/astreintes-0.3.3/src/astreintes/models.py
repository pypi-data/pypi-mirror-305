from typing import Optional, Literal
from pydantic import BaseModel, conint, NonNegativeInt, PositiveInt

N_SEMAINES = 52
MAX_ASTREINTES = 13

# todo test sum(site.n_rotation) >= min_aga + min_respi


class Parametres(BaseModel):
    max_astreintes: conint(ge=0, le=N_SEMAINES) = MAX_ASTREINTES
    min_aga: Optional[NonNegativeInt] = 1
    min_respi: Optional[NonNegativeInt] = 1
    n_iter_shuffle: Optional[PositiveInt] = 10_000
    seed: Optional[int] = None


class Site(BaseModel):
    nom: str
    rotations: PositiveInt
    aga: NonNegativeInt
    respi: NonNegativeInt


class Technicien(BaseModel):
    nom: str
    specialite: Literal['aga', 'respi']
    site: str


class Rotation(BaseModel):
    semaine: conint(ge=0, le=N_SEMAINES - 1)
    technicien: Technicien
