# Department of Earth, Planetary, and Space Sciences at UCLA #
## Mustard -  A Mineral Collection Database and catalog ## 

This Project is the development environment for the mineral database. 
The complete project will be released under a different name 

## Before beginning: ## 
  
### Install: ###
* [Vagrant](https://www.vagrantup.com/)
* [Virtualbox](https://www.virtualbox.org/)
* [Ansible](https://www.ansible.com/)

This setup uses Vagrant to launch a virtualbox VM (Ubuntu 18.4 LTS), and Ansible to provision the machine. 

The site is accesible at http://10.11.55.66:8000 by default.


### To Use: ###
* `cd` into the folder you will work from, in my case `~/Projects/`
* `git clone https://github.com/sixtycycles/mineralDB.git`  
* `cd mineralDB/`
* `vagrant up`
* wait for ansible to finish, hopefully no errors. 
* `vagrant ssh`
* run this command from the ssh session:
    * `sudo uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data` 
* navigate to `http://10.11.55.66:8000` in a browser and play around!


