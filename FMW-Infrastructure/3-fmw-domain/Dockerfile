#Copyright (c) 2019 Oracle and/or its affiliates. All rights reserved.
#
# Licensed under the Universal Permissive License v 1.0 as shown at http://oss.oracle.com/licenses/upl.
#
# ORACLE DOCKERFILES PROJECT
# --------------------------
# This is the Dockerfile for Oracle FMW Infrastructure 12.2.1.3
#
# HOW TO BUILD THIS IMAGE
# -----------------------
# The Oracle FMW Infrastructure image extends the Oracle WebLogic Infrastructure 12.2.1.3 image, you must first build the Oracle WebLogic Infrastructure image.
# Run:
#      $ docker build -f Dockerfile -t 12213-fmw-domain-in-volume .
#
# IMPORTANT
# ---------
# The resulting image of this Dockerfile contains a FMW Infra Base Domain.
#
# From
# -------------------------
FROM oracle/fmw-infrastructure:12.2.1.4

# Maintainer
# ----------
MAINTAINER Monica Riccelli <monica.riccelli@oracle.com>


# WLS Configuration
# ---------------------------
ENV ORACLE_HOME=/u01/oracle \
    VOLUME_DIR=/u01/oracle/user_projects \
    SCRIPT_FILE=/u01/oracle/container-scripts/* \
    HEALTH_SCRIPT_FILE=/u01/oracle/container-scripts/get_healthcheck_url.sh \
    DOMAIN_NAME="${DOMAIN_NAME:-base_domain}" \
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
    PATH=$PATH:/usr/java/default/bin:/u01/oracle/oracle_common/common/bin:/u01/oracle/wlserver/common/bin:/u01/oracle/container-scripts \
    APP_NAME=${APP_NAME:-attendance.ear} \
    APP_PKG_FILE=${APP_PKG_FILE:-attendance.ear} \
    LIBRARIES_NAME=${LIBRARIES_NAME:-MedanTemplate} \
    LIBRARIES_PKG_FILE=${LIBRARIES_PKG_FILE:-MedanTemplate.war}

# Add files required to build this image
COPY container-scripts/* /u01/oracle/container-scripts/
COPY properties/* /u01/oracle/properties/
# COPY Libares 
COPY build-files/MedanTemplate.war /u01/oracle/
# Copy deployment app
COPY build-files/attendance.ear /u01/oracle/
#Create directory where domain will be written to
USER root
RUN mkdir -p $CUSTOM_DOMAIN_ROOT && \
    chown -R oracle:oracle $CUSTOM_DOMAIN_ROOT && \
    chmod -R a+xwr $CUSTOM_DOMAIN_ROOT && \
    mkdir -p $CUSTOM_DOMAIN_HOME && \
    chmod -R a+xwr $CUSTOM_DOMAIN_HOME && \
    mkdir -p $ORACLE_HOME/properties && \
    chmod -R a+r $ORACLE_HOME/properties && \ 
    chmod +x /u01/oracle/container-scripts/*

VOLUME  $CUSTOM_DOMAIN_ROOT

USER oracle
WORKDIR $CUSTOM_DOMAIN_HOME
CMD ["/u01/oracle/container-scripts/createFMWDomain.sh"]
