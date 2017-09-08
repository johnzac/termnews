import boto.ec2,yaml,sys
with open("secrets.yml","r") as ymlfile:
    cfg= yaml.load(ymlfile)
ansible_user = cfg['aws-configuration']['ansible_user']
ansible_user_ssh_key_file = cfg['aws-configuration']['ansible_ssh_private_key_file']
fil = {}
awsConn = boto.ec2.connect_to_region(cfg['aws-configuration']['region'])
for tags in cfg['aws-configuration']['tags']:
    tagName,tagValue=tags.items()[0]
    fil['tag:'+tagName] = tagValue
fil['instance-state-name'] = 'running'
reservations = awsConn.get_all_reservations(filters=fil)
instancesArray = [i for r in reservations for i in r.instances ]
f = open(cfg['ansible-inventory-filename'], 'w')
f.write("[" + cfg["ansible-host"] + "]\n")
for instance in instancesArray:
    print(instance.ip_address)
    f.write(instance.ip_address + " ansible_user=" + ansible_user + " ansible_ssh_private_key_file=" ansible_user_ssh_key_file + "  \n")

f.close
