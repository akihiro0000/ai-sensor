FROM ubuntu:18.04
MAINTAINER mganeko

ENV PYTHON_VERSION=3.7.0
ENV DEBIAN_FRONTEND nonineractive

WORKDIR /root/
RUN apt update && apt upgrade -y \
    python3 \
    python3-pip \
    python3-dev \
    python3 -V \
    git \
    wget \
    vim \
    libopencv-highgui-dev \
    v4l-utils \
 && apt clean \
 && apt install -y  --no-install-recommends make cmake gcc g++ unzip wget build-essential zlib1g-dev libffi-dev libssl-dev \
 && rm -rf /var/lib/apt/list/* \
 && mkdir /root/work \
 && wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
 && tar zxf Python-${PYTHON_VERSION}.tgz \
 && rm -rf Python-3.7.0.tgz \

WORKDIR /root/work/                                                                                                         
RUN git clone https://github.com/AlexeyAB/darknet.git                                                                       
                                                                                                                            
WORKDIR /root/Python-${PYTHON_VERSION}/                                                                                     
RUN ./configure                                                                                                             
RUN make altinstall \                                                                                                       
 && ln -s /usr/local/bin/python3.7 /bin/python3 \                                                                           
 && ln -s /usr/local/bin/pip3.7 /bin/pip3 \                                                                                 
 && pip3 install --upgrade pip \                                                                                            
 && pip -V \                                                                                                                
 && pip install flask \                                                                                                     
 && pip3 install numpy pillow \                                                                                             
 && apt update \                                                                                                            
 && apt install --no-install-recommends -y build-essential cmake nano \                                                     
    ca-certificates unzip wget \                                                                                            
    pkg-config \                                                                                                            
    libgtk2.0-dev \                                                                                                         
    libjpeg-dev libpng-dev \                                                               
    ffmpeg libavcodec-dev libavformat-dev libavresample-dev libswscale-dev \               
    libv4l-dev \                                                                           
    libtbb-dev \                                                            
 && apt-get clean \                                                         
 && rm -rf /var/lib/apt/lists/* \                                           
                                                                            
WORKDIR /root/                                                              
RUN mkdir /tmp/opencv                                                       
                                                                            
WORKDIR /root/tmp/opencv                                                    
ENV OPENCV_VERSION="3.4.0"                                                  
RUN wget https://github.com/opencv/opencv/archive/${OPENCV_VERSION}.zip \   
 && unzip ${OPENCV_VERSION}.zip -d .                                        
                                                                            
WORKDIR /root/tmp/opencv/opencv-${OPENCV_VERSION}/                          
RUN mkdir build

WORKDIR /root/tmp/opencv/opencv-${OPENCV_VERSION}/build/                                                                    
RUN cmake -D BUILD_TESTS=OFF -D BUILD_PERF_TESTS=OFF -D WITH_FFMPEG=ON -D WITH_TBB=ON  .. | tee /tmp/opencv_cmake.log \     
 && make -j "$(nproc)" | tee /tmp/opencv_build.log \                                                                        
 && make install | tee /tmp/opencv_install.log                                                                              
                                                                                                                            
                                                                                                                            
                                                                                                                            
WORKDIR /root/work/darknet/                                                                                                 
RUN wget https://pjreddie.com/media/files/yolov3-tiny.weights \                                                             
 && git clone https://github.com/AlexeyAB/darknet.git \                                                                     
 && git clone https://github.com/akihiro0000/AIapp.git \                                                                    
 && pip3 install paho-mqtt \                                                                                                
 && mv ./AIapp/app.py ./ \                                                                                                  
 && pip3 install datetime \                                                                                                 
 && mv ./AIapp/camera.py ./ \                                                                                               
 && mv ./AIapp/templates ./ \                                                                                               
 && mv ./AIapp/darknet.py ./                                                                                                
                                                                                                                            
WORKDIR /root/work/darknet/darknet/                                                                                    
RUN sed -i -e "/OPENCV=/s/0/1/" Makefile \                                                                             
 && sed -i -e "/LIBSO=/s/0/1/" Makefile \                                                                              
 && make \                                                                                                             
 && mv ./libdarknet.so ../ \                                                                                           
 && mv ./cfg ../ \                                                                                                     
 && mv ./data ../  

WORKDIR /root/work/darknet/                                                                                                 
RUN rm -rf README.md \                                                                                                      
           Makefile \                                                                                                       
           image_yolov4.sh \                                                                                                
           net_cam_v4.sh \                                                                                                  
           video_yolov4.sh \                                                                                           
           build \                                                                                                     
           AIapp \                                                                                                     
           results \                                                                                                   
           image_yolov3.sh \                                                                                           
           video_yolov3.sh \                                                                                           
           net_cam_v3.sh \                                                                                             
           build.sh \                                                                                                  
           json_mjpeg_streams.sh \                                                                                     
           cmake \                                                                                                     
           CMakeLists.txt \                                                                                            
           3rdparty \                                                                                                  
           darknet_images.py \                                                                                         
           DarknetConfig.cmake.in \                                                                                    
           LICENSE \                                                                                                   
           include \                                                                                                   
           scripts \                                                                                                   
           src \                                                                                                       
           __pycache__  

