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
        cmd_par=kcweb.kcw.get_cmd_par()
        if cmd_par['server']:#启动web服务
            #执行kcwebplus自启项
            try:
                Queues.delwhere("code in (2,3)")
            except:pass
            startdata=sqlite().connect(model_app_path).where("types='kcwebplus'").table("start").order("id asc").select()
            for teml in startdata:
                os.system(teml['value'])
            if get_sysinfo()['uname'][0]=='Linux':
                system_start.insert_Boot_up(cmd='cd /kcwebplus && bash server.sh',name='kcwebplus自启',icon='https://img.kwebapp.cn/icon/kcweb.png')
                os.system('nohup kcwebplus intapp/index/pub/clistartplan --cli > app/runtime/log/server.log 2>&1 &')
        kcweb.cill_start(fdgrsgrsegsrsgrsbsdbftbrsbfdrtrtbdfsrsgr=fdgrsgrsegsrsgrsbsdbftbrsbfdrtrtbdfsrsgr)