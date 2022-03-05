## TO install FMW Infrastructure you will need 

1. Deploy RHEL8-OracleJava Image

2. Deploy FMW-Infrastructure Image

3. Deploy  your FMW domain

===================================
# (1) Deploy RHEL8-OracleJava Image

We will deploy RHEL8 with JDK8 as infrastructure for our Weblogic

1. Go to OracleJava8 Dir

` cd 1-OracleJava/8 ` 

2. Download REQUIRED FILES TO BUILD THIS IMAGE 
FROM ` https://www.oracle.com/java/technologies/javase-server-jre8-downloads.html `  to  ` OracleJava/8 ` 


Downloaded File Name: ` server-jre-8uXX-linux-x64.tar.gz `

3. Build OracleJava8 Image from Docker file 

` ./build.sh 8 `

4. Image will be build and named ` oracle/serverjre:8-oraclelinux8 `

We will use image to build WebLogic image in next step

5. Check your image status 

` docker images ` 


===================================================

# (2) Deploy FMW-infrastructure Image

1. Change Dir to 2-FMW-infrastructure/dockerfiles/12.2.1.4 

` $ cd 2-FMW-infrastructure/dockerfiles/12.2.1.4 `

2. Download REQUIRED FILES TO BUILD THIS IMAGE

Download the Generic installer from http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-for-dev-1703574.html 


Oracle WebLogic Server 12.2.1.4
Generic
(579 MB)


Download file name: fmw_12.2.1.4.0_wls_lite_Disk1_1of1.zip


3. Back to dir 2-FMW-infrastructure/dockerfiles

` cd .. ` 

4. Build your WebLogic Image 

` ./buildDockerImage.sh -v 12.2.1.4 ` 

This will build Image named : `oracle/fmw-infrastructure:12.2.1.4 `

NOTE: IF you deploy new domain for frist time it need to connect DB using NEW RCU PERFIX 

If there is existing domain it will skip creating new domain 

it check base_domain/logs if there are logs so we have a domain if no logs so it will create new domain 


We can run this image build every time we need to change any thing in docker file we will rebuild Weblogic env from 0 , So we will use this image as A source for next step to ` deploy your application ` 

--> If you want to use this image to run !NOT RECOMMAND 

```
docker run --name ..............

```

5. Check your image status 

` docker images ` 


===================================================

# (3) Deploy your FMW Domain
--


NOTE: IF you deploy new domain for frist time it need to connect DB using NEW RCU PERFIX 

If there is existing domain it will skip creating new domain 

it check base_domain/logs if there are logs so we have a domain if no logs so it will create new domain 


SO: we need to create volume to map your domain to your host ` -v /root/domains:/u01/oracle/user_projects/domains ` 

This path is in your pc and it's epmty `  /root/domains ` when domain created for frist time using RCU 
Iy will map domain home to ` /root/domains ` So when you restart contaier it will check this path ` /u01/oracle/user_projects/domains  ` inside container if found it, it will skep create new domain and will start you domain ..

If you using K8s you must create PVC ..


Dockerfile use image ` oracle/fmw-infrastructure:12.2.1.4` that's you build in step2 to Deploy your application inside weblogic

1. Change your dir to 3-fmw-domain

` cd 3-fmw-domain`


2. Copy your WAR file to container-scripts folder 


3. Build your image

` $ docker build -t deploy-domain . `


4. Edit ` properties/domain.properties ` and put your console username and password


5. Run your application 


``` 
docker run --name my_deployment -d \ 
-p 7010:7001 -v $PWD/properties:/u01/oracle/properties \
-e APP_NAME=$My_app -e APP_PKG_FILE=My_app.war  deploy-domain 
 
```

NOTE:  There are alot of other ENV values you can use but by default is


```
APP_NAME=pippoWebApp 

APP_PKG_FILE=pippoWebApp.war 

APP_PKG_LOCATION=/u01/oracle

USER_MEM_ARGS=-Djava.security.egd=file:/dev/./urandom

DOMAIN_NAME=base_domain

ADMIN_LISTEN_PORT=7001

ADMIN_NAME=AdminServer

ADMINISTRATION_PORT_ENABLED=false

ADMINISTRATION_PORT=9002

```


6. Check your docker container

` $ docker ps ` 

7. Check container logs 

` $ docker logs -f my_deployment `

8. Access weblogic admin

` http://IP:7010/console `

9. Access your deployment

` http://IP:7010/$Deployment_Name `



-------

Check automate-deployment-tips to know how auto deploy works  
we use wlst offline deployment



===================================================

# Deploy your Domain to kubernetes cluster

1. Create deployment

Change image to your domain image inside deployment.yaml

```
cd k8s-deployment

kubectl apply -f deployment.yaml 

```

2. Create Service

` kubectl apply -f service.yaml `


3. Create Ingress 

` kubectl apply -f ingress.yaml ` 