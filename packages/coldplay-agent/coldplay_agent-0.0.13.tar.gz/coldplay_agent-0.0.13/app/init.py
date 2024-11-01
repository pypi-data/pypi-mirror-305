import json
import shutil
import os

def initialize():
    # 获取用户输入的配置信息
    userinfo = input(
        "Enter your user information. For example:\n"
        '{"apiserver_host":"http://172.16.10.24:9099","apiserver_user":"coldplay@163.com","apiserver_pwd":"your pwd"}\n'
        "Paste the configuration here:\n"
    )
    config_dest = os.path.expanduser('~/.coldplay_config.ini')
    userinfo_json = json.loads(userinfo)
    # 创建配置文件内容
    config_content = f"""
    [DEFAULT]
    apiserver_host = {userinfo_json['apiserver_host']}
    apiserver_user = {userinfo_json['apiserver_user']}
    apiserver_pwd = {userinfo_json['apiserver_pwd']}
    """
    
    # 将输入的配置信息写入配置文件
    with open(config_dest, 'w') as config_file:
        config_file.write(config_content)
    
    print(f"Config file created at {config_dest}")
    print(f"Configuration saved: \n{config_content}")
