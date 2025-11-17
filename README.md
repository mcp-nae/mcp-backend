### CHAT PARA CONTROL DE INCIDENCIAS IT
Este es un prototipo de un sistema RAG (Retrieval-Augmented Generation) construido con LangChain. La aplicación permite "chatear" con un documento PDF (arquitecturas.pdf), extrayendo contexto relevante de una base de datos vectorial para responder preguntas del usuario de forma precisa.

## Tecnologías Utilizadas
* Framework: LangChain
* Modelos de Lenguaje (LLM):
    * Google Gemini (vía langchain_google_genai)
* Embeddings (Vectorización): 
    * Ollama - nomic-embed-text (vía langchain_ollama)
* Base de Datos Vectorial:
    * ChromaDB (vía langchain_chroma)
* Gestión de Entorno:
    * python-dotenv
* Lenguaje de Programación:
    * Python
## Instalación
1. Clonar el respositorio
```bash
git clone https://github.com/tatymediina/tp-rag-langchain.git
``` 
2. Moverse a la carpeta _mcp-backend_
```bash
cd mcp-backend
``` 

3. Crear un entorno virtual e instalar las dependencias del proyecto utilizando [uv](https://github.com/astral-sh/uv).
```bash
 uv sync
```

4. 
El proyecto se divide en dos fases principales: Ingesta y Recuperación/Generación.

1. Fase de Ingesta (Ingestion)
Este proceso se corre una sola vez para "aprender" el documento.

Carga (upload_pdf): Se lee el archivo arquitecturas.pdf y se extrae todo su contenido de texto.
División (text_splitter): El texto largo se divide en pedazos (chunks) más pequeños y manejables.
Vectorización (embedding): Cada chunk de texto se convierte en un vector numérico (un "embedding") que representa su significado semántico, usando el modelo nomic-embed-text de Ollama.
Almacenamiento (get_vector_store): Los vectores se guardan en una base de datos vectorial Chroma persistente (en el directorio ./vectorstore) en una colección específica.
2. Fase de Consulta (Chat Loop)
Esto es lo que sucede cada vez que un usuario hace una pregunta.

Consulta (retrieval): La pregunta del usuario también se convierte en un vector. Chroma usa este vector para buscar y recuperar los chunks de texto más similares (semánticamente relevantes) de la base de datos.
Contextualización (prompt): Se construye un prompt dinámico usando la plantilla. Este prompt le da al LLM su rol, sus reglas (ej. "responde solo con el contexto") e inyecta los chunks recuperados ({contexto}) y la pregunta del usuario ({input_user}).
Generación (response): El prompt completo se envía al LLM (ej. Gemini).
Streaming: La respuesta del LLM se recibe y se imprime en la consola en tiempo real (palabra por palabra).
Exploración: Bases de Datos Vectoriales
Aunque este proyecto utiliza Chroma por su simplicidad y capacidad de persistencia local, LangChain es compatible con una amplia gama de bases de datos vectoriales. La elección depende del caso de uso (producción vs. prototipo, escala, necesidad de filtros, etc.).

Aquí hay una comparativa de algunas alternativas populares:

| Base de Datos | Tipo | Ventajas | Desventajas |
| :--- | :--- | :--- | :--- |
| **Chroma** | Local / Open Source | Súper fácil de empezar, persistente, buena integración. | No está hecha para producción a gran escala (millones de vectores). |
| **FAISS** | En memoria / Open Source | Extremadamente rápida para búsqueda. De Facebook (Meta). | **No es persistente** por defecto (es un índice en RAM). Tienes que guardarlo y cargarlo como un archivo. |
| **Qdrant** | Local / Cloud / Open Source | Muy rápida, filtros avanzados, lista para producción. | Un poco más compleja de configurar que Chroma. |
| **Pinecone** | Servicio en Cloud | Totalmente gestionada, escalado infinito, muy potente. | Es de pago, añade latencia de red. |
| **pgvector** | Extensión de PostgreSQL | Genial si **ya usas PostgreSQL**. Tus vectores viven junto a tus datos relacionales. | Puede no ser tan rápida como una BD vectorial dedicada. |