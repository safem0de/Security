```bash
nerdctl pull hackersploit/bwapp-docker
nerdctl run -d -p 0.0.0.0:8080:80 --name bwapp hackersploit/bwapp-docker
```
http://localhost:8080/install.php<br>
http://localhost:8080/login.php
* Username: bee
* Password: bug

Windows
```bash
netstat -ano | findstr :8080
```

WSL/Linux/macOS
```bash
netstat -tuln | grep 8080
```
```bash
netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=8080 connectaddress=127.0.0.1 connectport=8080
```
```bash
netsh interface portproxy delete v4tov4 listenport=8080 listenaddress=0.0.0.0
```
