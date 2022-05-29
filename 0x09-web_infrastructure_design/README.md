# Web infrastructure design

## Description of the files inside this folder:

Inside each answer file, there is a link to the screenshot of the requested diagram. All screenshots were uploaded on imgur.

0. Simple web stack
1. Distributed web infrastructure
2. Secured and monitored web infrastructure

### Simple web stack

One server web infrastructure that hosts the website that is reachable via www.foobar.com.
Must have:
- 1 server
- 1 web server (Nginx)
- 1 application server
- 1 application files (your code base)
- 1 database (MySQL)
- 1 domain name foobar.com configured with a www record that points to your server IP 8.8.8.8

![Simple web infrastructure](https://github.com/jcgonzalezb/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/stacks/Simple%20Web%20Stack%20-%20Imgur.jpg)




### Distributed web infrastructure
Three server web infrastructure that hosts the website www.foobar.com.
Must have:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

![Distributed web infrastructure](https://github.com/jcgonzalezb/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/stacks/Distributed%20web%20infrastructure%20-%20Imgur.jpg)


### secured and monitored infrastructure

Three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
Must have:
- 2 servers
- 1 web server (Nginx)
- 1 application server
- 1 load-balancer (HAproxy)
- 1 set of application files (your code base)
- 1 database (MySQL)

![Secured and monitored infrastructure](https://github.com/jcgonzalezb/holberton-system_engineering-devops/blob/master/0x09-web_infrastructure_design/stacks/Secured%20and%20monitored%20web%20infrastructure%20-%20Imgur.jpg)











## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>







