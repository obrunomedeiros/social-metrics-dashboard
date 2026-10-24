import pandas as pd
from datetime import datetime

def transformar_metricas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe o DataFrame bruto da extração, realiza a limpeza, 
    padronização de tipos e tratamento de valores nulos.
    """
    if df.empty:
        print("[AVISO] O DataFrame recebido para transformação está vazio.")
        return df

    print("-> Iniciando a limpeza e transformação dos dados...")
    
    # Cria uma cópia para evitar warnings do Pandas
    df_clean = df.copy()

    # 1. Padronização de Colunas e Tipos Inteiros
    colunas_inteiras = [
        "perfil_id", "seguidores", "seguidores_ganhos", 
        "alcance", "impressoes", "engajamento", 
        "curtidas", "comentarios", "compartilhamentos", "cliques"
    ]
    
    for col in colunas_inteiras:
        if col in df_clean.columns:
            # Substitui nulos por 0 e converte para inteiro
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce').fillna(0).astype(int)
        else:
            # Caso a API não tenha retornado a coluna, inicializa com 0
            df_clean[col] = 0

    # 2. Padronização da Data (Garante formato YYYY-MM-DD)
    if "data" in df_clean.columns:
        df_clean["data"] = pd.to_datetime(df_clean["data"]).dt.date
    else:
        df_clean["data"] = datetime.now().date()

    # 3. Tratamento de strings ou colunas textuais (se houver)
    # Exemplo: remover espaços em branco desnecessários caso venham nomes de perfis
    if "nome_perfil" in df_clean.columns:
        df_clean["nome_perfil"] = df_clean["nome_perfil"].astype(str).str.strip()

    # 4. Seleção e ordenação final das colunas esperadas pelo banco de dados
    colunas_finais = [
        "perfil_id", "data", "seguidores", "seguidores_ganhos", 
        "alcance", "impressoes", "engajamento", "curtidas", 
        "comentarios", "compartilhamentos", "cliques"
    ]
    
    # Garante que apenas as colunas mapeadas no banco sigam adiante
    df_clean = df_clean[[col for col in colunas_finais if col in df_clean.columns]]

    print("-> Transformação concluída com sucesso!")
    return df_clean