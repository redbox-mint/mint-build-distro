FROM centos:7
RUN yum install -y wget java-1.7.0-openjdk tar
COPY "./mint.tar.gz" /mint.tar.gz
COPY institutional-build /opt/mint
RUN tar xvfz mint.tar.gz -C /opt/; rm /mint.tar.gz;chmod +x /opt/mint/server/*.sh
CMD /opt/mint/server/tf_fg.sh
