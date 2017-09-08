#!/bin/bash
gitDirectory="PATH/TO/git"
# Do not add / to end
ansibleRunDirectory="PATH/TO/DIRECTORY/WHERE/ANSIBLE-PLAYBOOK/IS/RUN"
ansiblePlayBookFile="NAME OF PLAYBOOK TO BE RUN IN $ansibleRunDirectory"
cd $gitDirectory
cd terraform/testing
terraform apply
sleep 5
cd $gitDirectory
cd boto/testing
python getInstances.py
cp testing ansibleRunDirectory/testing
cd $ansibleRunDirectory
ansible-playbook $ansiblePlayBookFile -i testing

