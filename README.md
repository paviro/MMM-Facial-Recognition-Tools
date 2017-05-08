# Facetrainer Tool
This repository contains tools to setup and train the [facial recognition module](https://github.com/paviro/MMM-Facial-Recognition) for the [MagicMirror](https://github.com/MichMich/MagicMirror).

# Facetrainer Tool

The scripts in this directory are based on scripts from [pi-facerec-box](https://github.com/tdicola/pi-facerec-box) and should be used on a computer (with a webcam). You need OpenCV installed on your computer. It works on a RaspberryPi.

## Usage
### Capturing training images
1. Make sure you have all dependencies (see below) installed.
2. Run `python capture.py`.
3. Decide whether you want to capture images from your web cam or convert existing `.jpg` images.
4. Enter the name of the person you are about to capture. Images will be stored in a folder named after the captured person in `training_data/`.
5. Follow screen instructions.

### Training model
1. Make sure you have all dependencies (see below) installed.
2. Make sure you have captured all your images.
3. Run `python train.py`. The script will automatically scan the directory `training_data/` for your images.
4. Wait. You will end up with a `training.xml` file in the current directory.
5. Copy down the `['name', 'name2','name3']` part because you will later need it for setting up your mirror's face recognition and to test your face recognition model.

# Facerecognition Test Tool
With this tool you can test if your facerecognition model is working.

## Usage
1. Make sure you have all dependencies (see below) installed.
2. Make sure your `training.xml` from running `train.py` is in this directory
3. specify the face recognition algorithm in the environment with
```
export FACE_ALGORITHM=1
```
4. specify your user labels in the environment with

```
export FACE_USERS=Alice,Bob,Casey,Doug
```
5. Run `python facerecognition.py`.

## Dependencies

### OpenCV

To install [OpenCV](http://opencv.org) run:

```
sudo apt-get install libopencv-dev python-opencv
```

If you are using virtual environments you will need to need to copy
the opencv python modules into your virutal environment path. That
will look something like this:

```
cp /usr/lib/python2.7/dist-packages/cv* ~/.virtualenvs/MY_VIRTUAL_ENV/lib/python2.7/site-packages/
```

Where ``python2.7`` will be the name of your python version where
opencv was installed and ``MY_VIRTUAL_ENV`` is the name of your
virtual environment.

### Python dependancies

Install the required python packages. 

```
pip install -r requirements.txt
```

Currently this is just the ``future`` module for making the scripts python 2 and 3 cross compatible.


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
