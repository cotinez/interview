FROM python as generator
WORKDIR /generator
ADD generator-server /generator
EXPOSE 5000
RUN ["/bin/bash", "-c", "pip install -r requirements.txt"]
ENTRYPOINT ["/usr/local/bin/python", "src/server.py"]

FROM python as solver
WORKDIR /solver
ADD solver-server /solver
EXPOSE 5001
RUN ["/bin/bash", "-c", "pip install -r requirements.txt"] 
ENTRYPOINT ["/usr/local/bin/python", "src/solver_server.py"]
