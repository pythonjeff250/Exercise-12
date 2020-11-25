import socket
dURL = 'http://data.pr4e.org'
url = input('Please enter a URL: ')
if len(url) < 1:
    url = dURL
urlPieces = url.split('/')
print(urlPieces)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((urlPieces[2], 80))
except:
    print('Something went wrong with your URL!')
    quit()
cmd = 'GET '+url+' HTTP/1.0\r\n\r\n'
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()
