# Facerecognition Test Tool
With this tool you can test if your facerecognition model is working.
The facerecognition in this tool is based on code from [pi-facerec-box](https://github.com/tdicola/pi-facerec-box). The tool is only tested on a desktop computer, not on a Pi.

## Usage
1. Make sure you have all dependencies (see bellow) installed.
2. Copy your `training.xml` from `tools/facetrainer` into the root folder of this tool.
3. In `tools/facerecognition_tester/lib/config.py` add add your training labels from `tools/facetrainer` under `personen = []` and specify the used algorithm.
4. Enter the `tools/facerecognition_tester` directory from a terminal and run `python facerecognition.py`.

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