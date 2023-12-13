rm -rf audio
mkdir -p audio

grep ')' embed.txt | while read -r line 
do
	key=$(echo "$line" | cut -d')' -f1)
	value=$(echo "$line" | cut -d')' -f2)
	echo "Generating audio for $key: ${value:1}"
	gtts-cli --lang en --tld co.uk "${value:1}" --output "audio/$key.mp3"
	ffmpeg -nostdin -i "audio/$key.mp3" "audio/$key.wav"
done
