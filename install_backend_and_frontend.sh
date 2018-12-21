cd /vagrant/frontend/
./install_frontend.sh

cd /vagrant/backend/
./install.sh

echo "---------------------------------------------------"
echo " The backend will run now automatically.  You      "
echo " can access the backend directly at these endpoints"
echo " endpoints:                                        "
echo "                                                   "
echo " GET http://0.0.0.0:5000/api/v1/events             "
echo " GET http://0.0.0.0:5000/api/v1/events/1           "
echo " PUT http://0.0.0.0:5000/api/v1/events             "
echo "                                                   "
echo " Run the frontend by opening another terminal and  "
echo " do:                                               "
echo "                                                   "
echo " cd frontend/events-frontend/                      "
echo " ./run_angular.sh                                  "
echo "                                                   "
echo " After kicking off the frontend, open a web        "
echo " browser and go to: http://0.0.0.0:4200/           "
echo "---------------------------------------------------"

./run_flask.sh
