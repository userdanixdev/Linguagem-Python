from datetime import datetime
from sqlalchemy import DateTime,ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column,relationship
from workout_api.Contrib.models import BaseModel
from workout_api.Atleta.models import AtletaModel
from workout_api.Categorias.models import CategoriaModel
from workout_api.Centro_treinamento.models import CentroTreinamentoModel



class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Mapped[int] = mapped_column(Integer,primary_key=True)
    nome: Mapped[str] = mapped_column(String(50),nullable=False)
    cpf: Mapped[str] = mapped_column(String(11),unique=True,nullable=False)
    idade: Mapped[int] = mapped_column(Integer,nullable=False)
    peso: Mapped[float] = mapped_column(Float,nullable=False)
    altura: Mapped[float] = mapped_column(Float,nullable=False)
    sexo: Mapped[float] = mapped_column(String(1),nullable=False)
    createt_at: Mapped[datetime] = mapped_column(Datetime,nullable=False)
    categoria:Mapped['CategoriaModel']= relationship(back_populates='atleta')
    categoria_id : Mapped[int]=mapped_column(ForeignKey('categorias.pk_id'))
    # Com isso, declaramos um relacionamento de atleta com categoria, porém, na categoria,
    # deverá ter um campo atleta também
    centro_treinamento:Mapped['CentroTreinamentoModel']= relationship(back_populates='atleta')
    centro_treinamento_id : Mapped[int]=mapped_column(ForeignKey('centros_treinamentos.pk_id'))


