#!/bin/bash
sudo apt-get install -y \
apt-transport-https \
ca-certificates \
curl \
gnupg2 \
software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/debian \
$(lsb_release -cs) \
stable"
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
sudo apt-get install -y docker-ce=5:18.09.3~3-0~debian-stretch docker-ce-cli=5:18.09.3~3-0~debian-stretch containerd.io"
