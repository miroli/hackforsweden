FROM ipython/scipyserver 

MAINTAINER cj.sveningsson@gmail.com

RUN cd /opt; git clone https://github.com/H4Q/therepo.git repo
RUN cd /opt/repo ; git checkout -b sandbox origin/sandbox
CMD cd /opt/repo; /notebook.sh
EXPOSE 8888
