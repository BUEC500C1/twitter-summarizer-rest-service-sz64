# video-sz64
video-sz64 created by GitHub Classroom

## Overview
This package will allow users to input a twitter handle and be returned a video of the twitter handles tweets for the day. 


## Use
The way to interact with the package is shown in test_request.py. Which includes a way to submit a request as well as to retrieve the video. 

## Design Decisions
Currently the class can only handle 5 requests at a time. This in most cases will not bottleneck the app unless the twitter handles called have hundreds of posts in a day. This also depends on the user's computer specs as it runs multiple processes for each request. To be safe the number 5 was chosen so even the simplest of machines could run the code. 


## Future Changes
- More calls to the application class, possible for different days or have only images and so on.
- Better tests in the test function.
  - Currently the test function works within terminal but not in github. Issues with paths need to be sorted out.
- A better progress meter. 
