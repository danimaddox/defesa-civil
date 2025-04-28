from supabase import create_client, Client

# ====> INSIRA AQUI SUA URL DO SUPABASE
SUPABASE_URL = "https://SEU-PROJETO.supabase.co"

# ====> INSIRA AQUI SUA CHAVE SECRETA (SERVICE_ROLE KEY)
SUPABASE_KEY = "SUA-SERVICE-ROLE-KEY"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Exemplo de dados para inserção automática
data = {
    "sigrc": 12345,
    "endereco": "Rua Exemplo",
    "numeral": 100,
    "bairro": "Centro",
    "distrito": "Distrito Central",
    "risco": 2,
    "motivo": "Manutenção Preventiva",
    "data": "2025-04-28"
}

try:
    response = supabase.table("tabela_unica").insert([data]).execute()
    print("✅ Dados inseridos com sucesso:", response.data)

except Exception as e:
    print("❌ Erro ao inserir dados:", e)
