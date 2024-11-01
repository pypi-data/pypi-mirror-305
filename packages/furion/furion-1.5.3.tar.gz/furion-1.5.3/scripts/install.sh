#!/bin/bash

# Exit on error
set -e

INSTALL_PATH=/usr/local/furion

function check_sanity {
	if [[ $(id -u) != "0" ]]; then
		die 'Must be run by root user'
	fi
	if [[ -z $(echo `which python`) ]]; then
		die "Cannot find python"
	fi
}

function check_install {
	if [[ -d $INSTALL_PATH ]]; then
		cd $INSTALL_PATH
		print_info "Already installed, trying to upgrade..."
		if [[ -d .git ]]; then
			git pull
		elif [[ -d .hg ]]; then
			hg pull && hg up
		else
			die "Not a git or hg repo, cannot upgrade. Please remove $INSTALL_PATH and try again."
		fi

		DIFF=$(echo `diff examples/furion_$1.cfg furion.cfg`)
		if [[ -n $DIFF ]]; then
			read -r -p "A new furion.cfg is found, update and override your local changes? (y/n):"
			if [[ $REPLY =~ ^[Yy]$ ]]; then
				cp -f examples/furion_$1.cfg furion.cfg
			fi
		fi

		if [[ $1 == "client" ]]; then
			if [[ -f upstream.json ]]; then
				DIFF=$(echo `diff examples/latest_upstream.json upstream.json`)
				if [[ -n $DIFF ]]; then
					read -r -p "A new upstream.json is found, update and override your local changes? (y/n):"
					if [[ $REPLY =~ ^[Yy]$ ]]; then
						cp -f examples/latest_upstream.json upstream.json
					fi
				fi
			else
				cp -f examples/latest_upstream.json upstream.json
			fi
		fi
			
		print_info "Restarting service..."
		case $OSTYPE in
			darwin*)
                if [[ -f /Library/LaunchDaemons/hu.keli.furion.plist ]]; then
                    launchctl unload /Library/LaunchDaemons/hu.keli.furion.plist
                    rm -f /Library/LaunchDaemons/hu.keli.furion.plist
                    cp -f examples/org.furion.plist /Library/LaunchDaemons/
                    launchctl load /Library/LaunchDaemons/org.furion.plist
                else
                    launchctl unload /Library/LaunchDaemons/org.furion.plist
                    launchctl load /Library/LaunchDaemons/org.furion.plist
                fi
				;;
			linux*)
				service furion restart
				;;
		esac
			
		print_info "Upgrade finished."
		exit 0
	fi
}

function die {
	echo "ERROR:" $1 > /dev/null 1>&2
	exit 1
}

function print_info {
	echo -n $'\e[1;36m'
	echo -n $1
	echo $'\e[0m'
}

function usage {
	cat << EOF 
Usage:
$0 client # install furion as a client (use upstream servers as proxies) 
$0 server # install furion as a server (acting as an upstream proxy server) 
EOF
	exit
}

function download {
	GIT=$(echo `which git`)
	HG=$(echo `which hg`)

	if [[ -f furion.py ]]; then
		print_info "Copying $PWD to $INSTALL_PATH..."
		cp -r "$PWD" /usr/local/furion
		return
	fi
	if [[ -n $GIT ]]; then
		git clone https://github.com/keli/furion.git $INSTALL_PATH
	elif [[ -n $HG ]]; then
		hg clone https://bitbucket.org/keli/furion $INSTALL_PATH
	else
		die "Can't find git or hg in your system, install one of them first."
	fi
}

function prepare_server {
	cd $INSTALL_PATH
	cp examples/furion_server.cfg furion.cfg
	cp examples/simpleauth.passwd .

	openssl req \
		-x509 -nodes -days 3650 \
		-subj "/C=US/ST=CA/L=LA/CN=$1.com" \
		-newkey rsa:2048 -keyout furion.pem -out furion.pem
}

function prepare_client {
	cd $INSTALL_PATH
	cp examples/furion_client.cfg furion.cfg
	cp examples/latest_upstream.json upstream.json
}

function install {
	check_sanity
	check_install $1
	print_info "Installing Furion as $1..."
	case $OSTYPE in
		darwin*)
			download
			prepare_$1 `date | md5 | head -c 10`
			cp -f examples/org.furion.plist /Library/LaunchDaemons/
			launchctl load /Library/LaunchDaemons/org.furion.plist
			;;	
		linux*)
			if [ ! -f /etc/debian_version ]; then
				die "The script supports only Debian for now."
			fi
			download
			prepare_$1 `date | md5sum | head -c 10`
			cp -f examples/furion.init /etc/init.d/furion
			update-rc.d furion defaults
			service furion start
			;;
	esac		
	print_info "Installation Complete."
}

[[ $# < 1 ]] && usage

case $1 in
	client|server)
		install $1
		;;
	*)
		usage
		;;
esac
