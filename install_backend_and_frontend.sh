cd /vagrant/frontend/
./install_frontend.sh

echo "----------------------------------------------"
echo " The backend will run now automatically. Run  "
echo " the frontend by opening another terminal and "
echo " do:                                          "
echo " cd frontend/events-frontend/                 "
echo " ./run_angular.sh                             "
echo "                                              "
echo " After kicking off the frontend, open a web   "
echo " browser and go to: http://0.0.0.0:4200/      "
echo "----------------------------------------------"

cd /vagrant/backend/
./run_flask.sh
