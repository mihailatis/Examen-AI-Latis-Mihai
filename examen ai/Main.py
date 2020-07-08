import os
import csv

if __name__ == '__main__':
    data = []
    with open(os.path.join(os.getcwd(), 'server.csv'), 'r') as server:
        csvreader = csv.reader(server, delimiter=',')
        headers = False
        for row in csvreader:
            if not headers:
                headers = True
                continue
            data.append(row)
    clients = []
    for row in data:
        if row[2] == 'high' and row[4] == 'simple':
            clients.append(row[0])
    print(clients)
    
    