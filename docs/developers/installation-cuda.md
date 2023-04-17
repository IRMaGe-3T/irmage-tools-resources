### Installation of Cuda 11.1

 * Install NVidia driver 455 metapackage from Ubuntu 'Software Update Manager' icon -> 'Settings & Livepatch ...' button -> 'Additional Drivers' tab.

 * From	[NVidia documentation] (https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) :

```
get https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt update
sudo apt install cuda
sudo nvidia-modprobe
```

 * To compile samples:
```
sudo apt install freeglut3-dev
sudo chown -R userloginname /usr/local/cuda-11.1/samples
# choose a sample application
cd /usr/local/cuda-11.1/samples/1_Utilities/deviceQuery
make
# try it
../../bin/x86_64/linux/release/./deviceQuery
```