import socket
dominio = input("Alvo: ")
brute = ["ns1", "ns2", "ns3", "ns4", "www","ftp","intranet" , "mail"]
for nome in brute:
    DNS = nome + "." +dominio
    
    try:
        print(f" {DNS} {socket.gethostbyname(DNS)}")
    except socket.gaierror:
            pass


