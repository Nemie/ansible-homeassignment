# ansible-homeassignment

Temporary repository for a home assignment

---

#### Required ansible modules

boto ( python 2.7 ) / boto3 ( python 3 )

`pip3 install --user boto3`

---

### Needed before starting

* You need to update the vars vault in `ansible/group_vars/all/vault.yml` with your own AWS access and secure key, DB username, DB password and DB host.
 * Password is: `ChangeMe#123`
* You need to create a `security group` in AWS with inbound permissions for port 80 (everyone) and port 22 (only your own ip as source)
* Then update the variables:
  * `security_group` in `ansible/group_vars/all/vars.yml` with the name you gave the new security group.
  * `vpc_subnet` with the subnet you wish to use for your host.
  * `project_name` with the name of your project, it will be used for the keypair that will be created.
  * Any of the other settings you might want to change for the setup.

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

 * [DB App Cloudfront](https://d2z9ytrf7s3dej.cloudfront.net)

 * [DB APP External URL](http://dbapp.skutt.net)

---

##### For DB App ( that is separate due to that it was finished later )



Files for this app is under **REPO/dbapp** including **requirements.txt** and **Dockerfile**.

* Create a development RDS Mysql instance and add your newly created **security_group** when setting it up ( for simplicity ).
* Also add **inbound permission** in your `security_group` in AWS for port **3306** with your created hosts **private ip as source**.
* Create DB and Table for user registration.

`CREATE DATABASE IF NOT EXISTS `ansibletest` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `ansibletest`;

CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
);`

* Manually created openssl keypair on the host for mysql backups:
`openssl req -x509 -nodes -newkey rsa:2048 -keyout mysqldump-key.priv.pem -out mysqldump-key.pub.pem`

* Manually created .mysqldump on the host.

* Included tasks to create cronjob for mysqldump in `setup-instances` role.

* Manually created ssh-keys for the host and added the public key to github.

* Manually cloned the ansible-homeassignment repo to the host.

---

#### Decrypting backups

* openssl smime -decrypt -in [filename].sql.gz.enc -binary -inform DEM -inkey mysqldump-key.priv.pem -out [filename].sql.gz
gzip -d [filename].sql.gz
