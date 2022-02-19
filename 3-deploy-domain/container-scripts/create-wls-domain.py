#Copyright (c) 2014-2018 Oracle and/or its affiliates. All rights reserved.
#
#Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#
# WebLogic on Docker Default Domain
#
# Domain, as defined in DOMAIN_NAME, will be created in this script. Name defaults to 'base_domain'.
#
# Since : October, 2014
# Author: monica.riccelli@oracle.com
# ==============================================
import os

domain_name  = os.environ.get("DOMAIN_NAME", "base_domain")
admin_name  = os.environ.get("ADMIN_NAME", "AdminServer")
admin_listen_port   = int(os.environ.get("ADMIN_LISTEN_PORT", "7001"))
domain_path  = '/u01/oracle/user_projects/domains/%s' % domain_name
production_mode = os.environ.get("PRODUCTION_MODE", "prod")
administration_port_enabled = os.environ.get("ADMINISTRATION_PORT_ENABLED", "true")
administration_port = int(os.environ.get("ADMINISTRATION_PORT", "9002"))
admin_name = os.environ.get('ADMIN_NAME', 'AdminServer')
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/base_domain')
appname    = os.environ.get('APP_NAME') # it will get app name from ENV docker file
apppkg     = os.environ.get('APP_PKG_FILE') # It will get app.jar file name from ENV docker file
appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle') # this path for where you copy WAR file inside container

print('domain_name                 : [%s]' % domain_name);
print('admin_listen_port           : [%s]' % admin_listen_port);
print('domain_path                 : [%s]' % domain_path);
print('production_mode             : [%s]' % production_mode);
print('admin name                  : [%s]' % admin_name);
print('administration_port_enabled : [%s]' % administration_port_enabled);
print('administration_port         : [%s]' % administration_port);
print('appname                     : [%s]' % appname);
print('apppkg                      : [%s]' % apppkg);
# Open default domain template
# ============================
readTemplate("/u01/oracle/wlserver/common/templates/wls/wls.jar")

set('Name', domain_name)
setOption('DomainName', domain_name)

# Set Administration Port 
# =======================
if administration_port_enabled != "false":
   set('AdministrationPort', administration_port)
   set('AdministrationPortEnabled', 'true')

# Disable Admin Console
# --------------------
# cmo.setConsoleEnabled(false)

# Configure the Administration Server and SSL port.
# =================================================
cd('/Servers/AdminServer')
set('Name', admin_name)
set('ListenAddress', '')
set('ListenPort', admin_listen_port)
if administration_port_enabled != "false":
   create('AdminServer','SSL')
   cd('SSL/AdminServer')
   set('Enabled', 'True')

# Define the user password for weblogic
# =====================================
cd(('/Security/%s/User/weblogic') % domain_name)
cmo.setName(username)
cmo.setPassword(password)

# Write the domain and close the domain template
# ==============================================
setOption('OverwriteDomain', 'true')
setOption('ServerStartMode',production_mode)

# Create Node Manager
# ===================
#cd('/NMProperties')
#set('ListenAddress','')
#set('ListenPort',5556)
#set('CrashRecoveryEnabled', 'true')
#set('NativeVersionEnabled', 'true')
#set('StartScriptEnabled', 'false')
#set('SecureListener', 'false')
#set('LogLevel', 'FINEST')

# Set the Node Manager user name and password 
# ===========================================
#cd('/SecurityConfiguration/%s' % domain_name)
#set('NodeManagerUsername', username)
#set('NodeManagerPasswordEncrypted', password)

## DEPLOY your application
# Write Domain
# ============
writeDomain(domain_path)
closeTemplate()

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create Application
# ==================
cd('/')
app = create(appname, 'AppDeployment')
app.setSourcePath(appdir + '/' + apppkg)
app.setStagingMode('nostage')

# Assign application to AdminServer
# =================================
assign('AppDeployment', appname, 'Target', 'AdminServer')

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
# Exit WLST
# =========
exit()
