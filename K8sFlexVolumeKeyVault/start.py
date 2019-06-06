from flask import Flask
import os
import socket
import contextlib
import ssl
import OpenSSL.crypto
import requests
import base64

app = Flask(__name__)

@app.route('/')
def hello():
    cert = open("/kvmnt/bhaskarsignercertificate", "r").read()
    pfx = base64.b64decode(cert.strip())

    pkcs12 = OpenSSL.crypto.load_pkcs12(pfx, "")
    
    html =  '<h2>Hello, Bhaskardeep Khaund</h2><br/><h3><b>Hostname :</b> {hostname}</h3><br><h3><b>Cert from /kvmnt :</b>{cert}</h3>'
    
    return html.format(hostname=socket.gethostname(), cert=pkcs12.get_certificate().get_serial_number())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

