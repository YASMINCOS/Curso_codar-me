class Evento:
    #atributo de classe
    
    id= 1
    
    def __init__(self, nome,local=""):
        self.nome=nome
        self.local=local
        #inicializar com atribuito
        self.id=Evento.id 
        Evento.id += 1
    def imprime_informacoes(self):
        print("Id do evento:",self.id)
        print("Nome do evento",self.nome)
        print("Local do evento",self.local)
        print("----------------")
        
    @classmethod 
    def cria_evento_online(cls,nome):
        evento= cls(nome,local=f"https://tamarcado.com/eventos?id={cls.id}")
        return evento
    @staticmethod
    def calcula_limite_pessoas_area (area):
        if area >=5 and area <10:
            return 5
        elif area >=10 and area < 20:
            return 15
        elif area >=20:
            return 30
        else:
            return 0
    #heranca   
class EventoOnline(Evento):
    def imprime_informacoes(self):
        ev_online = self.cria_evento_online ("Live de Python")
        ev2_online= self.cria_evento_online("Live de JavaScript")
        ev_online.imprime_informacoes()
        ev2_online.imprime_informacoes()
        print("Id do evento:",self.id)
        print("Nome do evento",self.nome)
        print("Link para acessar o evento",{self.local})
        print("----------------")

        
    
            

        
   