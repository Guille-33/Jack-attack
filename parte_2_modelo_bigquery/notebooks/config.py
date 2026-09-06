import os
from dotenv import load_dotenv

load_dotenv(override=True)

# Configuración dataset
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET_ID = os.getenv("BQ_DATASET_ID")
CREDENTIALS_PATH = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Configuración generador data
N_CLIENTES=500
N_PRODUCTOS=70
N_PEDIDOS=2000