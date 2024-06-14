# Servem para fazer as validações e serializar os dados>
from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.Centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.Contrib.schemas import BaseSchema, OutMixin
from workout_api.Categorias.schemas import CategoriaIn

class AtletaIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta',example='Joao',max_length=50)]
    cpf: Annotated[str, Field(description='CPF do atleta',example='03653309140',max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta',example=25)]
    peso: Annotated[PositiveFloat, Field(description='Idade do atleta',example=25)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta',example=1.70)]
    sexo: Annotated[str,Field(description='Sexo do atleta',example='M',max_lenght=1)]
    categoria: Annotated[CategoriaIn,Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta,Field(description='CT do atleta')]
class AtletaIn(Atleta):
    pass
class AtletaOut(AtletaIn,OutMixin):
    pass