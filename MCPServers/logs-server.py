from datetime import datetime
# import json
# import pickle
from typing import Annotated
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Demo")

data = [
  {
    "timestamp": "2025-11-09T13:30:05",
    "level": "INFO",
    "service": "WebServer",
    "message": "Request GET /api/v1/users processed in 55ms."
  },
  {
    "timestamp": "2025-11-09T13:30:15",
    "level": "INFO",
    "service": "AuthService",
    "message": "User 'francisco_g' logged in successfully from IP 189.122.1.1."
  },
  {
    "timestamp": "2025-11-09T13:31:02",
    "level": "INFO",
    "service": "WebServer",
    "message": "Request GET /api/v1/dashboard processed in 120ms."
  },
  {
    "timestamp": "2025-11-09T13:32:15",
    "level": "WARN",
    "service": "AuthService",
    "message": "Failed login attempt for user 'admin' from IP 102.5.10.3."
  },
  {
    "timestamp": "2025-11-09T13:32:45",
    "level": "WARN",
    "service": "AuthService",
    "message": "Failed login attempt for user 'admin' from IP 102.5.10.3."
  },
  {
    "timestamp": "2025-11-09T13:33:10",
    "level": "ERROR",
    "service": "AuthService",
    "message": "Brute force suspected: Account 'admin' locked for 15 minutes due to 3 failed attempts from IP 102.5.10.3."
  },
  {
    "timestamp": "2025-11-09T13:35:00",
    "level": "INFO",
    "service": "WebServer",
    "message": "Request GET /api/v1/settings processed in 40ms."
  },
  {
    "timestamp": "2025-11-09T13:36:22",
    "level": "WARN",
    "service": "DB_Pool",
    "message": "Connection pool 'main-pool' reached 90% capacity (90/100 connections)."
  },
  {
    "timestamp": "2025-11-09T13:40:01",
    "level": "ERROR",
    "service": "PaymentService",
    "message": "Connection refused: Failed to connect to 'stripe-api.internal:443'. DNS resolution failed."
  },
  {
    "timestamp": "2025-11-09T13:40:15",
    "level": "INFO",
    "service": "AuthService",
    "message": "User 'laura_p' logged in successfully from IP 190.200.3.5."
  },
  {
    "timestamp": "2025-11-09T13:40:31",
    "level": "ERROR",
    "service": "PaymentService",
    "message": "Connection refused: Failed to connect to 'stripe-api.internal:443'. DNS resolution failed."
  },
  {
    "timestamp": "2025-11-09T13:41:00",
    "level": "INFO",
    "service": "WebServer",
    "message": "Request POST /api/v1/checkout processed in 210ms."
  },
  {
    "timestamp": "2025-11-09T13:41:01",
    "level": "ERROR",
    "service": "PaymentService",
    "message": "Connection refused: Failed to connect to 'stripe-api.internal:443'. DNS resolution failed."
  },
  {
    "timestamp": "2025-11-09T13:41:05",
    "level": "INFO",
    "service": "WebServer",
    "message": "Request GET /api/v1/profile processed in 35ms."
  },
  {
    "timestamp": "2025-11-09T13:41:31",
    "level": "ERROR",
    "service": "PaymentService",
    "message": "Service 'stripe-api.internal' is unresponsive. Moving to maintenance mode."
  },
  {
    "timestamp": "2025-11-09T13:42:00",
    "level": "ERROR",
    "service": "PaymentService",
    "message": "Connection refused: Failed to connect to 'stripe-api.internal:443'. DNS resolution failed."
  },
  {
    "timestamp": "2025-11-09T13:42:05",
    "level": "WARN",
    "service": "DB_Pool",
    "message": "Connection pool 'main-pool' capacity returned to 60% (60/100 connections)."
  },
  {
    "timestamp": "2025-11-09T13:45:00",
    "level": "INFO",
    "service": "CronJob",
    "message": "Scheduled task 'DailyReport_Generator' started."
  },
  {
    "timestamp": "2025-11-09T13:45:10",
    "level": "INFO",
    "service": "CronJob",
    "message": "Scheduled task 'DailyReport_Generator' finished successfully. Runtime: 9.8s."
  },
  {
    "timestamp": "2025-11-09T13:46:00",
    "level": "INFO",
    "service": "WebServer",
    "message": "Request GET /api/v1/health processed in 5ms."
  }
]
@mcp.resource(uri="data:///logs",name="Logs")
def allLogs():
   return data


# @mcp.tool("ObtenerBoludeces")
# def chi_cheñol(algo:str):
#     """
#      Hace cosas re contra locas nomás te digo
#     """
#     try:
#       return {
#          "status":"succesful",
#          "data":"holaaaa"
#       } 
#     except Exception as e:
#       return f"Error: {str(e)}"
    


@mcp.tool("ObtenerLogs")
def obtener_logs(fecha_inicio: Annotated[datetime,"Fecha de Inicio del rango de fechas"],fecha_fin: Annotated[datetime,"Fecha de Fin del rango de fechas"] =  datetime.today().strftime('%Y-%m-%d') ):
    """
     Retorna un array de logs de un rango de fechas determinado, por defecto se busca hasta la fecha actual.
    """
    # print("llegó hasta acá")
    logsobtenidos = data

    return {
  "status": "success",
  "logs_encontrados": len(logsobtenidos),
  "logs": logsobtenidos
}

@mcp.tool("CrearTicket")
def crear_ticket(status,contenido ): 
    """
      Crea un ticket a partir de un estado de vulnerabilidad.
    """
    return

@mcp.tool("EnviarAlertaporEmail")
def enviar_alerta_por_email(asunto,contenido):
    """
      Envia una alerta por email de un ticket.
    """
    return


if __name__ == "__main__":
    mcp.run(transport="stdio")