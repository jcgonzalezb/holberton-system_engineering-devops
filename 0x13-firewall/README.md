# Firewall

## Description of the files inside this folder:

0. Bash script that installs ufw firewall; block all incoming except these TCP ports: 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP).
1. Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP. The file 100-port_forwarding is the ufw configuration file.

## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Bash script
- Web Servers: Installed ufw firewall on web-01, web-02 running Nginx
- Load Balancer: Installed ufw firewall on lb-01 running HAProxy, SSL
- Domain name from [.TECH Domains](https://get.tech/)
- Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)

<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://github.com/odb/official-bash-logo/blob/master/assets/Logos/Icons/SVG/48x48_white.svg" alt="bash" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
