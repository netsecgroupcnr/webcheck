# webcheck

This program allows you to check the status of your web server, while stress testing activities are accomplished, by adopting low-rate denial of service tools.

### Introduction ###

This software is a support software adopted for research purposes, during the execution of Slow Denial of Service Attacks against [Apache2](https://apache.org) web server.
The program provides a graphical web interface reporting the status of the server and the effects of a running attack.

### Preliminary requirements ###

Following requirements should be satisfied:
* Stress testing activities are executed on a system under the control of the tester, and the tester is responsible for such system
* Adoption of a Slow DoS Attack like [SlowDroid](http://www.netsec.ieiit.cnr.it/activities_transfer.html)
* Adoption of the [Apache2](https://apache.org) web server

### Installation ###

1. Access the system as `root`

2. `cd` into the `/root` directory
```
cd /root
```

3. Clone the repository
```
git clone https://github.com/netsecgroupcnr/webcheck.git
```

4. `cd` into the `webcheck` directory
```
cd webcheck
```

5. Run the following command to install Python dependencies:
```
pip install -r requirements.txt
```

### Configuration ###

Configuration is accomplished by replacing the `MAX` variable value (default to `150`) with the maximum number of simultaneous connections the server is able to manage.
Such information can be retrieved easily, by looking at the [Max* directives of Apache2](https://cmdref.net/middleware/web/httpd/maxclients.html).

### Execution ###

Open two different `root` shells and `cd` into the `/root/webcheck` directory, hence run the following commands:
* `sh savestatus.sh`
* `python checkServer.py`

### Generated output ###

At this point, it's possible to check the status of the server, by accessing through a common web browser to the http://hostname:8000 address, where `hostname` identifies the hostname/IP address of the server.

### References ###

Some relevant [scientific papers](https://scholar.google.it) are the following ones:
* Cambiaso, E., Papaleo, G., Chiola, G., & Aiello, M. (2013). Slow DoS attacks: definition and categorisation. International Journal of Trust Management in Computing and Communications, 1(3-4), 300-319.
* Cambiaso, E., Papaleo, G., & Aiello, M. (2012, October). Taxonomy of slow DoS attacks to web applications. In International Conference on Security in Computer Networks and Distributed Systems (pp. 195-204). Springer, Berlin, Heidelberg.
* Aiello, M., Papaleo, G., & Cambiaso, E. (2014). SlowReq: a weapon for cyberwarfare operations. Characteristics, limits, performance, remediations. In International Joint Conference SOCO’13-CISIS’13-ICEUTE’13 (pp. 537-546). Springer, Cham.
* Cambiaso, E., Papaleo, G., & Aiello, M. (2014, August). Slowdroid: Turning a smartphone into a mobile attack vector. In 2014 International Conference on Future Internet of Things and Cloud (pp. 405-410). IEEE.
* Cambiaso, E., Papaleo, G., & Aiello, M. (2017). Slowcomm: Design, development and performance evaluation of a new slow DoS attack. Journal of Information Security and Applications, 35, 23-31.
* Cambiaso, E., Papaleo, G., Chiola, G., & Aiello, M. (2015). Designing and modeling the slow next DoS attack. In International Joint Conference (pp. 249-259). Springer, Cham.

Other related works can be found at [www.netsec.ieiit.cnr.it](http://www.netsec.ieiit.cnr.it).

### License ###

The program is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/).

### Contacts ###

This program is implemented by the [NetSec group of CNR-IEIIT](http://www.netsec.ieiit.cnr.it).

Credits:
 * Idea:
   * Enrico Cambiaso
 * Design:
   * Enrico Cambiaso
 * Development:
   * Enrico Cambiaso
 * Support:
   * Maurizio Aiello
   * Gianluca Papaleo
