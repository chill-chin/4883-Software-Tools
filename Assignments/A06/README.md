# A06 - Software Tool Presentation
## Chintan Mehta

## Software Tools:

| Tool  | Description        |
| -------- | ------------------------------- |
|  **WinSCP**  | [FTP Client w GUI](https://winscp.net/eng/docs/feature_index) |
|  **PuTTY**  | [SSH/Telnet Client](https://www.putty.org/)  |

## Goal

* Achieve **_Secure Remote Server Management_** using **WinSCP** & **PuTTY**.

## Terminology

1. **Network Protocol:** A set of rules that govern the communication between devices on a computer network (e.g. IP, TCP, HTTP).

    1. **SSH:** Secure Shell (SSH) is used for **_secure remote communication_** between two devices over an **_insecure network_**.

    2. **SFTP, SCP:** Subsystem networking protocols operating over SSH.

<img align="center" width="600" height="330" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A06/1_SSH.png">

2. **WinSCP:** Windows Secure Copy (WinSCP) is a SFTP client for Windows. It allows **_secure file transfers_** & **_graphical file management_** between a local machine and a remote server. 
    - Some **features** include GUI, directory vizualization, scripting, file synchronization, and file encryption. 

3. **PuTTY:** PuTTY is an SSH, Telnet client that focuses on **_remote server access_** & **_command execution_**.
    - Some **features** include secure login, terminal emulation, port forwarding, and SSH key management.

## Demo

* **Scenario:** Connect with the web server using SSH and backup files to local client. 

    1. **Download** & **Setup** WinSCP, PuTTY.

    2. PuTTY's ***plink - command-line utility*** helps establish a SSH connection.

            "C:\Program Files\PuTTY\plink.exe" -ssh chamoy@stampede2.tacc.utexas.edu

        * Path to *plink.exe*: `"C:\Program Files\PuTTY\plink.exe"`
        * SSH Connection details: `-ssh chamoy@stampede2.tacc.utexas.edu`

    3. **Connection Confirmation:**
       <img align="center" width="600" height="20" src="https://github.com/chill-chin/4883-Software-Tools/blob/main/Assignments/A06/2_Confirmation.png">
