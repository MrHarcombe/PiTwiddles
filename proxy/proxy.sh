#!/bin/bash

function proxyOff {
   unset http_proxy https_proxy https-proxy ftp_proxy
   unset HTTP_PROXY HTTPS_PROXY HTTPS-PROXY FTP_PROXY

   sudo cp ~/proxy/apt.conf.proxyOff /etc/apt/apt.conf
}

function proxyOn {
   http_proxy="http://10.56.12.3:8080"
   https_proxy=$http_proxy
   https-proxy=$http_proxy
   ftp_proxy=$http_proxy
   HTTP_PROXY=$http_proxy
   HTTPS-PROXY=$http_proxy
   HTTPS_PROXY=$http_proxy
   FTP_PROXY=$http_proxy
   export http_proxy https_proxy https-proxy ftp_proxy
   export HTTP_PROXY HTTPS_PROXY HTTPS-PROXY FTP_PROXY

   sudo cp ~/proxy/apt.conf.proxyOn /etc/apt/apt.conf
}
