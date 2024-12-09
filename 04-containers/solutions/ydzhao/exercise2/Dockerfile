FROM asntech/bios259:w24

## Install latest version of seaborn uisng pip from PyPI - https://pypi.org/project/seaborn/
RUN pip install seaborn

## set working directory to /opt
WORKDIR /opt

## Copy the app2.py file to /opt  
COPY app2.py /opt

## Make app2.py executeable
RUN chmod +x /opt/app2.py

## Add ap2p.py to the path
ENV PATH=/opt:$PATH

## Run the application help
CMD ["app2.py", "--help"]
