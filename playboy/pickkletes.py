# -*- coding:utf-8 -*-
# Author Hsinhan Chiang
import pickle
roledefs = {
    'bpdcap': ['bpdcap@172.16.1.165:22', ],
    'bpdmbs': ['bpdmbs@172.16.1.165:22', ],
    'bpdposp': ['bpdposp@172.16.1.165:22', ],
    'cgdgw': ['cgdgw@172.16.1.166:22', ],
    'cgdpom': ['cgdpom@172.16.1.166:22', ],
    'cgdweb': ['cgdweb@172.16.1.166:22', ],
    'cgdifc': ['cgdifc@172.16.1.166:22', ],
    'csdacm': ['csdacm@172.16.1.167:22', ],
    'csdact': ['csdact@172.16.1.167:22', ],
    'csdbpg': ['csdbpg@172.16.1.167:22', ],
    'csdmkm': ['csdmkm@172.16.1.167:22', ],
    'gsdadt': ['gsdadt@172.16.1.170:22', ],
    'gsdpay': ['gsdpay@172.16.1.170:22', ],
    'gsdpsm': ['gsdpsm@172.16.1.170:22', ],
    'bsdbat': ['bsdbat@172.16.1.171:22', ],
    'bsdbui': ['bsdbui@172.16.1.171:22', ],
    'bsdrpt': ['bsdrpt@172.16.1.171:22', ],
}
serverInfo=open("serverInfo.cfg","wb")
pickle.dump(roledefs,serverInfo)