#!/bin/bash
function help { # help menu
    	echo "usage: ${0##*/} <filename>|<option>"
    	echo
    	echo "Options:"
    	echo "    -c, --clear   :   delete all .bak files in the directory"
    	echo "    -l, --list    :   list all .bak files in the directory"
    	echo "    -d, --drop    :   unbackup all .bak files in the directory"
    	echo "    --help        :   print this help"
    	echo "    --version     :   print the version"
    	exit
}

function about {
	echo -e "cbak v1.0 (c) 2018 - ThyGreg"
	echo -e "This script was written by \e[92m\e[5mGregor Löffler\e[0m."
	echo -e "Github: \e[94mhttps://github.com/g3gn\e[0m"
	exit
}

case $1 in
	-c|--clear)
		if [ -f *.bak ]; then rm *.bak; fi # remove all backups in folder
		exit
	;;

	-l|--list)
		ls | egrep '\.bak$' # list all backups in folder
		exit
	;;

	-d|--drop)
		for FILENAME in *.bak; do mv "$FILENAME" "${FILENAME%.bak}"; done # remove the extension .bak for all backups in folder
		exit
	;;

	--help)
		help # call the function help_menu
	;;

	--version)
		about # show script version
	;;

	*)
		# do nothing
	;;
esac

if [ $# = 0 ] # check if argument is empty
then
	help # call function help_menu
else
	if [[ $1 == *.bak ]] # check if file is already backuped
	then
		for FILENAME in $1; do mv "$FILENAME" "${FILENAME%.bak}"; done # remove backup if already exists
		exit 0
	else # create backup
		cp -v $1 $1.bak
		exit 0
	fi
fi
