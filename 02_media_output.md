## media_output

Note: mad props to [this](https://oshlab.com/raspberry-pi-fireplace-video-looper/) article, which was a crucial source of inspiration/help for what follows.

The Raspberry Pi is an excellent low-cost, reliable video looper, particularly for situations in which the video needs to "loop forever" and do so automatically on boot. Below are instructions for running the raspberry pi over the command line (via `ssh` or `screen`), also known as running "headless."


### omxplayer (video)

OMXPlayer is the recommended [command line](https://en.wikipedia.org/wiki/Command-line_interface) video player for `raspbian`. One can download and install it via `aptitude`: `sudo apt-get install omxplayer`


### config file changes

Two quick changes to one config file: `/boot/config.txt`

1. Uncomment (delete the `#`) the line reading `#hdmi_force_hotplug=1`
2. Uncomment `hdmi_group` and `hdmi_mode` and use the following numbers to set HDMI and 1080p at 60Hz as default (if you need a different default in the future it is simply a matter of updating with different values):

    ```bash
    hdmi_group=1
    hdmi_mode=16
    ```

3. Save and exit the file.


### acquiring and playing a video

1. download and install `youtube downloader` via `apitutude`: `sudo apt-get install youtube-dl`
2. locate a short video on youtube to act as a test file. for example, one can download the "original" [Nyan Cat](https://en.wikipedia.org/wiki/Nyan_Cat) animation from youtube (as of 03/14/2017) via: `youtube-dl https://www.youtube.com/watch?v=QH2-TGUlwu4&t=4s`
3. use the Unix command `mv` to change the Nyan Cat video filename (which is obnoxious) to simply `nyan_cat.mp4`: `mv Nyan\ Cat\ \[original\]-QH2-TGUlwu4.mp4 nyan_cat.mp4`
4. play the video: `omxplayer nyan_cat.mp4`


### looping a video file

omxplayer player has built-in looping functionality: `omxplayer --loop nyan_cat.mp4`

omxplayer also has a bunch of parameters to customize the specifics of the loop playback. try running the following (replace `nyan_cat.mp4` with whatever your video is called): `omxplayer -b --loop --no-osd -o hdmi nyan_cat.mp4`

more specifically:

* `-b`: forces omxplayer to create a black background behind the video
* `--loop`: the normal command to force omxplayer to loop a video file
* `--no-osd`: hides the on-screen dialogue messages (like "Seeking..." when looping back to the beginning of the video)
* `-o hdmi`: forces audio output via the HDMI cable
* `-r`: not used in the command above but can force the video to fill the screen


### looping one video forever

With minimal alterations, and a bit of setup, one can make a `bash` file that runs the omxplayer loop command:

1. on your raspberry pi make a folder called `videolooper` in your `home` directory: `mkdir videolooper`
2. cd into `videolooper`: `cd videolooper`
3. make a `video` folder inside `videolooper` (videos will be stored here): `mkdir video`
4. on your mac make a new file called `loop_one.sh` wherever you want (we are going to set this up and then send it to the raspberry pi via `scp`): `touch loop_one.sh`
5. open up `loop_one.sh` in whatever text editor you like (remember, we are still on our mac at this point). i like [Atom](https://atom.io/) : `atom loop_one.sh`
6. Copy the following code and paste it all into your `loop_one.sh` file (then save and exit):

    ```bash
    #!/bin/sh

    omxplayer -b --loop --no-osd -o hdmi /home/pi/nyan_cat.mp4

    ```
7. use `scp` to send `loop_one.sh` to your raspberry pi (note, this requires knowledge of your pi's ip address): `scp loop_one.sh pi@<PI_IP_ADDRESS>:/home/pi/`

8. back on your pi, make `loop_one.sh` executable with `chmod`: `chmod +x loop_one.sh`
9. run `loop_one.sh` with the following command `./loop_one.sh`
10. `Control-C` (KeyboardInterrupt) to exit loop
