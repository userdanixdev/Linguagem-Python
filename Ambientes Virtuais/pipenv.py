## Pipenv é uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências com a criação de ambiente virtual para seus projetos e adiciona/remove
## pacotes automaticamente do arquivo Pipfile conforme você instala e desinstala pacotes.

pip install pipenv
# 
pipenv install django
## Para visualizar conteúdo do arquivo use os comandos:
type Pipfile
get-content Pipfile
# Ambos irão fornecer o mesmo resultado abaixo:

[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
django = "*"

[dev-packages]

[requires]
python_version = "3.12"

# USANDO O GET-CONTENT PARA VISUALIZAR O ARQUIVO 'Pipfile.lock' :
get-content Pipfile.lock
{
    "_meta": {
        "hash": {
            "sha256": "0b5823de65ff0f5100b8f0fd7642f5000e8f2788c925cc51afe587d419e35515"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.12"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "asgiref": {
            "hashes": [
                "sha256:3e1e3ecc849832fe52ccf2cb6686b7a55f82bb1d6aee72a58826471390335e47",
                "sha256:c343bd80a0bec947a9860adb4c432ffa7db769836c64238fc34bdc3fec84d590"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==3.8.1"
        },
        "django": {
            "hashes": [
                "sha256:8363ac062bb4ef7c3f12d078f6fa5d154031d129a15170a1066412af49d30905",
                "sha256:ff1b61005004e476e0aeea47c7f79b85864c70124030e95146315396f1e7951f"
            ],
            "index": "pypi",
            "markers": "python_version >= '3.10'",
            "version": "==5.0.6"
        },
        "sqlparse": {
            "hashes": [
                "sha256:714d0a4932c059d16189f58ef5411ec2287a4360f17cdd0edd2d09d4c5087c93",
                "sha256:c204494cd97479d0e39f28c93d46c0b2d5959c7b9ab904762ea6c7af211c8663"
            ],
            "markers": "python_version >= '3.8'",
            "version": "==0.5.0"
        },
        "tzdata": {
            "hashes": [
                "sha256:2674120f8d891909751c38abcdfd386ac0a5a1127954fbc332af6b5ceae07efd",
                "sha256:9068bc196136463f5245e51efda838afa15aaeca9903f49050dfa2679db4d252"
            ],
            "markers": "sys_platform == 'win32'",
            "version": "==2024.1"
        }
    },
    "develop": {}
}
## No arquivo acima, mostra a hash e as dependências e versão de cada programa no lock. Quando vc passa o projeto para outro programador esse arquivo vai também ##
## O gerenciador de pacote pipenv é mais completo que o pip, sendo assim, tem a possibilidade de atualizar os pacotes com a função update do próprio gerenciador ##

Comando 'graph' do pipenv irá listar todas as dependências e ainda poder exclui-las

pipenv graph
## Para verificar todas as funcionalidades do gerenciador basta chama-lo:
pipenv
Commands:
  check         Checks for PyUp Safety security vulnerabilities and against
                PEP 508 markers provided in Pipfile.
  clean         Uninstalls all packages not specified in Pipfile.lock.
  graph         Displays currently-installed dependency graph information.
  install       Installs provided packages and adds them to Pipfile, or (if no
                packages are given), installs all packages from Pipfile.
  lock          Generates Pipfile.lock.
  open          View a given module in your editor.
  requirements  Generate a requirements.txt from Pipfile.lock.
  run           Spawns a command installed into the virtualenv.
  scripts       Lists scripts in current environment config.
  shell         Spawns a shell within the virtualenv.
  sync          Installs all packages specified in Pipfile.lock.
  uninstall     Uninstalls a provided package and removes it from Pipfile.
  update        Runs lock, then sync.
  upgrade       Resolves provided packages and adds them to Pipfile, or (if no
                packages are given), merges results to Pipfile.lock
  verify        Verify the hash in Pipfile.lock is up-to-date.

## Com o comando pipenv clean, o interpretador irá desistalar todos as dependências ##

