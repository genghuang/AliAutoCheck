import subprocess
import os
import datetime

dt = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
file_name = './autostart.log'
chkProcess = os.popen("docker ps |grep yile |grep -v 'grep' |wc -l").read()
chkProcessArray = chkProcess.split("\n")
chkProcessInfo = [ x for x in chkProcessArray if x != '']
chkStatus = os.popen("docker inspect --format '{{.State.Running}}' yile").read()
chkStatusArray = chkStatus.split("\n")
chkStatusInfo = [ i for i in chkStatusArray if i != '']
f = open(file_name, mode='a', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
if len(chkProcessInfo) >= 1 and len(chkStatusInfo) >= 1:
    if chkProcessInfo[0] == '0' or chkStatusInfo[0] == 'false':
        f.write(dt+"系统检测到 yile 服务异常 \n")
    else:
        f.write(dt+"系统检测到 yile 正在运行中 \n")
else:
    f.write(dt+"Error: No such object: water_group_service \n")
