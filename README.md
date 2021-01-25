# Arkhn DevOps exercise

 devops-interview


## STEP 1: A small python program

Pull or clone the repository to execute locally

RUN:

$ python generator-server/src/server.py

$ python solver-server/src/solver_server.py




## STEP 2: Dockerizing the program

RUN:

$ docker build -t generator --target generator .

$ docker run -p 5000:5000 -d generator

$ docker build -t solver --target solver .

$ docker run -p 5001:5001 -d solver


              OR


$ docker-compose up -d



## STEP 3: Using a CI to build a publish your docker image

The .github/workflows/ci.yml file

RUN:

$ docker pull egafosso/generator

$ docker pull egafosso/solver


## STEP 4: Ansible automation
Note: An ubuntu EC2 instance has been used to write and test this playbook instead of Vagrant VM.
"ansible" folder in the repository contains :
- Inventory folder containing an INI inventory file (with localhost only as managed host)
- configuration file (ansible.cfg)
- The playbook (playbook.yml)

They play is directly applied to localhost in this play as inventory contains no managed host.

RUN:

$ ansible-playbook -vv ansible/playbook.yml


            --------------------    THANK YOU   ------------------------
