# selenium_ubuntu

### First, make sure Python and pip are installed on your server.
```sh
sudo apt update
sudo apt install python3 python3-pip -y

```

### Install Requirements.txt
```sh
pip3 install -r requirements.txt
```

### Install Google Chrome
```sh
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

### Install ChromeDriver

```sh
wget https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
```