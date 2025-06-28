class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}")
        print(f"Telefone: {self.__telefone}")
        print(f"Email: {self.__email}")

    def get_nome(self):
        return self.__nome    
class Cliente(Pessoa):
    def __init__(self, nome, telefone, email, id_unico):
        super().__init__(nome, telefone, email)
        self.__id_unico = id_unico

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"ID único: {self.__id_unico}")
class Reserva:
    def __init__(self, dono_da_reserva, quarto_reservado, data_checkin, data_checkout, status):
        self.__dono_da_reserva = dono_da_reserva
        self.__quarto_reservado = quarto_reservado
        self.__data_checkin = data_checkin
        self.__data_checkout = data_checkout
        self.__status = status

    def get_nome(self):
        return self.__dono_da_reserva
    
    def get_quarto(self):
        return self.__quarto_reservado
class Quarto:
    def __init__(self, numero_do_quarto, tipo_de_quarto, preco_diaria, status="disponivel"):
        self.__numero_do_quarto = numero_do_quarto
        self.__tipo_de_quarto = tipo_de_quarto
        self.__preco_diaria = preco_diaria
        self.__status = status

    def get_status(self):
        return self.__status
    
    def get_numero_quarto(self):
        return self.__numero_do_quarto
    
    def set_status(self, novo_status):
        self.__status = novo_status
class GerenciadorDeReservas:
    def __init__(self) -> None:
        self.__reservas = []

    def verificar_disponibilidade(self, quarto):
        return quarto.get_status() == "disponivel"

    def criar_reserva(self, dono_da_reserva, quarto_reservado, data_checkin, data_checkout, status):
        if self.verificar_disponibilidade(quarto_reservado):
            reserva = Reserva(dono_da_reserva, quarto_reservado, data_checkin, data_checkout, "ocupado")
            quarto_reservado.set_status("ocupado")
            self.__reservas.append(reserva)
            print("reserva criada com sucesso.")
            return reserva
        else:
            print("Quarto não disponível")
            return None
        
    def cancelar_reserva(self, reserva):
        if reserva in self.__reservas:
            reserva.get_quarto().set_status("disponivel")
            self.__reservas.remove(reserva)
            print("Reserva cancelada.")
        else:
            print("Reserva nao encontrada")

    def modificar_reserva(self, reserva, novo_quarto, nova_data_checkin, nova_data_checkout):
        if reserva in self.__reservas:
            if self.verificar_disponibilidade(novo_quarto):
                reserva.get_quarto().set_status("disponivel")
                reserva._Reserva__quarto_reservado = novo_quarto
                reserva._Reserva__data_checkin = nova_data_checkin
                reserva._Reserva__data_checkout = nova_data_checkout
                novo_quarto.set_status("ocupado")
                print("Reserva modificada com sucesso.")
            else:
                print("Quarto nao disponivel.")
        else:
            print("Reserva nao existe ou ja foi cancelada.")
    def listar_reservas(self):
        for reserva in self.__reservas:
            print(f"Reserva de {reserva.get_nome().get_nome()}, no quarto {reserva.get_quarto().get_numero_quarto()}")