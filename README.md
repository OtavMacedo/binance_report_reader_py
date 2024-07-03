# ReportReader

O `ReportReader` é uma classe Python que permite ler um relatório CSV gerado pela Binance contendo operações de compra e gasto de Bitcoins (BTC) e reais brasileiros (BRL). Ele processa esses dados para calcular o montante total de BTC, o total gasto em BRL e o preço médio do BTC com base nas transações.

## Funcionalidades

- Leitura de um arquivo CSV contendo dados de transações.
- Processamento das transações para extrair operações de compra e gasto.
- Cálculo do montante total de BTC e o total gasto em BRL.
- Cálculo do preço médio do BTC com base nas operações de compra.
- Armazenamento dos resultados calculados em um arquivo JSON.

## Requisitos

- Python 3.x
- Bibliotecas Python: `csv`, `json`, `pathlib`

## Uso

**Clone o repositório:**

    ```bash
    git clone url
    ```

### Exemplo de Uso:

```python
from binance_report_reader import ReportReader

# Caminho para o relatório CSV
report_path = "caminho/para/seu/arquivo.csv"

# Inicialização do ReportReader
report = ReportReader(report_path)

# Exibe os valores calculados
report.display_values()
```

### Métodos Disponíveis:

`__init__(report_abs_path: str)`
Inicializa a classe ReportReader com o caminho absoluto para o relatório CSV.

`display_values()`
Exibe os valores calculados de preço médio do BTC, quantidade total de BTC e total gasto em BRL.

`return_operation_list()`
Retorna uma lista de todas as operações combinadas de compra e gasto de BTC e BRL.

## Estrutura de Arquivos

- `binance_report_reader.py`: Contém a implementação da classe `ReportReader`.
- `wallet.json`: Arquivo JSON onde os resultados calculados são armazenados.

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato pelo e-mail: otavmacedo04@gmail.com