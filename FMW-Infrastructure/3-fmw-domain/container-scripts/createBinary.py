import os

# Deployment Information
domainhome = os.environ.get('DOMAIN_HOME', '/u01/oracle/user_projects/domains/base_domain')
admin_name = os.environ.get('ADMIN_NAME', 'AdminServer')
appname    = os.environ.get('LIBRARIES_NAME')
apppkg     = os.environ.get('LIBRARIES_PKG_FILE')
appdir     = os.environ.get('LIBRARIES_PKG_LOCATION', '/u01/oracle')

# Read Domain in Offline Mode
# ===========================
readDomain(domainhome)

# Create Application
# ==================
cd('/')
app = create(appname, 'Library')
app.setSourcePath(appdir + '/' + apppkg)
app.setStagingMode('nostage')

# Assign application to AdminServer
# =================================
assign('Library', appname, 'Target', 'AdminServer')

# Update Domain, Close It, Exit
# ==========================
updateDomain()
closeDomain()
exit()
