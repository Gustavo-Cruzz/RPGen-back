from pymongo import MongoClient, errors
import configparser
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, 'config', 'config.ini')

# Variáveis globais para o cliente e DB, para evitar múltiplas conexões
_client = None
_db = None

def _get_mongo_config():
    """
    Lê as configurações do MongoDB.
    Prioriza variáveis de ambiente 
    Faz fallback para o arquivo config.ini para desenvolvimento local.
    """
   
    mongo_uri_env = os.environ.get('MONGODB_ATLAS_URI')
    db_name_env = os.environ.get('MONGODB_DATABASE_NAME')

    if mongo_uri_env and db_name_env:
        print("Usando configurações do MongoDB a partir de variáveis de ambiente (Vercel).")
        return mongo_uri_env, db_name_env

    # Prioridade 2: Arquivo config.ini (para desenvolvimento local)
    print("Variáveis de ambiente MONGODB_ATLAS_URI ou MONGODB_DATABASE_NAME não encontradas.")
    print(f"Tentando ler configurações do arquivo: {CONFIG_FILE}")

    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(
            f"Arquivo de configuração '{CONFIG_FILE}' não encontrado e "
            "variáveis de ambiente MONGODB_ATLAS_URI/MONGODB_DATABASE_NAME não definidas."
        )
    
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)
    
    if 'mongodb' not in config:
        raise ValueError(
            "Seção [mongodb] não encontrada no arquivo de configuração e "
            "variáveis de ambiente não definidas."
        )
    
    uri_config = config.get('mongodb', 'atlas_uri', fallback=None)
    db_name_config = config.get('mongodb', 'database_name', fallback=None)
    
    if not uri_config or not db_name_config:
        raise ValueError(
            "Configurações 'atlas_uri' ou 'database_name' não encontradas na seção [mongodb] do config.ini "
            "e variáveis de ambiente não definidas."
        )
    
    print("Usando configurações do MongoDB a partir do arquivo config.ini.")
    return uri_config, db_name_config

def get_db_connection():
    """Retorna uma instância do banco de dados MongoDB."""
    global _client, _db
    if _db is None: # Conectar somente se ainda não houver uma conexão ativa
        try:
            mongo_uri, db_name = _get_mongo_config()
            
            print(f"Conectando ao MongoDB: URI (início): {mongo_uri[:30]}..., DB: {db_name}")
            # Timeout de conexão e servidor em milissegundos
            _client = MongoClient(
                mongo_uri, 
                serverSelectionTimeoutMS=5000, 
                connectTimeoutMS=5000,         
                socketTimeoutMS=5000           
            )
            # Verifica a conexão enviando um comando 'ping'
            _client.admin.command('ping') 
            print("Conexão com MongoDB estabelecida com sucesso.")
            _db = _client[db_name]
        except FileNotFoundError as e:
            print(f"Erro de configuração: {e}")
            raise
        except ValueError as e:
            print(f"Erro de valor de configuração: {e}")
            raise
        except configparser.Error as e:
            print(f"Erro ao ler o arquivo de configuração: {e}")
            raise
        except errors.ConfigurationError as e:
            print(f"Erro de configuração do PyMongo (verifique a URI de conexão): {e}")
            raise
        except errors.ConnectionFailure as e:
            print(f"Falha ao conectar ao MongoDB Atlas (verifique a rede/firewall/URI): {e}")
            raise
        except Exception as e: # Pega outras exceções inesperadas
            print(f"Ocorreu um erro inesperado ao conectar ao MongoDB: {e}")
            raise
    return _db

def get_collection(collection_name: str):
    """Retorna uma coleção específica do banco de dados conectado."""
    db = get_db_connection() # Garante que a conexão esteja estabelecida
    if db:
        return db[collection_name]
    return None 

def close_db_connection():
    """Fecha a conexão com o MongoDB, se estiver aberta."""
    global _client, _db
    if _client:
        _client.close()
        _client = None
        _db = None
        print("Conexão com MongoDB fechada.")

