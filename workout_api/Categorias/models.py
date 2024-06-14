from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.Contrib.models import BaseModel
from workout_api.Atleta.models import AtletaModel
from workout_api.Categorias.models import CategoriaModel
from workout_api.Centro_treinamento.models import CentroTreinamentoModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(50),unique=True,nullable=False)
    categoria:Mapped['AtletaModel']= relationship(back_populates='categoria')