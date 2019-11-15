import os
import sys

import pulumi
import pulumi_aws as aws

import socket


import os

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name)
from local_settings import PUBLIC_KEY



## Settings
EC2_SIZE = 't2.micro'
EC2_KEY_NAME = 'MY TEST KEY'


## AWS
#
## aws ami
ami = aws.get_ami(most_recent="true",
                  owners=['195777427543'],
                  filters=[{"name":"name","values":["195777427543/ez_django_02"]}])
## aws security group
group = aws.ec2.SecurityGroup('webserver-secgrp',
    description='Enable HTTP access',
    ingress=[
        {'protocol': 'tcp', 'from_port': 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0']},
        {'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0']},
        {'protocol': 'tcp', 'from_port': 443, 'to_port': 443, 'cidr_blocks': ['0.0.0.0/0']}
    ],
    egress=[
        {'protocol': 'tcp', 'from_port': 80, 'to_port': 80, 'cidr_blocks': ['0.0.0.0/0']},
        {'protocol': 'tcp', 'from_port': 443, 'to_port': 443, 'cidr_blocks': ['0.0.0.0/0']}

    ])

## aws key pair
key_pair = aws.ec2.key_pair.KeyPair(
    resource_name=EC2_KEY_NAME,
    key_name=EC2_KEY_NAME,
    public_key=PUBLIC_KEY
)

## aws ec2 server
server = aws.ec2.Instance('webserver-www',
    instance_type=EC2_SIZE,
    security_groups=[group.name], # reference security group from above
    ami=ami.id,
    key_name=EC2_KEY_NAME,
  )



pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)