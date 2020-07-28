import sb
conta1 = sb.ContaCorrente('Banco do Brasil', 1000, 1, 9000)
conta2 = sb.ContaPoupanca('Santander', 500, 2)
cliente1 = sb.Cliente('luis', 19, conta1)
cliente2 = sb.Cliente('gabriel', 18, conta2)
sb.Banco.adicionar_cliente(cliente1)
sb.Banco.adicionar_cliente(cliente2)
sb.Banco.listar_clientes()
#cliente1.infos()
#cliente2.infos()
conta1.depositar(300)
cliente1.checa_saca(10)
cliente1.infos()
