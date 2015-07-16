#!/bin/bash

#echo `hg log -v -b xxxx -u user -M --template "{files} "`|sed -e 's/\ /\n/g' |sort -u

function helpdoc()
{
echo "Show revision files of the specified user in the specified branch"
echo "Options:"
echo "    -b branchName.         Give branch name,default is current branch"
echo "    -u userName.           Give user name,default is hg user"
echo "    -h                     Give this help"
}

HGBRANCH=`hg branch`
HGUSER=`hg showconfig ui.username|cut -d ' ' -f 1`

while getopts ":b:u:h" optname
	do
		case "$optname" in
			"b")
			HGBRANCH=$OPTARG
			;;
			"u")
			HGUSER=$OPTARG
			;;
			"h")
			helpdoc
			exit 0
			;;
			"?")
			echo "Unknown option $OPTARG"
			helpdoc
			exit 2
			;;
			":")
			echo "No argument,for $OPTARG"
			helpdoc
			exit 2
			;;
			*)
			echo "Unknow error"
			helpdoc
			exit 2
			;;
		esac
	done

HGUSER=${HGUSER%% *} #delete the character after the space\
if [ ""!="$HGUSER" ] 
then
	echo `hg log -v -b ${HGBRANCH} -u ${HGUSER} -M --template "{files} "`|sed -e 's/\ /\n/g' |sort -u
else
	echo "user name is empty!!!"
	helpdoc
	exit 2
fi
	

