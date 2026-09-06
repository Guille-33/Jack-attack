from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud.bigquery.table import (ForeignKey,TableConstraints,TableReference,ColumnReference, PrimaryKey)
from config import (CREDENTIALS_PATH,PROJECT_ID,DATASET_ID)

# Cliente autenticado
def create_client()->bigquery.Client:
    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH
    )
    client = bigquery.Client(
        project=PROJECT_ID,
        credentials=credentials
    )
    return client

# Crear dataset
def generate_dataset(client:bigquery.Client):
    dataset_ref = bigquery.Dataset(f"{PROJECT_ID}.{DATASET_ID}")
    dataset_ref.location = "EU"  # Datos en Europa
    client.create_dataset(dataset_ref, exists_ok=True)
    print(f"Dataset {DATASET_ID} creado")

# Crear tabla
def build_BQ_table(*,name:str,fields:dict,constraints:dict,client:bigquery.Client):
    schema=[]
    foreign_keys=[]
    for (field,info) in fields.items():
        schema.append(
            bigquery.SchemaField(name=field,field_type=info[0],mode=info[1] if len(info)>1 else None)
        )
    table_ref=f"{PROJECT_ID}.{DATASET_ID}.{name}"
    table=bigquery.Table(table_ref=table_ref,schema=schema)
    for f in constraints.get('foreigns',[]):
        referenced_table=TableReference.from_string(f"{PROJECT_ID}.{DATASET_ID}.{f.get('ref_table')}")
        column_references=ColumnReference(
            referenced_column=f.get('ref_column'),
            referencing_column=f.get('loc_column')
        )
        foreign_keys.append(
            ForeignKey(
                name=f.get('ref_table'),
                referenced_table=referenced_table,
                column_references=[column_references]
            )
        )
    primary=constraints.get('primary')
    table.table_constraints=TableConstraints(primary_key=PrimaryKey(columns=primary),foreign_keys=foreign_keys if foreign_keys else None)
    client.create_table(table=table,exists_ok=True)
    print(f"Tabla {name} procesada correctamente en BigQuery.")