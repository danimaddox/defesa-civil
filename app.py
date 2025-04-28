from flask import Flask, request, jsonify
from supabase import create_client, Client
import os

app = Flask(__name__)

# Configuração do Supabase
SUPABASE_URL = "https://seu-projeto.supabase.co"
SUPABASE_KEY = "sua-chave-secreta"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        data = request.json
        
        # Verifica se todas as colunas necessárias estão presentes
        required_columns = ["sigrc", "endereco", "numeral", "bairro", "distrito", "risco", "motivo", "data"]
        missing_columns = [col for col in required_columns if col not in data]
        
        if missing_columns:
            return jsonify({"error": f"Colunas ausentes: {', '.join(missing_columns)}"}), 400
        
        # Converte tipos para garantir compatibilidade com PostgreSQL
        data["sigrc"] = int(data["sigrc"])
        data["numeral"] = int(data["numeral"])
        data["risco"] = int(data["risco"])
        
        response = supabase.table("tabela_unica").insert([{
            "sigrc": data["sigrc"],
            "endereco": data["endereco"],
            "numeral": data["numeral"],
            "bairro": data["bairro"],
            "distrito": data["distrito"],
            "risco": data["risco"],
            "motivo": data["motivo"],
            "data": data["data"]
        }]).execute()
        
        return jsonify({"message": "Dados inseridos com sucesso!", "response": response.data})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)