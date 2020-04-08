# ansible-homeassignment
Temporary repository for a home assignment
---
#### Required ansible modules

boto ( python 2.7 ) / boto3 ( python 3 )

`pip3 install --user boto3`
---
### Needed before starting

* You need to update the vars vault in `ansible/group_vars/all/vault.yml` with your own AWS access and secure key.
 * Password is: `ChangeMe#123`
* You need to create a `security group` in AWS with inbound permissions for port 80 (everyone) and port 22 (only your own ip as source)
* Then update the variable `security_group` in `ansible/group_vars/all/vars.yml` with the name you gave the new security group.
---
### Ansible Commands

*Work from the **ansible** folder:  `cd ansible`*

#### Create an EC2 host(s) and add entries to inventories

`ansible-playbook --ask-vault-pass -i inventory aws.yml -v`

#### Setup Created Host(s)

`ansible-playbook --ask-vault-pass -i inventory setup-instances.yml -v`

---
#### Remove Created Host(s) and entries in inventories

When all done testing the setup, you can use this to clean up aws and your inventory files for a fresh start.

`ansible-playbook --ask-vault-pass -i inventory terminate-aws.yml -v`

---
##### URLs


 * [Cloudfront](https://d3pjnsjeewswwe.cloudfront.net/)

 * [External Url](http://homeassignment.skutt.net)

---

##### Steps removed since I skipped DB setup in the end

I got things working-ish, an app where you could register a user and it was supposed to be added to a database, but for some reason it doesn't and the app gives 200.

* Create a development RDS Mysql instance and add your newly created **security_group** when setting it up ( for simplicity ).
* Also add **inbound permission** in your `security_group` in AWS for port **3306** with your created hosts **private ip as source**.
* Create DB and Table for user registration.
