from datetime import datetime
from uuid import uuid4
from fastapi import APIRouter, Body, HTTPException,status
from workout_api.Atleta.schemas import AtletaIn,AtletaOut
from workout_api.Atleta.models import AtletaModel
from workout_api.Categorias.models import CategoriaModel

from workout_api.Contrib.dependencies import DatabaseDependency
from sqlalchemy.future import select

api_router= APIRouter()

@router.post('/',summary='Criar novo atleta',
             status_code=status.HTTP_201_CREATED,
             response_model=AtletaOut
             )
async def post(db_session: DatabaseDependency,atleta_in:AtletaIn=Body(...)
    ):
        categoria = (await db_session.execute(select(CategoriaModel).filter_by(nome=atleta_in))).scalars().first()
        if not categoria:
            raise HTTPException(
                   status_code=status.HTTP_400_BAD_REQUEST,
                   detail=f'Centro de treinamento não encontrado no id': {id})        
        
        #breakpoint()   
        atleta_out = AtletaOut(id=uuid4(),created_at=datetime.utcnow(), **atleta_in.model_dump())
        atleta_model = AtletaModel(**atleta_out.model_dump(exclude={'categoria':'centro_treinamento'}))
        db_session.add()(atleta_model)
        await db_session.commit()
        return categoria

    