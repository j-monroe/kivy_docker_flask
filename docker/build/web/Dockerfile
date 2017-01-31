FROM centos:7
MAINTAINER The CentOS Project <cloud-ops@centos.org>
LABEL Vendor="CentOS" \
      License=GPLv2 \
      Version=2.4.6-40


RUN yum -y --setopt=tsflags=nodocs update && \
yum -y install epel-release && \ 
yum -y install python-pip && \ 
yum install mod_wsgi -y  && \ 
yum clean all  && \ 
useradd python-web
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["micro.py"]
