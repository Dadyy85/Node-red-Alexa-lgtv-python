# Node-red-script-lgtv-python
Sequence of instructions node-red and python script, for play youtube from Alexa to LG tv.
<br>

Tools needed:<br>
Node-red  https://github.com/node-red/node-red <br>
  necessary pallets:<br>
    *node-red-contrib-alexa-remote2-applestrudel  https://github.com/bbindreiter/node-red-contrib-alexa-remote2-applestrudel <br>
    *node-red-contrib-lgtv  https://github.com/hobbyquaker/node-red-contrib-lgtv <br>
*mqtt broker <br>
*platform (example raspberry pi) to host Python scripts
<br> <br> <br>
<p>Principle of operation:</p>
<p>* Starting with an alexa voice command containing the word "youtube and the name of the video".</p>
<p>* Node red reads the command Alexa and sends an mqtt message, containing the name of the video.</p>
<p>* The python script reads the mqtt message, and performs a search on youtube.</p>
<p>* Found the video, it transmits the address (via mqtt) useful to the lgtv node.</p>
