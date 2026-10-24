import requests
from src.config import Config
from datetime import datetime
import pandas as pd

def extrair_dados_instagram():
    """
    Realiza a requisição HTTP para a Meta Graph API,
    extraindo as métricas diárias da conta comercial do Instagram.
    """
    account_id = Config.IG_BUSINESS_ACCOUNT_ID
    access_token = Config.IG_ACCESS_TOKEN
    
    if not account_id or not access_token:
        raise ValueError("As credenciais do Instagram (ID ou Token) não estão configuradas no ambiente.")
    
    # Endpoint oficial da Meta Graph API para a conta Business
    url = f"https://graph.facebook.com/v19.0/{account_id}"
    
    # Parâmetros solicitando métricas de perfil e seguidores
    params = {
        "fields": "followers_count,follows_count,media_count,insights.metric(reach,impressions,profile_views).period(day)",
        "access_token": access_token
    }
    
    print(f"-> Conectando à API do Instagram para o ID: {account_id}...")
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Erro na requisição da API do Instagram [{response.status_code}]: {response.text}")
    
    data = response.json()
    
    # Processamento inicial dos dados brutos recebidos da API
    seguidores_totais = data.get("followers_count", 0)
    
    # Extração iterativa dos insights retornados pela API da Meta
    insights_data = data.get("insights", {}).get("data", [])
    metricas_extraidas = {
        "data": datetime.now().date(),
        "seguidores": seguidores_totais,
        "seguidores_ganhos": 0, # Poderá ser calculado comparando com o dia anterior no banco
        "alcance": 0,
        "impressoes": 0,
        "cliques": 0
    }
    
    for item in insights_data:
        nome_metrica = item.get("name")
        valor = item.get("values", [{}])[0].get("value", 0)
        
        if nome_metrica == "reach":
            metricas_extraidas["alcance"] = valor
        elif nome_metrica == "impressions":
            metricas_extraidas["impressoes"] = valor
        elif nome_metrica == "profile_views":
            metricas_extraidas["cliques"] = valor

    # Simulando o perfil_id 1 (que corresponde ao Instagram na nossa tabela dim_perfis)
    # No orquestrador principal, você mapeará isso dinamicamente.
    metricas_extraidas["perfil_id"] = 1 
    
    # Retorna como um DataFrame do pandas para padronizar com o restante da pipeline
    df_resultado = pd.DataFrame([metricas_extraidas])
    
    print("-> Dados do Instagram extraídos com sucesso!")
    return df_resultado