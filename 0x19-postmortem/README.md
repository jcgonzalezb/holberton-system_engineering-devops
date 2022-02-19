# Postmortem

The following is the incident report for the demo page outrage that occurred on January 4, 2022.
Issue Summary

From 9:20 am to 9:40 am CT, after a student started a docker container, he tried to curl the port 80, but instead of getting a page that contained “Hello Holberton”, he got the following error message: curl: (7) Failed to connect to port 80: connection refused. This student was the only one affected by this incident. After an inspection, a command was inserted, and the problem was solved. The fact that the Apache program had not been initialized before the curl command was inserted caused the error mentioned.

Timeline

9:20 AM: Docker container initialized
9:25 AM: Unsuccessful curl attempt done
9:27 AM: Several tests done to check connections to different ports
9:39 AM: Apache service started. The command to start Apache was inserted on the terminal
9:40 AM: Curl attend done successfully and page containing “Hello Holberton” was returned

Root Cause

The Apache was disable when the docker container was started and it was not an easy way to notice that the Apache was disable after the docker container was initialized. At 9:25 AM the student tried a curl unsuccessfully.

Resolution and recovery

After several tests done to check connections to different ports and getting errors and messages from the container, at 9:39 AM the command to start the Apache was inserted and a curl was done. That curling port 80 successfully returned a page that contained “Hello Holberton”.

Corrective and Preventative Measures

* The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:
Every time that you are working with a web server (Apache2 in this case), the first thing that you should do is check its status and make sure that it is running properly. In case it is not running, you can start or restart the service.

* If you are new working with web servers, it is recommended to first read the manual to make sure that you are familiar with the basic commands. This could be helpful in case you are facing a problem because you can make a basic troubleshooting to avoid dealing with complex procedures that probably are not necessary.


## Author

- Juan Camilo González <a href="https://twitter.com/juankter" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="juankter" height="30" width="40" /></a>
<a href="https://bit.ly/2MBNR0t" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://bit.ly/2mbnr0t" height="30" width="40" /></a>