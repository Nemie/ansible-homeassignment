# ansible-homeassignment
Temporary repository for a home assignment

##### Required ansible modules

boto ( python 2.7 ) / boto3 ( python 3 )

`pip3 install --user boto3`

##### Needed before starting

* You need to update the vars vault in `ansible/group_vars/all/vault.yml` with your own AWS access and secure key.
 * Password is: `ChangeMe#123`
* You need to create a security group in AWS with permissions for port 80 (everyone) and port 22 (your own ip only)
* Then update the variable `security_group` in `ansible/group_vars/all/vars.yml` with the name you gave the new security group.

### Ansible Commands

*Work from the **ansible** folder:  `cd ansible`*

#### Create an EC2 host(s) and add entries to inventories

`ansible-playbook --ask-vault-pass -i inventory aws.yml -v`

#### Setup Created Host(s)

`ansible-playbook --ask-vault-pass -i inventory setup-instances.yml -v`


#### Remove Created Host(s) and entries in inventories

`ansible-playbook --ask-vault-pass -i inventory terminate-aws.yml -v`


##### URLs

* The direct link to the cloudfront distribution
 * [Cloudfront Link](https://d3pjnsjeewswwe.cloudfront.net/)
* The domain url
 * [External Url](http://homeassignment.skutt.net)
