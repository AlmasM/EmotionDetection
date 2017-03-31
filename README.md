# Emotion Detection
Research project that focuses on recognizing emotions using face recognition and NLP. The project is developed by Emory NLP lab.

### Note
This repository contains source files from two repositories: [face-py-faster-rcnn](https://github.com/playerkk/face-py-faster-rcnn), which subsequently uses [py-faster-rcnn](https://github.com/rbgirshick/py-faster-rcnn) 

### Outline
  1. [Software requirements](#software-requirements)
  2. [Installation of Faster R-CNN](#installation-of-faster-r-cnn-based-on-face-py-faster-rcnn)
  3. [Adjusting to detect in Friends TV show](#installation-of-faster-r-cnn-friends-tv-show)

### Software requirements 
  1. Install `caffe` and `pycaffe`. Detailed installation instructions can be found at [Caffe: Installation](http://caffe.berkeleyvision.org/installation.html)
  2. Python Packages: [cython](http://cython.readthedocs.io/en/latest/src/quickstart/install.html), [opencv-mac](http://www.pyimagesearch.com/2016/11/28/macos-install-opencv-3-and-python-2-7/#comment-413944), or [opencv-ubuntu](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/), and easydict
  3. Make sure you use virtual environment. Further instructions can be found at [pyimagesearch](http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)
  
  
### Installation of Faster R-CNN (Based on `face-py-faster-rcnn`)
  1. Follow every step outlined by [face-py-faster-rcnn](https://github.com/playerkk/face-py-faster-rcnn)
  
**Note 1:** Make sure [Step 3](https://github.com/playerkk/face-py-faster-rcnn#installation-sufficient-for-the-demo) and [Step 4](https://github.com/playerkk/face-py-faster-rcnn#installation-sufficient-for-the-demo) are executed without errors, otherwise, caffe won't run.

**Note 2:** `Face-py-faster-rcnn` uses WIDER data set to train the model. The output should be .caffemodel extension

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
  

### Installig OpenFace
  1. Install, scientific computing framework, [Torch](http://torch.ch/docs/getting-started.html)
  2. Clone OpenFace, face recognition with deep neural networks, [repo](https://github.com/cmusatyalab/openface) 

