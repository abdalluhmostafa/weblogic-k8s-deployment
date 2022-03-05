FROM oracle/weblogic:12.2.1.4-generic
MAINTAINER Johnathan Kupferer <jkupfere@redhat.com>

# Define variables with default values
ENV ORACLE_HOME=/u01/oracle \
    VOLUME_DIR=/u01/oracle/user_projects \
    SCRIPT_FILE=/u01/oracle/container-scripts/* \
    HEALTH_SCRIPT_FILE=/u01/oracle/container-scripts/get_healthcheck_url.sh \
    DOMAIN_NAME="${DOMAIN_NAME:-infra_domain}" \
    ADMIN_LISTEN_PORT="${ADMIN_LISTEN_PORT:-7001}" \
    ADMIN_NAME="${ADMIN_NAME:-AdminServer}" \
    ADMIN_HOST="${ADMIN_HOST:-InfraAdminContainer}" \
    ADMINISTRATION_PORT_ENABLED="${ADMINISTRATION_PORT_ENABLED:-true}" \
    ADMINISTRATION_PORT="${ADMINISTRATION_PORT:-9002}" \
    MANAGEDSERVER_PORT="${MANAGEDSERVER_PORT:-8001}" \
    MANAGED_NAME="${MANAGED_NAME:-infraServer1}" \
    MANAGED_SERVER_CONTAINER="${MANAGED_SERVER_CONTAINER:-false}" \
    RCUPREFIX="${RCUPREFIX:-INFRA01}" \
    PRODUCTION_MODE="${PRODUCTION_MODE:-prod}" \
    CONNECTION_STRING=${CONNECTION_STRING:-InfraDB:1521/InfraPDB1.us.oracle.com} \
    JAVA_OPTIONS="-Doracle.jdbc.fanEnabled=false -Dweblogic.StdoutDebugEnabled=false" \
    PATH=$PATH:/usr/java/default/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin:/u01/oracle/container-scripts

USER oracle

# Copy files and deploy application in WLST Offline mode
#-------------

WORKDIR ${ORACLE_HOME}
# Define default command to start script.
CMD ["/u01/oracle/createAndStartEmptyDomain.sh"]