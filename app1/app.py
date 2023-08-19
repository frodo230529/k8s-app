from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def index():
    # 서버의 호스트 이름
    host_name = socket.gethostname()
    
    # 서버의 IP 주소
    server_ip = socket.gethostbyname(host_name)
    
    # 서비스 포트
    service_port = 5000  # 기본 Flask 포트

    # 클라이언트의 IP 주소
    client_ip = request.remote_addr

    return f'''
    <h1>Server and Client Information</h1>
    <p>Server Hostname: {host_name}</p>
    <p>Server IP: {server_ip}</p>
    <p>Service Port: {service_port}</p>
    <p>Client IP: {client_ip}</p>
    '''

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
