# wifi_setup.sh
#!/bin/bash

sudo apt update
sudo apt install hostapd dnsmasq -y

# Configurar hostapd
sudo bash -c 'cat > /etc/hostapd/hostapd.conf <<EOF
interface=wlan0
driver=nl80211
ssid=PhotoServer
hw_mode=g
channel=6
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=CanonServer
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
EOF'

sudo sed -i 's|#DAEMON_CONF="".*|DAEMON_CONF="/etc/hostapd/hostapd.conf"|g' /etc/default/hostapd

# Configurar dnsmasq
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
sudo bash -c 'cat > /etc/dnsmasq.conf <<EOF
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
EOF'

# Configurar interfaces de red
sudo bash -c 'cat >> /etc/dhcpcd.conf <<EOF
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
EOF'

sudo bash -c 'cat > /etc/network/interfaces <<EOF
source-directory /etc/network/interfaces.d
EOF'

sudo rfkill unblock wlan
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd
sudo systemctl start dnsmasq
sudo systemctl start hostapd
sudo systemctl enable dnsmasq
sudo systemctl enable hostapd
