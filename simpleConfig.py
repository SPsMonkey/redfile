#对python的configparsor进行简单封装，那个用起来太复杂了
#使用就2个函数  read_config （）和write_config()
import os
import configparser

def create_config():
    config = configparser.ConfigParser()
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def read_config(section,key,default=""):
    if not os.path.exists('config.ini'):
        create_config()
    config = configparser.ConfigParser()
    config.read('config.ini')
    if not (section in config.sections()):
        config.add_section(section)
    if not(key in config[section]):
        config.set(section,key,default,)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    result=config[section][key]
    return result


def write_config(section,key,value):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config.set(section,key,value)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)