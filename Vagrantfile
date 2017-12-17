# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/xenial64"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  #config.vm.network "forwarded_port", guest: 8080, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 8888, host: 8888, host_ip: "127.0.0.1"
  # config.vm.network "forwarded_port", guest: 27017, host: 27017, host_ip: "127.0.0.1"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.


  config.vm.provision "file", source: "~/.gitconfig", destination: ".gitconfig"

  #mongodb instance to run the game server
  config.vm.provision "docker" do |d|
    d.run "mongo",
      image: "mongo:3.4",
      args: "-v '/data:/data/db' -p 27017:27017"
  end

  # install dependencies
  config.vm.provision "shell", inline: <<-SHELL
  sudo apt-get update
  sudo apt-get install -y zsh curl python3 python3-venv
  sudo apt-get install -y ruby ruby-dev gcc make
  git clone git://github.com/robbyrussell/oh-my-zsh.git .oh-my-zsh
  cp .oh-my-zsh/templates/zshrc.zsh-template .zshrc
  sudo chsh -s /bin/zsh ubuntu

  sudo echo "
  source ~/python3/bin/activate
  cd /vagrant
  export PYTHONPATH=$PYTHONPATH:/vagrant
  " >> .zshrc
  SHELL

  # do some more setup as a non-priviliged user
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
  pyvenv python3
  . ./python3/bin/activate
  pip install --upgrade pip
  pip install docker-compose

  cd /vagrant
  pip install -r requirements.txt
  SHELL

end