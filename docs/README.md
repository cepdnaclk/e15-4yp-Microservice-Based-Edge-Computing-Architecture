---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e15-4yp-Microservice-Based-Edge-Computing-Architecture
title: Microservice Based Edge Computing Architecture
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# Project Title

#### Team

- E/15/048, Gayal Laksara, [email](mailto:Laksaragayal1996@email.com)
- E/15/243, Sewwandi Nisansala, [email](mailto:sewwanis@gmail.com)
- E/15/271, Sonali Prasadika, [email](mailto:sonaliprasadika077@gmail.com)

#### Supervisors

- Dr.Upul Jayasinghe, [email](mailto:upuljm@eng.pdn.ac.lk)
- Dr. Isuru Nawinne, [email](mailto:isurunawinne@eng.pdn.ac.lk)


#### Table of content

1. [Abstract](#abstract)
3. [Related works](#related-works)
4. [Methodology](#methodology)
5. [Experiment Setup and Implementation](#experiment-setup-and-implementation)
6. [Results and Analysis](#results-and-analysis)
7. [Conclusion](#conclusion)
8. [Publications](#publications)
9. [Links](#links)

---

# Abstract

With technological advancement, the adoption of advanced Internet of Things (IoT) technologies has improved impressively in the past few years. These services place such services at the extreme edge of the network. With such improvements, speciﬁc Quality of Service (QoS) trade-offs are needed to be considered. Some of such trade-offs are, particularly in situations when workloads vary over time or when IoT devices are dynamically changing their geographic position or when the data is needed to be processed in real-time and so on. Recent research has given much emphasis on realizing AI computing at the edge in contrast to cloud computing approaches to support the delay-sensitive IoT applications, autonomic decision making, and smart service creation at the edge in comparison to traditional IoT solutions. However, existing solutions have limitations concerning distributed and simultaneous resource management for AI computation and data processing at the edge; concurrent and real-time application execution; and platform-independent deployment. In our research, we focus on developing a novel platform and relevant modules with integrated AI processing and edge computer paradigms considering issues related to scalability, heterogeneity, security, and interoperability of IoT services. Further, each component is designed to handle the control signals, data flows, microservice orchestration, and resource composition to match with the IoT application requirements.

# Related works

### Distributed Computing

Distributed Edge and Fog address some challenging scenarios of traditional cloud computing architecture. Chao Gong et al. presented ICE computing architecture that combines AI techniques and edge computing. They have achieved lower latency and a higher caching hate ratio at the edge to achieve a smart IoT [10]. Muhammad Alam et al. proposed distributed architecture with cloud, fog and edge devices, which makes sure that the data gets collected and analyzed at the most
efficient and logical layer [11]. Edge Computing is inbuilt with predictive algorithms that may make decisions autonomously without looking forward to the cloud [7]. Fog Computing extends device-centric approaches to IoT development by introducing support for edge processing, network processing, and integration with Cloud Computing. Consistent with the research paper [12], fog devices will be
classified as edge, IO (Input/Output), and compute nodes. In [13], the authors have presented the results of the efficient utilization of resources in the network infrastructure by using
fog, cloud architecture. Here Fog computing results in solving the problem of latency in time-critical IoT applications.

### Microservices Architecture

Microservices is an architectural style that structures an application as a collection of services that are highly maintainable and testable, loosely coupled, and independently deployable. These services are purposely built to perform a cohesive business function and are an evolution of the standard service-oriented architecture style [7], [14], [15]. In a microservice architecture, interdependent software components are individually configured as a microservice, where each
service is liable for its small purpose. During a monolithic architecture, all functional logics for handling demands operate within the same process [16]–[18] [19]. There are some advantages in microservice architecture which are independent deployment, and fault isolation, meaning we are able to fix the fault only within the corresponding microservice otherwise the complete monolith to be re-developed, mixed technology stack which means we will use different technologies in several
microservices.

# Methodology

### Design the Algorithm with Neural Network

The main purpose of the AI algorithm of the project is to create a neural network from scratch in Python, which is capable of solving multi-class classification problems and can be distributed over the three-level architecture ROOF, Fog and Cloud. Some parameters of the algorithm should be transferred between each layer, then a certain model is not suitable for this case since the model can not pass through APIs from one layer to another layer. Therefore weight matrices are considered as parameters that are transferred between each layer. Softmax and cross-entropy functions are used as activation function and loss functions for creating the neural networks for multi-class classification. The cross-entropy cost function is used for optimizing the cost with softmax activation function at the output layer. There are two algorithms in our project one for predicting the vehicle’s speed and another for predicting air condition state in the vehicle. 

### Proposed Platform

To facilitate real-time processing and distributed communication at the edge, we propose a three-layer architecture, namely ROOF, fog, and cloud. Edge consists of fog devices and ROOF devices to process data in real-time but with less computation power and memory size. Fog acts as an intermediate level between ROOF and Cloud. Fog consists of more computation power and memory power than ROOF but not as much as Cloud. And finally, we have Cloud level to do higher computations to achieve the desired goals. This proposed architecture is network independent since this is three-layered architecture. The ROOF is the closest layer to the IoT devices and it does the AI computing on the sensor data from IoT devices. Here the horizontal distribution is also used to delegate the computational power on several nodes at the same time on ROOF and Fog layers. Therefore we have reduced memory and computational issues at the ROOF and Fog layers. Apart from this, there are policies that implemented to get high accuracy on the AI model which are discussed in section III.
Even though this hierarchical architecture provides a solution for the real-time data processing issue, we needed a system that can have components that we can reuse. With that intend we move to the microservice-based architecture rather than going with a monolithic architecture.

# Experiment Setup and Implementation

From the theoretical view, the proposed hierarchy and reason for going such a hierarchy is explained in Section III. The system is designed for the use case, an autonomous car. To validate and run the system we took a testbed approach. 

### Implementation of the Prototype 

Since the system is designed only on a software basis we need a method to generate data in a way that happens in a real vehicle. In real vehicles, we have a microcontroller to collect data from different sensors such as Lidars, GPS, speedometers, etc. The microcontroller sent these data to the desired processing units to process and get the desired output. This is where the testbed is coming from. In our system, the testbed acts as our microcontroller and it sends data in a manner which the microcontroller sent. The dataset is found from Kaggle, provided freely by Victor R. F. (Car trips data log). As the ROOF layer, easily obtainable hardware which is a total of three Raspberry Pi 3s (RPis) is used as ROOF nodes. RPis 3 are single-board computers (SBCs) with 1.2 GHz CPU and 1 GB RAM, 16 GB storage disk while also having integrated WiFi. Due to the hardware limitations of a single Raspberry Pi, the processing is delegated through the three ROOF nodes. Due to the less processing power of Raspberry pi and the focus is to improve the processing power by delegating between the three of them. The three ROOF nodes interact using WIFI. Two laptops were used as the Fog layer. One with Intel® Core™ i3-3227U CPU @ 1.90GHz × 4 and Ubuntu 18.04.4 LTS as the operating system and the other laptop with Intel(R) Core(TM) i7-4600 CPU @ 2.10 GHz and Windows 7 operating system.
We have used the Google Cloud Platform to provide cloud computing services at the cloud level. For that a machine type of e2-medium (2 vCPUs, 4 GB memory) with Ubuntu 18.04.5 LTS as the operating system. To communicate with these three layers, the Restful API method is used.

### Dynamic offloading

Dynamic offloading improves the performance of ROOF architecture since it has lower computational power. In [20], the authors proposed task-centric and data-centric algorithms to analyze the threshold when the dynamic offload is happening. In our case, since the data is sent to the upper levels (FOG and Cloud), the data are not stored at the ROOF. Therefore the data-centric method is not suitable for this case. Here the task-centric algorithm is considered to do the offloading. Since the Raspberry Pis have less computation the overload can happen and it gets too much time to process data
even the processing is delegated horizontally on several nodes. The tasks which get larger processing times in the nodes are offloaded to the least overloading nodes. The utility function for calculating offloading algorithm is as follows.

| Meaning                        | Symbol              |
| -------------------------------|:-------------------:|
| Max device factor              | α<sub>a</sub>       | 
| Min device factor              | α<sub>b</sub>       |
| Number of connected edge nodes | E<sub>n</sub>       |
| Threshold                      | T                   |
| Time per offload service       | β<sub>i</sub>       |
| Total time                     | β<sub>t</sub>       |


   α<sub>a</sub> = 1/(E<sub>n</sub>)<br/>
   α<sub>a</sub> = 1/(E<sub>n</sub> + 1)<br/>
   T = (β<sub>i</sub> / β<sub>t</sub>) <br>
  
  Offload occurs when, <br>
    T > α<sub>a</sub> 
 
 
 ### Microservices Implementation
 
 For developing this microservice-based edge computing architecture, we propose to use a three-level hierarchical system, Namely as ROOF, fog, and cloud. On each level to some extend the processing is happening and each level has AIbased microservices for doing specific tasks. Microservices we mainly used processing microservice, AC model training microservice, speed model training microservice, confusion matrix microservice, classification report microservice and accuracy microservice
In our hierarchy, except AC Model Training Microservice and Speed Model Training Microservice, all the other microservices act as a shared resource to achieve their goals. The goal of the processing microservice is to get data from the testbed (for ROOF) and for other levels, lower-level processing
microservice sent data to upper-level processing microservice. Further, the functionalities in the processing are splitting data to testing and training, and assigning separate APIs to respective results (e,g-: AC model x training data, Speed model x training data, etc). Speed model train microservice and AC model training microservice both are responsible for training the model for both the Speed and AC services. But all the accuracy, confusion matrix, and classification report microservices are responsible for providing accuracy, a classification report, and also a confusion matrix, and those results are used to validate the results. Here we have implemented a policy in a model train, which is it requests the accuracies from all the upper layers and if an upper layer has greater accuracy compared to its current accuracy, then the weight matrices of that corresponding upper layer are requested and replaced in the model. As a result of this, since the lower level has less computation and storage powers compared to its upper layer, there is a possibility that
the upper layer may have achieved greater accuracy. So we can achieve the same accuracy level for lower layers by sharing the model in this way. The ROOF model can be seen in figure 1
The whole hierarchy can be seen in Figure 2. All the functionalities happening in ROOF happens in fog and cloud. Additionally, we have a separate microservice called Global Accuracy at both fog and cloud levels. Global accuracy microservice is the one that responds for keeping the track of accuracy and weight matrices of near vehicles. It requests the accuracy from all the nearby vehicles and if a vehicle has higher accuracy, we update the global accuracy microservice with that vehicle’s accuracy and weight matrix data. A policy in this microservice is, at the start, we have seen with the
lesser number of datasets we get about 100% accuracy. But this accuracy is not valid because it can not predict the correct outputs with the changing natures. The policy is, to update the global accuracy, the corresponding vehicle must have generated more than the size of 1000 data sets.
As seen in figure 3, cloud level has some additional functionalities compared to its lower levels. Since the cloud is the topmost layer, all the input data coming from the testbed is saved in the cloud firestore for archiving reasons. The further initial plan is to use the cloud database service to act as a global accuracy saver, but since firestore does not allow us to save 2-D matrices we fall back to the strategy we used in the fog here. Further, we have developed a mobile app that is interconnected with a special service provided with the use of cloud functionalities. The service is to give a fuel consumption assumption for the user by combining speed and ac control data. The mobile app is for the user and the user can give the current location and destination with the available amount of fuel. Those data sent to a service running in the cloud which calculates the rough assumption of fuel consumption with the speed and ac data at cloud level, and the result is sent back
to the mobile app

### lementation of the NN Algorithm

As mentioned above, in the methodology section, the algorithms are divided into two sub-phases as the feed-forward phase and the backpropagation phase.
 

# Results and Analysis

# Conclusion

With the staunch objective of providing real-time processing at the edge, we have developed a microservice-based AI computational hierarchy. The processing happens in both vertical hierarchical manner(ROOF, Fog, Cloud) and also horizontal hierarchical manner(In the ROOF level). Each level has its own policies (Accuracy checking from upper levels...etc) to control the flow of data and how the process should be distributed.  

## Publications
1. [Semester 7 report](./)
2. [Semester 7 slides](./)
3. [Semester 8 report](./)
4. [Semester 8 slides](./)
5. Author 1, Author 2 and Author 3 "Research paper title" (2021). [PDF](./).


## Links

[//]: # ( NOTE: EDIT THIS LINKS WITH YOUR REPO DETAILS )

- [Project Repository](https://github.com/cepdnaclk/repository-name)
- [Project Page](https://cepdnaclk.github.io/repository-name)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)

[//]: # "Please refer this to learn more about Markdown syntax"
[//]: # "https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet"
