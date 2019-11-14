import pulumi
import pulumi_aws as aws

## AWS ec2
#
## settings
size = 't2.micro'
ami = aws.get_ami(most_recent="true",
                  owners=['099720109477'],
                  filters=[{"name":"name","values":["ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-*"]}])
## aws security group
group = aws.ec2.SecurityGroup('webserver-secgrp',
    description='Enable HTTP access',
    ingress=[
        { 'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0'] }
    ])
## aws ec2 server
server = aws.ec2.Instance('webserver-www',
    instance_type=size,
    security_groups=[group.name], # reference security group from above
    ami=ami.id)

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)