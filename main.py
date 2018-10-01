from entidades import cliente
from repositorios import cliente_repositorio

cliente = cliente.Cliente("Samantha", 25)

cliente_repositorio.ClienteRepositorio.listar_clientes()


