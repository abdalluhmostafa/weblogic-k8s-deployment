import os

# Deployment Information
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/base_domain')
admin_name = os.environ.get('ADMIN_NAME', 'AdminServer')
appname    = os.environ.get('APP_NAME', 'pippoWebApp')
apppkg     = os.environ.get('APP_PKG_FILE', 'pippoWebApp.war')
appdir     = os.environ.get('APP_PKG_LOCATION', '/u01/oracle')

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
exit()