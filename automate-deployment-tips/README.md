# deploy application as deployment using command line (t3)

java -cp /u01/oracle/wlserver/server/lib/weblogic.jar weblogic.Deployer -adminurl t3://localhost:7001 -user USER -password PASSWORD -deploy /u01/oracle/pippoWebApp.war  -remote -upload -timeout 500



# Redeploy your deployment to update it using command line (t3)
java -cp /u01/oracle/wlserver/server/lib/weblogic.jar weblogic.Deployer -adminurl t3://localhost:7001 -user aot -password oracle@aot -redeploy -name pippoWebApp -source /u01/oracle/pippoWebApp.war


------------------------------------------------------
------------------------------------------------------

# deploy application as deployment using (wlst.sh) Online deployment

It must your weblogic servies UP becuose it's access your console and make deployment

for ex:-

you_app_name = pippoWebApp

your_war_file_path= /u01/oracle/pippoWebApp.war


```
$ wlst.sh

$ connect('USER','PASS','t3://localhost:7001')

$ deploy('pippoWebApp','/u01/oracle/pippoWebApp.war',upload='true')

```

OR add these lines to new file like ` wlst-online-deployment.py` and run it 

`
wlst.sh wlst-online-deployment.py
`

Then restart weblogic services ` bin/stopWebLogic.sh `




# Deploy application as deployment using (wlst.sh) OFFLINE deployment _ CI/CD

Offline is good way due it can run even Weblogic serivce down

Edit Values for appname,apppkg,appdir 

appname    = os.environ.get('APP_NAME', 'pippoWebApp')

apppkg     = os.environ.get('APP_PKG_FILE', 'pippoWebApp.war')

appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle') # path to your war file

then run it 

` 
wlst.sh wlst-offline-deployment.py
`



