# HTTPS SSL

## Description of the files inside this folder:

0. Bash script that will display information about subdomains.
1. Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www. The file 1-haproxy_ssl_termination is the HAproxy configuration file. HAproxy is listening to port TCP 443 and accepts SSL traffic.


## Languages and Tools:

- OS: Ubuntu 20.04 LTS
- Language: Bash script
- Web Servers: web-01, web-02 Nginx
- Load Balancer: lb-01, (www) HAproxy
- Domain name from [.TECH Domains](https://get.tech/)
- Style guidelines: [Shellcheck](https://github.com/koalaman/shellcheck)

<p align="left"> <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"> <img src="https://github.com/odb/official-bash-logo/blob/master/assets/Logos/Icons/SVG/48x48_white.svg" alt="bash" width="40" height="40"/> </a> </p>


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>
