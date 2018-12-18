#sudo apt-get update
#sudo apt-get install -y g++
#mkdir node
#cd node/
#wget https://nodejs.org/dist/v10.14.2/node-v10.14.2.tar.gz
#tar xvf node-v10.14.2.tar.gz
#cd node-v10.14.2
#./configure
#make
#sudo make install

mkdir node
cd node/
wget https://nodejs.org/dist/v10.14.2/node-v10.14.2-linux-x64.tar.xz
tar xvf node-v10.14.2-linux-x64.tar.xz
cd node-v10.14.2-linux-x64/bin/
cd /home/vagrant/.local/bin/
ln -s /vagrant/frontend/node/node-v10.14.2-linux-x64/bin/node node
ln -s /vagrant/frontend/node/node-v10.14.2-linux-x64/bin/npm npm
ln -s /vagrant/frontend/node/node-v10.14.2-linux-x64/bin/npx npx
