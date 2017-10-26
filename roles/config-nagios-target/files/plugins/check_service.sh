#!/usr/bin/env bash

# Nagios Exit Codes
OK=0
WARNING=1
CRITICAL=2
UNKNOWN=3

systemctl status $1
rc1=$?

case $rc1 in
0)
	systemctl is-active $1 &>/dev/null
	rc2=$?

	case $rc2 in
	0)
	        exit $OK
	        ;;
	*)
		exit $WARNING
		;;
	esac
	;;
*)
        exit $CRITICAL
        ;;
esac

exit $UNKNOWN
