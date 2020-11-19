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
 && rm -rf Python-3.7.0.tgz

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
 && rm -rf /var/lib/apt/lists/*


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




LABEL maintainer="sean@seancook.dev"
LABEL description="CPU-only version of OpenPose. Not slimmed for production."
LABEL version="1.0"

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /root/



RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install wget apt-utils lsb-core cmake git -y && \
    apt-get install libopencv-dev -y

RUN git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git

WORKDIR /root/openpose/

RUN git checkout caa794cf81bed53b9e114299b715a6d972097b5b

WORKDIR /root/openpose/scripts/ubuntu

RUN sed -i 's/\<sudo -H\>//g' install_deps.sh; \
   sed -i 's/\<sudo\>//g' install_deps.sh; \
   sed -i 's/\<easy_install pip\>//g' install_deps.sh; \
   sync; sleep 1; bash install_deps.sh

WORKDIR /root/openpose/

RUN mkdir build

WORKDIR /root/openpose/build


RUN cmake -DGPU_MODE:String=CPU_ONLY \
          -DDOWNLOAD_BODY_MPI_MODEL:Bool=ON \
          -DDOWNLOAD_BODY_COCO_MODEL:Bool=ON \
          -DDOWNLOAD_FACE_MODEL:Bool=ON \
          -DDOWNLOAD_HAND_MODEL:Bool=ON \
          -DUSE_MKL:Bool=OFF \
          ..

RUN make

RUN apt-get remove wget unzip cmake git build-essential -y && apt-get autoremove -y

WORKDIR /root/openpose

#ENTRYPOINT ["build/examples/openpose/openpose.bin"]

#CMD ["--help"]
