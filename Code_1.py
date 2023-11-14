'''Configuração do Ambiente de Desenvolvimento:

    Instale Python, Pip e Git no Ubuntu usando comandos como sudo apt install python3 python3-pip git.
    Configure o Git (git config --global user.name "Seu Nome" e git config --global user.email "seuemail@example.com").
    Crie um ambiente virtual (virtualenv venv) e ative-o (source venv/bin/activate).
    Instale Flask e SQLAlchemy (pip install flask sqlalchemy).

Implementação da Lógica de Coleta de Dados:

    Crie um arquivo data_collector.py.
    Escreva o código para simular a coleta de dados:
'''
import random
from datetime import datetime, timedelta

def simulate_daily_data(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield {
            'date': current_date.strftime('%d/%m/%Y'),
            'location': 'São Paulo',
            'total_aircrafts': random.randint(100, 200),
            'drones': random.randint(30, 60),
            'eVTOLs': random.randint(20, 40),
            'commercial_flights': random.randint(50, 100),
            'incidents': {
                'on_ground': random.randint(0, 5),
                'in_air': random.randint(0, 5)
            },
            'weather_conditions': {
                'visibility': random.choice(['Low', 'Medium', 'High']),
                'wind_speed': random.choice(['Low', 'Medium', 'High']),
                'precipitation': random.choice(['None', 'Light', 'Moderate', 'Heavy'])
            },
            'traffic_density': random.choice(['Low', 'Medium', 'High']),
            'operational_issues': random.randint(0, 10)
        }
        current_date += timedelta(days=1)

def collect_data():
    start_date = datetime(2023, 12, 24)
    end_date = datetime(2024, 1, 2)
    return list(simulate_daily_data(start_date, end_date))

if __name__ == "__main__":
    data = collect_data()
    for day_data in data:
        print(day_data)

#Execute o script (python data_collector.py) para ver a simulação dos dados.

#Este processo abrange tanto a configuração do ambiente de desenvolvimento quanto a implementação da lógica de coleta de dados, incluindo a simulação de dados para São Paulo em um período de alta densidade de aeronaves e problemas operacionais.
