FROM ipython/scipyserver 

MAINTAINER cj.sveningsson@gmail.com

RUN cd /opt; git clone https://github.com/vienno/hackforsweden.git repo
RUN cd /opt/repo ; git checkout -b sandbox origin/master
CMD cd /opt/repo; /notebook.sh
EXPOSE 8888
