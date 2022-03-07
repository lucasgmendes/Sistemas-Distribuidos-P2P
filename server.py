from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc
import math
import hashlib
import util

NODES = 8
MAX_KEYS = 64
MAX_GRPC_WORKERS = 10

def str_to_bits(key):
    return int.from_bytes(hashlib.sha256(key.encode()).digest()[:4], 'little') % MAX_KEYS

class HashService(service_pb2_grpc.HashServicer):

    def __init__(self, node, next_instance):
        self.node = node
        self.next_instance = next_instance

    def available_node(self, chave):
        hash_key = str_to_bits(chave)
        choice = self.node.range[0] <= hash_key <= self.node.range[1]
        if choice:
            print(f'[+] Calculo da chave [{hash_key}] sendo feito no nó [{self.node.id}]')
        else:
            print(f'[+] Requisição transferida do nó [{self.node.id}] para o nó [{self.node.next}]')
        return choice

    def send_to_next_node(self, comando, chave, valor):
        stub = service_pb2_grpc.HashStub(self.channel)
        return stub.Create(service_pb2.HashRequest(comando=comando,
                                                   chave=chave,
                                                   valor=valor))

    def Create(self, request, context):
        if self.available_node(request.chave):
            try:
                self.node.hash[request.chave] = request.valor
                return service_pb2.HashReply(codigo=0, resposta=f'Receita [{request.chave}] criada com sucesso')
            except Exception as e:
                return service_pb2.HashReply(codigo=1, resposta=f'ERRO: {str(e)}')
        else:
            return self.next_instance(self.node.next_index, request.comando, request.chave, request.valor)

    def Read(self, request, context):
        if self.available_node(request.chave):
            try:
                valor = self.node.hash[request.chave]
                return service_pb2.HashReply(codigo=0, resposta=valor)
            except Exception as e:
                return service_pb2.HashReply(codigo=1, resposta=f'ERRO: {str(e)}')
        else:
            return self.next_instance(self.node.next_index, request.comando, request.chave, request.valor)

    def Update(self, request, context):
        if self.available_node(request.chave):
            try:
                self.node.hash[request.chave] = request.valor
                return service_pb2.HashReply(codigo=0, resposta=f'Receita [{request.chave}] atualizada com sucesso')
            except Exception as e:
                return service_pb2.HashReply(codigo=1, resposta=f'ERRO: {str(e)}')
        else:
            return self.next_instance(self.node.next_index, request.comando, request.chave, request.valor)

    def Delete(self, request, context):
        if self.available_node(request.chave):
            try:
                del self.node.hash[request.chave]
                return service_pb2.HashReply(codigo=0, resposta=f'Receita [{request.chave}] deletada com sucesso')
            except Exception as e:
                return service_pb2.HashReply(codigo=1, resposta=f'ERRO: {str(e)}')
        else:
            return self.next_instance(self.node.next_index, request.comando, request.chave, request.valor)

class Node(object):
    def __init__(self, ip, port, index, id, value_range, next_instance):
        self.ip = ip
        self.port = port
        self.index = index
        self.id = id
        self.range = value_range
        self.next_instance = next_instance
        self.hash = dict()

    def run(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=MAX_GRPC_WORKERS))

        service_pb2_grpc.add_HashServicer_to_server(HashService(self, self.next_instance), self.server)
        self.server.add_insecure_port(f'{self.ip}:{self.port}')
        self.server.start()

        print(f"[+] Host do servidor: [{self.ip}:{self.port}] conectado e pronto para receber chamadas!")

    def stop(self):
        self.server.stop(True)

    def __str__(self):
        return f'Node[ip={self.ip}, port={self.port}, id={self.id}, range={self.range}, next={self.next}]'

class GrpcServer(object):
    def __init__(self, N, qtd_chaves):
        self.size = N
        self.qtd_chaves = qtd_chaves
        self.range_size = math.ceil(qtd_chaves/N)
        self.servers = list()

        for i in range(0, N):
            ip = '127.0.0.1'
            port = 5050 + i

            value_range = (
                i * self.range_size,
                min(((i + 1) * self.range_size) - 1, self.qtd_chaves - 1)
            )
            self.servers.append(Node(ip, port, i, (i + 1) * self.range_size, value_range, self.next_instance))

        for i in range(0, N-1):
            self.servers[i].next_index = i + 1
            self.servers[i].next = (i + 2) * self.range_size

        self.servers[N-1].next = 0

    def start_servers(self):
        print(f'[+] Iniciando os {self.size} servidores')
        try:
            for server in self.servers:
                print(f'[+] Iniciando {server}')
                server.run()

            print("\n[*] Caso deseje encerrar o processo digite: [stop]")
            while(True):
                x = input()
                if x == 'stop':
                    break
                pass

        except KeyboardInterrupt:
            print("\n[-] Forçando parada via terminal")
            for server in self.servers:
                server.stop()

    def next_instance(self, node_id, comando, chave, valor):
        cur_node = self.servers[node_id]

        with grpc.insecure_channel(f'{cur_node.ip}:{cur_node.port}') as channel:
            return util.treat_command(channel, comando, chave, valor)

if __name__ == "__main__":
    server_ring = GrpcServer(NODES, MAX_KEYS)
    server_ring.start_servers()
