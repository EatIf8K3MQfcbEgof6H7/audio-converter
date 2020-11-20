# audio-converter

converts wma-files to mp3-files with tag-information

1. create docker image via docker 

`docker build --pull --rm -f "Dockerfile" -t ffmpegpythondockerexample2:latest "." `

2. start container with mapped local folder with mpa-files to /tmp

`docker run -t -i -v /tmp2:/tmp ffmpegpythondockerexample2`

