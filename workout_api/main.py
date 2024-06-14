from fastapi import FastAPI
from workout_api.routers import api_router
from workout_api.Atleta.models import AtletaModel
from workout_api.Categorias.models import CategoriaModel
from workout_api.Centro_treinamento.models import CentroTreinamentoModel
# fazendo essas importações, consertamos a importação circular

app = FastAPI(title='WorkoutApi')

if __name__ == 'main':
    import uvicorn
    uvicorn.run('main:app',host='0.0.0.0',port=8000,log_level='info',reload=True)

# Para subir o servidor pelo terminal:
# workout_api uvicorn workout_api.main:app -- reload
# Criar um arquivo requirements.txt

# Precisamos incluir as rotas no main:
app.include_router(api_router)

