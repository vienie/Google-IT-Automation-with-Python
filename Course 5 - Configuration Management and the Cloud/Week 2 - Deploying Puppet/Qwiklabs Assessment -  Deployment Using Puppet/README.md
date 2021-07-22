## Introduction
You want to automatically manage the computers in your company's fleet, including a number of different machines with different operating systems. You've decided to use Puppet to automate the configurations on these machines. Part of the setup is already done, but there are more rules that need to be added, and more operating systems to consider.

### Puppet rules
The goal of this exercise is for you to see what Puppet looks like in action. During this lab, you'll be connecting to two different VMs. The VM named puppet is the Puppet Master that has the Puppet rules that you'll need to edit. The VM named linux-instance is a client VM that you'll use to test that your catalog was applied successfully.

The manifests used for the production environment are located in the directory /etc/puppet/code/environments/production/manifests, which contains a site.pp file with the node definitions that will be used for this deployment. On top of that, the modules directory contains a bunch of modules that are already in use. You'll be extending the code of this deployment to add more functionality to it.

### Install packages
```
cd /etc/puppet/code/environments/production/modules/packages
```
(On this Github: File for this is /packages/manifest/init.pp)

### Fetch machine information
```
cd /etc/puppet/code/environments/production/modules/machine_info
```
(On this Github: file for this is /machine_info/manifest/init.pp)

### Puppet Templates
```
cd /etc/puppet/code/environments/production/modules/machine_info
```
(On this Github: file for this is /machine_info/template/info.erb)

### Reboot machine

Create a new directory: 
```
sudo mkdir -p /etc/puppet/code/environments/production/modules/reboot/manifests 
```
Change to dir:
```
cd /etc/puppet/code/environments/production/modules/reboot/manifests
```
(On this Github: file for this is /reboot/manifests/init.pp)

Lastly, edit the site.pp file
```
sudo nano /etc/puppet/code/environments/production/manifests/site.pp 
```
(On this Github: file for this is site.pp)


Note: remember to test for each step on the linux-instance VM, run this: 
```
sudo puppet agent -v --test 
```
