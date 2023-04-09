# -*- coding: utf-8 -*-
# @Time    : 2023/3/8 20:11
# @Author  : 石鑫磊
# @Site    :
# @File    : remote_connent.py
# @Software: PyCharm
# @Comment :

import paramiko
from web_frame.etc import config
import sys
sys.path.append('./../')
import os

from etc.config import BASEDIR

class SSHProxy():
    instance = None
    def __init__(self):
        self.hostname = config.hostname
        self.port = config.port
        self.username = config.name
        self.password = config.password
        self.open()
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.instance:
    #             return cls.instance
    #     cls.instance = object.__new__(cls)
    #     return cls.instance

    def open(self):
        # private_key=paramiko.RSAKey.from_private_key(self.password)
        self.transport = paramiko.Transport(self.hostname, self.port)
        # self.transport.connect(username=self.username, pkey=private_key)
        self.transport.connect(username=self.username, password=self.password)

    def close(self):
        self.transport.close()

    def command(self, cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin, stdout, stderr = ssh.exec_command(cmd)
        result = stdout.read()
        return result

    def upload(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.put(local_path, remote_path)
        sftp.close()

    def download(self, local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.transport)
        sftp.get(remote_path, local_path)
        sftp.close()

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


if __name__ == "__main__":
    with SSHProxy() as ssh:
        ssh.download(os.path.join(BASEDIR, 'source/saba_set.sh'),'/root/saba_set.sh')
        res = ssh.command('df -h')
        print(res.decode('utf-8'))