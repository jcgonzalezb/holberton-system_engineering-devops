# Bash - MySQL

## Description of the files inside this folder:

> SQL is installed on both Nginx web servers and configured so that the first is the Primary and the second is a Replica.

0. The file 4-mysql_configuration_primary is the MySQL primary configuration (my.cnf or mysqld.cnf).
1. The file 4-mysql_configuration_replica is the MySQL replica configuration (my.cnf or mysqld.cnf).
2. Bash script that generates a MySQL dump and creates a compressed archive out of it.

## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Bash script
- Web Servers: Installed ufw firewall on web-01, web-02 running Nginx. MySQL distribution 5.7.x installed on both servers
- Load Balancer: Installed ufw firewall on lb-01 running HAProxy, SSL
- Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)

<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://github.com/odb/official-bash-logo/blob/master/assets/Logos/Icons/SVG/48x48_white.svg" alt="bash" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
