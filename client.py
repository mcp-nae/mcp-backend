import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from model import llm
from langchain.messages import HumanMessage,AIMessage
import asyncio

api_key = os.getenv("API_KEY")

model = ChatGoogleGenerativeAI(
api_key=api_key,
model="gemini-2.5-flash",
temperature=0.5,
max_tokens=2048)

client = MultiServerMCPClient(
    {
        "logs": {
            "transport": "stdio",  # Local subprocess communication
            "command": "python",
            # Absolute path to your math_server.py file
            "args": ["./MCPServers/logs-server.py"],
        },}
)

messages = []
async def invoke_agent():
    tools = await client.get_tools()
    agent = create_agent(model, tools,system_prompt="""Eres un agente especializado en análisis de logs. Sigue estas reglas estrictamente:

1. NUNCA muestres el JSON crudo al usuario
2. Cuando recibas logs de una fecha específica:
   - Agrupa los logs por nivel (INFO, WARN, ERROR)
   - Resume la cantidad de eventos por servicio
   - Destaca eventos críticos o patrones importantes
3. Presenta la información en formato legible:
   - "Se encontraron X eventos INFO, Y eventos WARN, Z eventos ERROR"
   - "Principales servicios afectados: [lista]"
   - "Eventos destacados: [resumen de los más importantes]"
4. Si encuentras patrones de error o advertencias repetidas, sugiere crear un ticket
5. Si el usuario pide más detalles sobre un evento específico, entonces muestra ese log en particular

Recuerda: SIEMPRE procesa y resume la información, NUNCA muestres el JSON raw.""")
    response = await agent.ainvoke(
        {"messages":messages},
    stream_mode="messages"
    )

    
    last_content = None
    formatted_response = []
    for chunk in response:
        current_content = chunk[0].content
        # convertie el contenido a string si es una lista
        if isinstance(current_content, list):
            current_content = current_content[0] if current_content else ""
        
        # Ssolo procesar strings y filtramos JSON y contenido no deseado
        if isinstance(current_content, str):
            if current_content and current_content != last_content:
                # filtrar contenido que parece JSON
                if not any(current_content.startswith(x) for x in ['{', '[', '"', "['", '{"']):
                    print(current_content)
                    formatted_response.append(current_content)
            last_content = current_content
    
    # agregar la respuesta formateada al historial de mensajes
    if formatted_response:
        final_content = "".join(formatted_response)
        messages.append(AIMessage(content=final_content))
    return messages

async def promptLLM(message: str):
    prompt = ""
    if (message == None):  
        prompt = input("Usuario: ")
    else: 
        prompt = message
    print("hasta acá llegó",prompt)
    messages.append(HumanMessage(prompt))
    response = await invoke_agent()
    return response

if __name__ == "__main__":
    asyncio.run(promptLLM())
    asyncio.run(promptLLM())
    asyncio.run(promptLLM())
