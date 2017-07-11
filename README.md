# Emotion Detection
Research project that focuses on recognizing emotions using face recognition and NLP. The project is developed by Emory NLP lab.

### Note
This repository contains source files from two repositories: [face-py-faster-rcnn](https://github.com/playerkk/face-py-faster-rcnn), which subsequently uses [py-faster-rcnn](https://github.com/rbgirshick/py-faster-rcnn) 

### Outline
  1. [Software requirements](#software-requirements)
  2. [Installation of Faster R-CNN](#installation-of-faster-r-cnn-based-on-face-py-faster-rcnn)
  3. [Adjusting to detect in Friends TV show](#installation-of-faster-r-cnn-friends-tv-show)
  4. [Face_recognition package installation](#installing-face-recognition-package-using-dlib)
  5. [Run Face_recognition package](#run-face-recognition-package)

### Software requirements 
  1. Install `caffe` and `pycaffe`. Detailed installation instructions can be found at [Caffe: Installation](http://caffe.berkeleyvision.org/installation.html)
  2. Python Packages: [cython](http://cython.readthedocs.io/en/latest/src/quickstart/install.html), [opencv-mac](http://www.pyimagesearch.com/2016/11/28/macos-install-opencv-3-and-python-2-7/#comment-413944), or [opencv-ubuntu](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/), and easydict
  3. Make sure you use virtual environment. Further instructions can be found at [pyimagesearch](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)
  
  
### Installation of Faster R-CNN (Based on `face-py-faster-rcnn`)
  1. Follow every step outlined by [face-py-faster-rcnn](https://github.com/playerkk/face-py-faster-rcnn)
  
**Note 1:** Make sure [Step 3](https://github.com/playerkk/face-py-faster-rcnn#installation-sufficient-for-the-demo) and [Step 4](https://github.com/playerkk/face-py-faster-rcnn#installation-sufficient-for-the-demo) are executed without errors, otherwise, caffe won't run.

**Note 2:** `Face-py-faster-rcnn` uses WIDER data set to train the model. The output should be .caffemodel extension

**Note 3:** Make sure to download the package Faster RCNN package 'recursively'. 

  2. To test the model, the tutorial uses [FDDB](http://vis-www.cs.umass.edu/fddb/index.html#download) provided by UMass. So, if you are using pre-trained model, there is no need to download WIDER data set (make sure you adjust code accordingly).
  3. If all the steps are executed without errors, you can run the code on dataset:
  ```Shell
    ~$ cd rcnn/face-py-faster-rcnn-master/ 
    python ./tools/run_face_detection_on_fddb.py --gpu=0
  ```
  
  
### Installation of Faster R-CNN (Friends TV show)

  1. Update directory names in the file: run_face_detection_on_fddb.py:
  
    1.1 location of .caffemodel
    1.2 data_dir, out_dir
    1.3 plt.savefig() in the vis_detections() method
  2. Run the code as in Step 3 of Installation of `face-py-faster-rcnn`  
  

### Installing Face Recognition package using dlib 
  1. Install dlib using either Method 1 or Method 2.

**Method 1**
  
  Use procedure outlined by [PyImageSearch](http://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/)

**Method 2**

  Make sure you install python, [opencv](http://www.pyimagesearch.com/2016/11/28/macos-install-opencv-3-and-python-2-7/), boost, boost-python, dlib using ```brew install package_name```.
  
  Download [dlib](http://dlib.net/files/dlib-19.4.tar.bz2) from website
  
  Activate virtual environment, and in dlib directory, run ```python setup.py install``` 
  
  More information can be found in this [github](https://github.com/cmusatyalab/openface/issues/187)
  
  2. Install face_recognition package
  
  Make sure dlib is installed without errors, otherwise face_recognition will not run properly. Then, in your bash run
  
  ```bash
  pip install face_recognition
  ```
  
  3. More information about face recognition can be found [here](http://blog.dlib.net/2017/02/high-quality-face-recognition-with-deep.html)
  
  4. Convenient explanation and sample explanations are given by [Adam Geitgey](https://github.com/ageitgey/face_recognition)


 ### Run Face Recognition Package ###
  
  1. Copy get_dir.py file
  2. Inside the get_dir.py file provide 3 paths. 
  
    2.1 rootDir - known faces (i.e. faces of characters: Rachel, Ross,  Monica, etc)
    2.2 unknownDir - location of pictures where you need to recognize faces 
    2.3 newDir - location where to store new, evaluated pictures
  
  
     
