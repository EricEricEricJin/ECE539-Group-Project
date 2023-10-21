#!bash
src=$1/`ls $1 | grep "30280.m4s"`
dest=$2
tmpdir=/tmp/bv2audio

echo Source: $src
echo Destination: $dest

if [ ! -d $tmpdir ]
then
	mkdir $tmpdir
fi

echo -e "\n"

if [ -f $1/.videoInfo ];
then
	# parse JSON file
	artist=`grep -o '"uname":"[^"]*' $1/.videoInfo | grep -o '[^"]*' | tail -1 | sed "s/\//_/g"`
	title=`grep -o '"title":"[^"]*' $1/.videoInfo | grep -o '[^"]*' | tail -1 | sed "s/\//_/g"`
	album=`grep -o '"groupTitle":"[^"]*' $1/.videoInfo | grep -o '[^"]*' | tail -1 | sed "s/\//_/g"`
	echo Title: $title
	echo Artist: $artist
	echo Album: $album

	# remove the 9 zeros from head
	tail -c +10 $src > $tmpdir/`basename $src`

	# convert to AAC-encoded audio file with metadata
	ffmpeg -i "$tmpdir/`basename $src`" -metadata ARTIST="$artist" -metadata ALBUM="$album" -metadata TITLE="$title" -c copy "$dest/$artist-$title.m4a" \
		|| cp "$tmpdir/`basename $src`" "$dest/$artist-$title.m4a"

	# remove tmp file
	rm "$tmpdir/`basename $src`"
else
	echo "ERR: video info not found!"
fi

echo -e "\n"

