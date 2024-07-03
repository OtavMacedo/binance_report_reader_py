import csv
import json
from pathlib import Path

class ReportReader:
    def __init__(self, report_abs_path: str):
        """
        Inicializa o ReportReader com o caminho do relatório.

        Args:
            report_abs_path (str): Caminho absoluto do relatório CSV.
        """
        self._report_path = report_abs_path
        self._buy_list = []
        self._spend_list = []
        self._btc_amount, self._brl_spent, self._btc_average_price = 0, 0, 0

        self._extract_operations_from_csv()
        self._data_base_reader()
        self._calculate_average_price()
        self._data_base_writer()

    def _extract_operations_from_csv(self):
        """
        Extrai operações do arquivo CSV e as armazena nas listas de compras e
        gastos.
        """
        reader = self._csv_reader()

        for line in reader:
            coin, operation, change = (
                line['Coin'],
                line['Operation'],
                line['Change']
            )
            if coin not in {'BTC','BRL'}:
                continue

            try:
                change_value = float(change)
            except ValueError:
                continue
            
            if operation == 'Transaction Buy':
                self._buy_list.append([coin, change_value])

            elif operation == 'Transaction Spend':
                self._spend_list.append([coin, abs(change_value)])

    def _csv_reader(self):
        """
        Lê o arquivo CSV e retorna o conteúdo como uma lista de dicionários.

        Returns:
            list: Lista de dicionários contendo as linhas do CSV.
        """
        try:
            with open(self._report_path, 'r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            print(f"Error: The file {self._report_path} was not found.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return []
    
    def _calculate_average_price(self):
        """
        Calcula o preço médio do BTC com base nas operações.
        """
        self._sum_operations()

        if self._btc_amount > 0:
            self._btc_average_price = round(self._brl_spent/self._btc_amount, 2)
        else:
            self._btc_average_price = 0
    
    def _sum_operations(self):
        """
        Soma as operações de compra e gasto.
        """
        for buy, spend in zip(self._buy_list, self._spend_list):
            self._btc_amount += buy[1]
            self._brl_spent += spend[1]

    def _data_base_writer(self):
        """
        Escreve os dados calculados em um arquivo JSON.
        """
        data_base_path = Path(__file__).parent / 'wallet.json'

        wallet = {
            'btc_amount': round(self._btc_amount,8),
            'brl_spent': round(self._brl_spent, 2),
            'average_price': round(self._btc_average_price, 2) 
        }
        try:
            with open(data_base_path, 'w') as data_base:
                json.dump(wallet, data_base)
        except Exception as e:
            print(f"An error occurred while writing to the database: {e}")
    
    def _data_base_reader(self):
        """
        Lê os dados do arquivo JSON e atualiza os atributos da classe.
        """
        data_base_path = Path(__file__).parent / 'wallet.json'

        if data_base_path.exists():
            try:
                with open(data_base_path, 'r') as data_base:
                    data: dict = json.load(data_base)

                self._btc_amount = data.get('btc_amount', 0) 
                self._brl_spent = data.get('brl_spent', 0)
                self._btc_average_price = data.get('btc_average_price', 0)
            except Exception as e:
                print(f"An error occurred while reading the database: {e}")

    def return_operation_list(self):
        """
        Retorna a lista de operações combinando listas de compras e gastos.

        Returns:
            list: Lista combinada de operações de compra e gasto.
        """
        operations_count = len(self._buy_list)
        operations_list = [
            self._buy_list[i] + self._spend_list[i]
            for i in range(operations_count)
        ]
        return operations_list

    def display_values(self):
        """
        Exibe os valores calculados de preço médio, quantidade de BTC adquirido
        e BRL gasto.
        """
        print(f'Preço médio: R${self._btc_average_price}')
        print('qtd btc:', round(self._btc_amount, 8))
        print('brl gasto:', round(self._brl_spent, 2))

# Exemplo de uso
report = ReportReader('C:\\Users\\otavi\\Projetos\\binance_report_reader_py\\0e4e8d46-37d9-11ef-925b-0695fa030f45-1.csv')
report.display_values()
