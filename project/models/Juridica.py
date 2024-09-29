import sys
sys.path.append('/workspaces/Atividade-Pontuada-01/project/')
from project.models.Endereco import Endereco
from project.models.Pessoa import Pessoa
from abc import ABC, abstractmethod

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj:str, inscricaoEstadual:str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual