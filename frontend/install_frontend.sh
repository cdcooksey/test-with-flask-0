# Install current version of Node / NPM
mkdir node
cd node/
wget https://nodejs.org/dist/v10.14.2/node-v10.14.2-linux-x64.tar.xz
tar xvf node-v10.14.2-linux-x64.tar.xz
cd node-v10.14.2-linux-x64/bin/
cd /home/vagrant/.local/bin/
ln -s /vagrant/frontend/node/node-v10.14.2-linux-x64/bin/node node
ln -s /vagrant/frontend/node/node-v10.14.2-linux-x64/bin/npm npm
ln -s /vagrant/frontend/node/node-v10.14.2-linux-x64/bin/npx npx

# Install Angular
cd /vagrant/frontend/
npm install -g @angular/cli
cd /home/vagrant/.local/bin/
ln -s /vagrant/frontend/node/node-v10.14.2-linux-x64/lib/node_modules/@angular/cli/bin/ng ng
cd /vagrant/frontend/events-frontend
npm install
