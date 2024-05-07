from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey, create_engine, Column, Integer, DECIMAL, inspect
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select


Base = declarative_base()

class Client(Base):
    __tablename__ = 'client_base'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    cpf = Column(String(9), unique=True)
    endereco = Column(String(45))

    conta = relationship('Conta', back_populates='client')
    def __repr__(self):
        return f'User(id={self.id!r}, name={self.name!r}, cpf={self.cpf}, endereco={self.endereco!r}'

class Conta(Base):
    __tablename__ = 'conta_base'

    id = Column(Integer, primary_key=True)
    tipo = Column(String(30))
    agencia = Column(String(20))
    num = Column(Integer)
    saldo = Column(DECIMAL)
    id_client = Column(Integer, ForeignKey('client_base.id'), nullable=False)

    client = relationship('Client', back_populates='conta')

    def __repr__(self):
        return f'User(id={self.id!r}, tipo={self.tipo!r}, agencia={self.agencia}, num={self.num!r}, saldo={self.saldo!r}'

engine = create_engine("sqlite:///teste.db")

print(Client.__tablename__)
print(Conta.__tablename__)

Base.metadata.create_all(engine)

insp = inspect(engine)
print(insp.has_table("client_base"))
'''
Persistindo dados no bd

with Session(engine) as session:
    zezim = Client(
        name="zezim do balacobaco",
        cpf="123456789",
        endereco='chique-chique, Bahia',
    )
    seila = Client(
        name="ababa",
        cpf="234232",
        endereco='boga azul, Ceara',

    )
    alice_in_chains = Client(name='alice', cpf='2342542', endereco='pentecostal rua major de alfrredo, 456')
    session.add_all([zezim, seila, alice_in_chains])
    session.commit()
    
PERSISTINDO NA CONTA

with Session(engine) as session:
    conta_teste = Conta(
        tipo='corrente',
        agencia='roxin-03',
        num='246911',
        saldo=1000,
        id_client=3,
    )
    outro_teste = Conta(
        tipo='poupanca',
        agencia='laranja-01',
        num='24341',
        saldo=2000,
        id_client=1,
    )
    session.add_all([conta, outro_teste])
    session.commit()
'''

session = Session(engine)

stmt = select(Client).where(Client.name.in_(['zezim do balacobaco', 'alice']))
for user in session.scalars(stmt):
    print(user)

result = session.execute(select(Conta).order_by(Conta.id))
print(result.fetchone())

# Verificando a tabela de contas
stmt_conta = select(Conta).where(Conta.id_client.in_([1,3]))
for account in session.scalars(stmt_conta):
    print(account)