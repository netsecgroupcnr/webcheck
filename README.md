# webcheck

This program allows you to check the status of your web server, while stress testing activities are accomplished, by adopting low-rate denial of service tools.

### Introduction ###

TODO

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

### Analysis ###

At this point, it's possible to check the status of the server, by accessing through a common web browser to the http://hostname:8000 address, where `hostname` identifies the hostname/IP address of the server.

### Output ###

TODO

### References ###

TODO

### License ###

The program is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/).

### Contacts ###

This program is implemented by the [NetSec group of CNR-IEIIT](http://www.netsec.ieiit.cnr.it).
