import argparse
import paramiko
from random import randint
from paramiko.ssh_exception import SSHException
from scp import SCPClient, SCPException


#creo una connessione ssh al server
def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

#faccio uso del comando scp per scaricare i file di log
def scp_get(scp, dates, download_path):
    for elem in dates:
        scp.close()
        try:
            scp.get('VOL250GB/pdns_' + elem + '*', download_path)
            print('Scarico -->' + elem)
        except SCPException as e:
            print('Il log a data ' + elem + ' non esiste.')

def download(download_path,ip,port,host,psw,year):
    ssh = createSSHClient(ip, port, host, psw) 
    scp = SCPClient(ssh.get_transport(), sanitize=lambda x: x)

    year = year
    dates = []

    for month in range(1, 13):
        month = str(month)
        #estraggo dei giorni da 1 a 31 a seconda del mese
        if month in [4, 6, 9, 11]:
            days = [randint(1, 30), randint(1, 30), randint(1, 30), randint(1, 30), randint(1, 30), randint(1, 30)]
        elif int(month) == 2:
            days = [randint(1, 28), randint(1, 28), randint(1, 28), randint(1, 28), randint(1, 28), randint(1, 28)]
        else:
            days = [randint(1, 31), randint(1, 31), randint(1, 31), randint(1, 31), randint(1, 31), randint(1, 31)]
        if int(month) < 10:
            month = '0' + str(month)
        for day in days:
            day = str(day)
            hour = str(randint(0, 23))
            if int(day) < 10:
                day = '0' + str(day)
            if int(hour) < 10:
                hour = '0' + str(hour)
            date = year + '_' + month + '_' + day + '_' + hour
            dates.append(date)

    scp_get(scp, dates, download_path)

    ssh.close()
    scp.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip-address',type=str, default='', help='Indirizzo IP dove scaricare i file GAR')
    parser.add_argument('--port', type=str, default='', help='Porta indirizzo IP')
    parser.add_argument('--host',type=str, default='', help='Host')
    parser.add_argument('--year', type=str, default='2021', help='Anno file Log')
    parser.add_argument('--psw', type=str, default='', help='Password del server')
    parser.add_argument('--out-dir', type=str, default='D:/Universita/Laurea Magistrale/Advanced Cybersecurity/Progetto/log_files', help='Directory di output')
    args, _ = parser.parse_known_args()
    download(args.out_dir, args.ip_address, args.port, args.host, args.psw, args.year)

main()

