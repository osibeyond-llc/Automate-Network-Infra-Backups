import os, datetime, time, sys, pymsteams

sys.path.append("C:/Users/user/backup.conf")
sys.path.append("C:/Users/user/AppData/Local/Programs/Python/Python38/python.exe")
sys.path.append("C:/Users/user/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/site-packages")
sys.path.append("C:/Users/user/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/site-packages/pymsteams")
sys.path.append("C:/Users/user/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0/LocalCache/local-packages/Python38/site-packages/pymsteams-0.1.12-py3.8.egg-info")


import paramiko, scp
from scp import SCPClient

myTeamsMessage = pymsteams.connectorcard("https://outlook.office.com/webhook/57f6c43f-9da6-45fc-9e31-3723ff646870@24206b4b-82b5-439b-b729-30902be87f29/IncomingWebhook/f17751a552894cb1a8dac849f830bf49/da0dbdfb-1e95-4465-9218-248769e7f365")



now = datetime.datetime.now()
print(now)
def createSSHClient(server, port, user, password):
	client = paramiko.SSHClient()
	client.load_system_host_keys()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(server, port, user, password)
	return client

server = "192.168.zzzzzzz"
port = "22"
user = "yyyyyyy"
password = "xxxxxxxxxxxxxxx"


ssh = createSSHClient(server, port, user, password)
scp = SCPClient(ssh.get_transport())
nowstring = (now.strftime("%m-%d-%Y-%H-%M"))
path =  "C:/Users/user/backup.confs/confs/%s" % nowstring

if not os.path.exists(path):
	try:
		os.mkdir(path)
	except OSError:
		print("Could not make directory, made in C:/Temp instead.")
		path = "C:/Temp/confs/%s" % nowstring
		os.mkdir(path)


scp.get("/tmp/system.cfg", path + "/system.cfg")
scp.get("/tmp/running.cfg", path + "/running.cfg")



#email to teams, datetime, first and tailing 20 chars as confirmation
myTeamsMessage.text("Server:" + server + "  |  Date: " + nowstring + "| Directory Name: " + path + "| system.cfg present: **" + str(os.path.exists(path + "/system.cfg")) + "** - system.cfg size: " + str(os.path.getsize(path + "/system.cfg")) + "| running.cfg present: **" + str(os.path.exists(path + "/running.cfg")) + "** - running.cfg size: " + str(os.path.getsize(path + "/running.cfg")))
print(("Server: " + server + "  |  Date: " + nowstring + "  |  Directory Name: " + path + "  |  system.cfg present: " + str(os.path.exists(path + "/system.cfg")) + " - system.cfg size: " + str(os.path.getsize(path + "/system.cfg")) + "  |  running.cfg present: " + str(os.path.exists(path + "/running.cfg")) + " - running.cfg size: " + str(os.path.getsize(path + "/running.cfg"))))

myTeamsMessage.send()



#To use stdout-based config files when using a platform that doesnt allow SCP

#ssh = paramiko.SSHClient()
#now = datetime.datetime.now()

#astmh
#server = "192.168.xxxxx"
#u#sername = "yyyyyyyyy"
#password = "zzzzzzzzzzzz"
#conf_path = "/var/run/fastpath/startup-config"
#filename_prefix = "C:\\Users\\user\\Desktop\\confs\\" + server

#FTP site:  confs : C:\Users\user\Desktop\confs

#ssh = paramiko.Transport((server, 22))
#ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect(username=username, password=password)
#sftp = paramiko.SFTPClient.from_transport(ssh)
#sftp.get("/var/tmp/system.cfg", "C:/Users/user/Destop/confs/system.cfg")
#sftp.get("/var/tmp/running.cfg", "C:/Users/user/Destop/confs/running.cfg")

#chan = ssh.invoke_shell()
#time.sleep(2)
#chan.send('echo "     --------- SYSTEM.CFG ---------"\n')
#chan.send('\n')
#chan.send('cat /tmp/system.cfg\n')
#chan.send('echo "     --------- RUNNING.cfg --------"\n')
#chan.send('cat /tmp/running.cfg\n')
#time.sleep(30)
#output = chan.recv(999999)
##print(output)
#filename = "%s_%.2i%.2i%i_%.2i%.2i.cfg" % ( filename_prefix, now.year, now.month, now.day, now.hour, now.minute)
#ff = open(filename, 'a')
# ff.write(output)
#ff.write(output.decode("utf-8"))
#ff.close()
###close ssh session
ssh.close()
print(server)

#######################_
