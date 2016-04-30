# Facetrainer Tool
The scripts in this directory are based on scripts from [pi-facerec-box](https://github.com/tdicola/pi-facerec-box) and should be used on a computer (with a webcam). You need OpenCV installed on your computer. It may work on a Pi but is probably pretty slow.

## Usage
### Capturing training images
1. Make sure you have all dependencies (see bellow) installed.
2. Enter the `tools/facetrainer` directory from a terminal and run `python capture.py`.
3. Decide whether you want to capture images from your web cam or convert existing `.jpg` images.
4. Enter the name of the person you are about to capture. Images will be stored in a folder named after the captured person in `tools/facetrainer/training_data/`.
5. Follow screen instructions.

### Training model
1. Make sure you have all dependencies (see bellow) installed.
2. Make sure you have captured all your images.
3. Enter the `tools/facetrainer` directory from a terminal and run `python train.py`. The script will automatically scan `tools/facetrainer/training_data` for your images.
4. Wait. You will end up with a `training.xml` file in `tools/facetrainer`.
5. Write down the `['name', 'name2','name3']` part because you will later need it for setting up your mirror's face recognition.

## Dependencies
- [OpenCV](http://opencv.org) (sudo apt-get install libopencv-dev python-opencv)

## Open Source Licenses
###[pi-facerec-box](https://github.com/tdicola/pi-facerec-box)
The MIT License (MIT)

Copyright (c) 2014 Tony DiCola

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The negative training data is from the ORL face database.  Please see the file
tools/facetrainer/training_data/negative/README for more information on this data.
