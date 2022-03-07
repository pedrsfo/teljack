# teljack
Sequestro de sessão TCP em comunicações Telnet

Este script tem por finalidade realizar o sequestro de sessão TCP e injeção de pacote malicioso uma comunicação Telnet.

Utilizando os princípios de análise de pacotes, é realizada a captura da porta de origem da comunicação
TCP, número de sequencia e número de confirmação. É criado o pacote contendo o payload malicioso
de modo a estabelecer uma comunicação direta entre o servidor e o atacante, através de uma conexão reversa.

IMPORTANTE-1: Para a correta execução deste exploit, o atacate necessita ter acesso a comunicação entre o
cliente e o servidor. O ataque MITM, utilizando ARP Spoof, possibilita o sniff de pacotes. ;)

IMPORTANTE-2: Para a correta execução deste exploit, abra uma porta TCP de sua preferência para aguardar
a conexão reversa do exploit. Ex: nc -lp 4545

Modo de uso: Abra uma porta de sua preferência para esperar o exploit se conectar. Execute o exploit.
