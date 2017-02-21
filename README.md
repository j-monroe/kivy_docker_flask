# kivy_docker_flask
Dockerized flask service + kivy front end 

I built this super simple web app When you kick it and and give it a location of /clothin?place=work It will tell you what you should be wearing.

Then I made a kivy front end It's kind of ugly but it works none the less. The point is that the Kivy front end will consume A version of the web service and then print out the result from the server.

I also turned the web service into a dockerized centos version so it will build a centos container and start.

This version will just use python to start a single threaded listener I still need to do some more research on what it looks like to do apache in docker on centos 
