# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "private_network", ip: "10.11.55.66"
  #config.vm.host_name = 'mineralDB.local'
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--memory", "2048"]
    vb.customize ["modifyvm", :id, "--cpus", "1"]
  end

  config.vm.synced_folder "code/", "/srv/project_code/"

  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = '2.0'
    ansible.playbook = "localdev_playbook.yml"
    ansible.host_vars = {
        "default" => {
            "ansible_python_interpreter" => "/usr/bin/python3"
        }
    }

  end
end
