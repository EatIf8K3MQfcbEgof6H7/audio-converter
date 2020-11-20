# audio-converter

converts wma to mp3 with tag-information

Beware: wma-sourcefiles will be deleted, so use copies of the files

1. create docker image via docker 

`docker build --pull --rm -f "Dockerfile" -t ffmpegpythondockerexample2:latest "." `

2. start container with mapped localfolder /tmp2 with mpa-files to /tmp

`docker run -t -i -v /tmp2:/tmp ffmpegpythondockerexample2`




