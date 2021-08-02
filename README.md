# slightly-efficient-nmap-scan

A python script which makes your nmap scan *slightly* more efficient by:  
1. Running an nmap scan to just discover open ports  
2. Then running another nmap scans with the -A flag only on the open ports discovered in step 1  
  
<h3>Running the script</h3>

1. <code>chmod +x scan.py</code>
2. <code>./scan.sh 127.0.0.1</code> where 127.0.0.1 is the IP you need to scan  

<h3>Requirements</h3>

Needless to say, you should have nmap already installed.

<h3>P.S</h3>
Please do not scan IP addresses that you do not have the permission to.
