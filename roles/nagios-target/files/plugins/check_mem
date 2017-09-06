#!/usr/bin/env bash

#Set script name
SCRIPT=`basename ${BASH_SOURCE[0]}`

#Set default values
optMW=95
optMC=98
optSW=95
optSC=98

# help function
function printHelp {
  echo -e \\n"Help for $SCRIPT"\\n
  echo -e "Basic usage: $SCRIPT -w {warning} -c {critical} -W {warning} -C {critical}"\\n
  echo "Command switches are optional, default values for warning is 95% and critical is 98%"
  echo "-w - Sets warning value for Memory Usage. Default is 95%"
  echo "-c - Sets critical value for Memory Usage. Default is 98%"
  echo "-W - Sets warning value for Swap Usage. Default is 95%"
  echo "-C - Sets critical value for Swap Usage. Default is 98%"
  echo -e "-h  - Displays this help message"\\n
  echo -e "Example: $SCRIPT -w 80 -c 90 -W 40 -C 60"\\n
  echo -e \\n\\n"Author: Lukasz Gogolin, lukasz.gogolin@gmail.com"
  echo -e "Git: http://bitbucket.org/lgogolin/nagios_plugins"
  exit 1
}

# regex to check is OPTARG an integer
re='^[0-9]+$'

while getopts :w:c:W:C:h FLAG; do
  case $FLAG in
    w)
      if ! [[ $OPTARG =~ $re ]] ; then
        echo "error: Not a number" >&2; exit 1
      else
        optMW=$OPTARG
      fi
      ;;
    c)
      if ! [[ $OPTARG =~ $re ]] ; then
        echo "error: Not a number" >&2; exit 1
      else
        optMC=$OPTARG
      fi
      ;;
    W)
      if ! [[ $OPTARG =~ $re ]] ; then
        echo "error: Not a number" >&2; exit 1
      else
        optSW=$OPTARG
      fi
      ;;
    C)
      if ! [[ $OPTARG =~ $re ]] ; then
        echo "error: Not a number" >&2; exit 1
      else
        optSC=$OPTARG
      fi
      ;;
    h)
      printHelp
      ;;
    \?)
      echo -e \\n"Option - $OPTARG not allowed."
      printHelp
      exit 2
      ;;
  esac
done

shift $((OPTIND-1))





array=( $(cat /proc/meminfo | egrep 'MemTotal|MemFree|Buffers|Cached|SwapTotal|SwapFree' |awk '{print $1 " " $2}' |tr '\n' ' ' |tr -d ':' |awk '{ printf("%i %i %i %i %i %i %i", $2, $4, $6, $8, $10, $12, $14) }') )

memTotal_k=${array[0]}
memTotal_b=$(($memTotal_k*1024))
memFree_k=${array[1]}
memFree_b=$(($memFree_k*1024))
memBuffer_k=${array[2]}
memBuffer_b=$(($memBuffer_k*1024))
memCache_k=${array[3]}
memCache_b=$(($memCache_k*1024))
memTotal_m=$(($memTotal_k/1024))
memFree_m=$(($memFree_k/1024))
memBuffer_m=$(($memBuffer_k/1024))
memCache_m=$(($memCache_k/1024))
memUsed_b=$(($memTotal_b-$memFree_b-$memBuffer_b-$memCache_b))
memUsed_m=$(($memTotal_m-$memFree_m-$memBuffer_m-$memCache_m))
memUsedPrc=$((($memUsed_b*100)/$memTotal_b))

swapTotal_k=${array[5]}
swapTotal_b=$(($swapTotal_k*1024))
swapFree_k=${array[6]}
swapFree_b=$(($swapFree_k*1024))
swapUsed_k=$(($swapTotal_k-$swapFree_k))
swapUsed_b=$(($swapUsed_k*1024))
swapTotal_m=$(($swapTotal_k/1024))
swapFree_m=$(($swapFree_k/1024))
swapUsed_m=$(($swapTotal_m-$swapFree_m))

if [ $swapTotal_k -eq 0 ]; then
    swapUsedPrc=0
else
    swapUsedPrc=$((($swapUsed_k*100)/$swapTotal_k))
fi

message="[MEMORY] Total: $memTotal_m MB - Used: $memUsed_m MB - $memUsedPrc% [SWAP] Total: $swapTotal_m MB - Used: $swapUsed_m MB - $swapUsedPrc% | MTOTAL=$memTotal_b;;;; MUSED=$memUsed_b;;;; MCACHE=$memCache_b;;;; MBUFFER=$memBuffer_b;;;; STOTAL=$swapTotal_b;;;; SUSED=$swapUsed_b;;;;"


if [ $memUsedPrc -ge $optMC ] || [ $swapUsedPrc -ge $optSC ]; then
  echo -e $message
  $(exit 2)
elif [ $memUsedPrc -ge $optMW ] || [ $swapUsedPrc -ge $optSW ]; then
  echo -e $message
  $(exit 1)
else
  echo -e $message
  $(exit 0)
fi

