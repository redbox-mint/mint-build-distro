FROM centos:7
RUN yum install -y wget java-1.7.0-openjdk tar
COPY "./mint.tar.gz" /mint.tar.gz
RUN tar xvfz mint.tar.gz -C /opt/; rm /mint.tar.gz;chmod +x /opt/mint/server/tf_fg.sh
CMD /opt/mint/server/tf_fg.sh
