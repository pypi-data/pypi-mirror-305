try:
    from .common import *
except Exception as e:
    if 'unable to open database file' in str(e):
        print('该命令仅支持运行kcwebplus项目')
        exit()
    else:
        print('e',e)
from kcweb import kcweb
def cill_start(fdgrsgrsegsrsgrsbsdbftbrsbfdrtrtbdfsrsgr='kcwebplus'):
        "脚本入口"
        kcweb.cill_start(fdgrsgrsegsrsgrsbsdbftbrsbfdrtrtbdfsrsgr=fdgrsgrsegsrsgrsbsdbftbrsbfdrtrtbdfsrsgr)