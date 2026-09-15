import pandas as pd
import os

def processar_camada_silver(caminho_bronze, caminho_silver):
    print("Iniciando processamento da camada Silver...")
    
    df = pd.read_csv(caminho_bronze, encoding='latin1', sep=';')
    
    # 1: Limpeza de nulos
    df['CPF PORTADOR'] = df['CPF PORTADOR'].fillna('SIGILOSO')
    df['DATA TRANSAÇÃO'] = df['DATA TRANSAÇÃO'].fillna('SIGILOSO')
    
    # 2: Padronizando o cabeçalho (minúsculo, sem espaço, sem acento)
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.normalize('NFKD')
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')
    )
    
    # Removendo espaços em branco no início ou fim dos dados de texto
    colunas_texto = df.select_dtypes(include=['object']).columns
    for col in colunas_texto:
        df[col] = df[col].astype(str).str.strip()
        
    # 3: Conversão de valores
    df['valor_transacao'] = df['valor_transacao'].str.replace(',', '.').astype(float)
    
    # 4: Padronização de datas
    df['data_transacao'] = pd.to_datetime(df['data_transacao'], format='%d/%m/%Y', errors='coerce')
    
    # SALVAMENTO
    df.to_parquet(caminho_silver, index=False)
    print(f"Processamento concluído! Arquivo salvo na Silver em: {caminho_silver}")

if __name__ == "__main__":

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    ARQUIVO_BRONZE = os.path.join(BASE_DIR, 'data', '01_bronze', '202512_CPGF.csv')
    ARQUIVO_SILVER = os.path.join(BASE_DIR, 'data', '02_silver', 'cpgf_silver.parquet')
    
    processar_camada_silver(ARQUIVO_BRONZE, ARQUIVO_SILVER)