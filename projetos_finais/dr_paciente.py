'''
** Agendador Paciente - Doutor ** -
Crie uma classe de paciente e uma classe de médico.
Tenha um objeto médico que possa lidar
com vários pacientes e configurar um programa de agendamento,
onde um médico só pode lidar com 16 pacientes durante um dia de trabalho de 8 horas.
'''

class Paciente:
    pass

class Medico:
    def __init__(self):
        pass

    pacientes = []
    dia = 1

    def colocar_paciente(self, paciente):
        self.pacientes.append(paciente)
        if len(self.pacientes) > 8*self.dia:
            self.dia += 1
        print(f'Esse paciente será marcado para o dia {self.dia}')


m1 = Medico()
p1 = Paciente()
p2 = Paciente()
p3 = Paciente()
p4 = Paciente()
p5 = Paciente()
p6 = Paciente()
p7 = Paciente()
p8 = Paciente()
p9 = Paciente()
p10 = Paciente()
p11 = Paciente()
p12 = Paciente()
p13 = Paciente()
p14 = Paciente()
p15 = Paciente()
p16 = Paciente()
p17 = Paciente()
m1.colocar_paciente(p1)
m1.colocar_paciente(p2)
m1.colocar_paciente(p3)
m1.colocar_paciente(p4)
m1.colocar_paciente(p5)
m1.colocar_paciente(p6)
m1.colocar_paciente(p7)
m1.colocar_paciente(p8)
m1.colocar_paciente(p9)
m1.colocar_paciente(p10)
m1.colocar_paciente(p11)
m1.colocar_paciente(p12)
m1.colocar_paciente(p13)
m1.colocar_paciente(p14)
m1.colocar_paciente(p15)
m1.colocar_paciente(p16)
m1.colocar_paciente(p17)
print(m1.pacientes)
