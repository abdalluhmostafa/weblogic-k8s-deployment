FROM oracle/weblogic:12.2.1.4-generic
MAINTAINER Johnathan Kupferer <jkupfere@redhat.com>

# Define variables with default values
ENV APP_NAME=${APP_NAME:-pippoWebApp} \
    APP_PKG_FILE=${APP_PKG_FILE:-pippoWebApp.war} \
    APP_PKG_LOCATION=${APP_PKG_LOCATION:-/u01/oracle} \
    USER_MEM_ARGS="-Djava.security.egd=file:/dev/./urandom" \
    SCRIPT_FILE=/u01/oracle/createAndStartEmptyDomain.sh \
    HEALTH_SCRIPT_FILE=/u01/oracle/get_healthcheck_url.sh \
    PATH=$PATH:${JAVA_HOME}/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin \
    DOMAIN_NAME="${DOMAIN_NAME:-base_domain}" \
    ADMIN_LISTEN_PORT="${ADMIN_LISTEN_PORT:-7001}" \
    ADMIN_NAME="${ADMIN_NAME:-AdminServer}" \
    ADMINISTRATION_PORT_ENABLED=false \
    ADMINISTRATION_PORT="${ADMINISTRATION_PORT:-9002}"

USER oracle

# Copy files and deploy application in WLST Offline mode
#-------------
COPY container-scripts/pippoWebApp.war container-scripts/create-wls-domain.py /u01/oracle/

# Define default command to start script.
CMD ["/u01/oracle/createAndStartEmptyDomain.sh"]