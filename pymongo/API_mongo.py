import urllib.parse
import pprint
import pymongo as pyM
import datetime

# Connection
username = urllib.parse.quote_plus('YOUR_USER')
password = urllib.parse.quote_plus('YOUR_PASSWORD')

client = pyM.MongoClient(f'YOUR_URL_CONNECTION')

db = client.test
collection = db.bank
print(db.bank)

zezim = {
    'name': 'zezim linguiça',
    'cpf': '123456789',
    'endereco': {
        'rua': 'boga rosa - ceara',
        'bairro': 'cancao',
        'cep': 12345
    },
    'date': datetime.datetime.now(tz=datetime.timezone.utc),
    'conta': 3242,
    'agencia': 'Roxinho-99',
    'tipo': 'poupanca'
}

bank = db.bank
bank_id = bank.insert_one(zezim).inserted_id

print(db.list_collection_names())

# exemplo de consulta
pprint.pprint(bank.find_one({"endereco.rua": "boga rosa - ceara"}))

many_cabras = [{
    'name': 'maria madalena',
    'cpf': '123456789',
    'endereco': {
        'rua': 'a',
        'bairro': 'sezxo',
        'cep': 54321
    },
    'date': datetime.datetime.now(tz=datetime.timezone.utc),
    'conta': 1234,
    'agencia': 'ZUK-99',
    'tipo': 'corrente'
}, {
    'name': 'brocks',
    'cpf': '123456',
    'endereco': {
        'rua': 'mercadao',
        'bairro': 'centro',
        'cep': 876
    },
    'date': datetime.datetime.now(tz=datetime.timezone.utc),
    'conta': 233,
    'agencia': 'laranja_54',
    'tipo': 'especial'
}]

result = bank.insert_many(many_cabras)

# retorna todos os documentos
all_data = bank.find({})
for docs in all_data:
    print(docs)