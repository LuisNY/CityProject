# PyCity

Simple database project.
Need to install mysql first, and set the right psw and username.
Once mysql is installed, need to run the script `db_schema.sql` to create db and table.

`>> mysql --password="..." < db_schema.sql`

Program can be executed with 

`>> python main.py`


Alternatively, you can use Docker. 

Assuming that the image of PyCity is available in docker-hub, with docker-compose you can run the application running:

`docker-compose run pycity`

Otherwise you need to modify the docker-compose.yaml file such that the PyCity image is built from the Docker file first.



