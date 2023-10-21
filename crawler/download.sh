for x in `cat BV.txt`;
do
	if [ ! -f $x.mp3 ];
	then
		echo Downloading $x;
		# download
		bilili.exe https://www.bilibili.com/video/$x -q 16 -d D:/vv -y;
		# convert
		ffmpeg -i D:/vv/*/Videos/*.mp4 $x.mp3;
		# clean
		rm -r D:/vv;
	
	else
		echo $x already downloaded.;
	fi;
done;
