# Nginx - Application server for Airbnb

## Description of the files inside this folder:

2. Configure Nginx to serve page from the route '/airbnb-onepage/'. Nginx should proxy requests to the process listening on port 5000. Nginx config file updloaded.
3. Configure Nginx to proxy HTTP requests to the route '/airbnb-dynamic/number_odd_or_even/(any integer)' to a Gunicorn instance listening on port 5001. Nginx config file updloaded.
4. Configure Nginx so that the route '/api/' points to a Gunicorn instance listening on port 5002. Nginx config file updloaded.
5. Configure Nginx so that the route '/' points to your Gunicorn instance. This instance should serve content from web_dynamic/2-hbnb.py on port 5003. Nginx config file updloaded.

## Enviroment

- OS: Ubuntu 20.04 LTS
- Technologies: Gunicorn
- Web Server: Nginx

## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
