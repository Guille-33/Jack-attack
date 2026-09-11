# Jack-attack 🃏

Este proyecto está dividido en dos partes principales:
1. **Parte 1: SQL Murder Mystery** - Resolución del misterio utilizando consultas SQL.
2. **Parte 2: Modelo BigQuery** - Implementación y desarrollo de modelos de datos en Google BigQuery.

---

## 🛠️ Instrucciones de Setup (Configuración del Proyecto)

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 1. Prerrequisitos
Asegúrate de tener instalado lo siguiente en tu sistema:
* **Python 3.9 o superior**
* **Git**
* Una cuenta de **Google Cloud Platform (GCP)** (necesaria para la parte de BigQuery)

### 2. Clonar el Repositorio
Clona este proyecto en tu máquina local y accede a la carpeta del proyecto:
```bash
git clone https://github.com
cd Jack-attack
```

### 3. Crear y Activar un Entorno Virtual
Es muy recomendable usar un entorno virtual para no interferir con otras librerías de tu sistema.

* **En macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **En Windows (Command Prompt):**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### 4. Instalar las Dependencias
Con el entorno virtual activado, instala todas las librerías necesarias ejecutando:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configurar las Variables de Entorno
El proyecto requiere configurar ciertas credenciales y variables para conectarse a los servicios (como BigQuery).

1. Duplica el archivo `.env.example` y renombralo a `.env`:
   ```bash
   cp .env.example .env
   ```
2. Abre el archivo `.env` recién creado y rellena las variables con tus datos reales (por ejemplo, rutas a tus llaves JSON de GCP, IDs de proyecto, etc.).

---

## 🚀 Ejecución del Proyecto

* **Parte 1 (SQL Murder Mystery):** Entra en la carpeta `parte_1_sql_murder_mystery` y ejecuta los scripts correspondientes o cuadernos de notas asignados.
* **Parte 2 (BigQuery):** Entra en la carpeta `parte_2_modelo_bigquery`. Asegúrate de tener tus credenciales de Google Cloud activas en el archivo `.env` antes de lanzar los modelos.