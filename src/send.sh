echo "Sending audio files to ELMO..."
address="192.168.0.$1"
scp audio/*.wav idmind@"$address":elmo-v2/src/static/sounds
