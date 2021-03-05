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

## Abstract

With technological advancement, the adoption of advanced Internet of Things (IoT) technologies has improved impressively in the past few years. These services place such services at the extreme edge of the network. With such improvements, speciﬁc Quality of Service (QoS) trade-offs are needed to be considered. Some of such trade-offs are, particularly in situations when workloads vary over time or when IoT devices are dynamically changing their geographic position or when the data is needed to be processed in real-time and so on. Recent research has given much emphasis on realizing AI computing at the edge in contrast to cloud computing approaches to support the delay-sensitive IoT applications, autonomic decision making, and smart service creation at the edge in comparison to traditional IoT solutions. However, existing solutions have limitations concerning distributed and simultaneous resource management for AI computation and data processing at the edge; concurrent and real-time application execution; and platform-independent deployment. In our research, we focus on developing a novel platform and relevant modules with integrated AI processing and edge computer paradigms considering issues related to scalability, heterogeneity, security, and interoperability of IoT services. Further, each component is designed to handle the control signals, data flows, microservice orchestration, and resource composition to match with the IoT application requirements.

## Related works



## Methodology

#### Design the Algorithm with Neural Network

The main purpose of the AI algorithm of the project is to create a neural network from scratch in Python, which is capable of solving multi-class classification problems and can be distributed over the three-level architecture ROOF, Fog and Cloud. Some parameters of the algorithm should be transferred between each layer, then a certain model is not suitable for this case since the model can not pass through APIs from one layer to another layer. Therefore weight matrices are considered as parameters that are transferred between each layer. Softmax and cross-entropy functions are used as activation function and loss functions for creating the neural networks for multi-class classification. The cross-entropy cost function is used for optimizing the cost with softmax activation function at the output layer. There are two algorithms in our project one for predicting the vehicle’s speed and another for predicting air condition state in the vehicle. 

#### Proposed Architecture

For developing this microservice-based edge computing architecture, our proposal is to use a three-level hierarchical system, Namely as edge, fog, and cloud. On each level to some extend the processing is happening and each level has AI-based microservices for doing specific tasks. The microservices we have mainly used
are Processing Microservice, AC Model Training Microservice, Speed Model Training Microservice, Confusion Matrix Microservice, Classification Report Microservice and Accuracy Microservice. In our hierarchy, except AC Model Training Microservice and Speed Model Training Microservice, all the other microservices act as a shared resource to achieve their goals.
 
The goal of the processing microservice is to get data from the testbed (In ROOF level but for fog, data is coming from the ROOF and for cloud data is coming from fog) and do some processing such as splitting data to testing and training, and assigning separate APIs to respective result (e,g-: AC model x training data, Speed model x training data...etc). Speed model train microservice and AC model training microservice both are responsible for training the model for both the Speed and AC services. But all the Accuracy, Confusion Matrix, and Classification Report Microservices are as names suggested they provide accuracy, a classification report, and also a confusion matrix, and those results are used to check the validity of the results. One of the main features in our hierarchy is in each level if it has a higher level,( for example, the ROOF has fog and cloud, the fog has cloud but the cloud does not have any higher level) they requested the respective accuracies of the model in the higher levels. If the higher levels have higher accuracy then request their respective weight matrixes and assign them to the current level to achieve the accuracy which the higher level has got.

## Experiment Setup and Implementation

For the implementation, a testbed is implemented which acts as a microcontroller to send data via Rest APIs. As the ROOF layer, easily obtainable hardware was used. For that, a total of three Raspberry Pi 3s (RPis) is used as ROOF nodes.RPis 3 are small single-board computers (SBCs) with 1.2 GHz CPU and 1 GB RAM, 16 GB storage disk while also having integrated WiFi. Due to the hardware limitations of a single Raspberry Pi, the processing is delegated through the three ROOF nodes due to less processing power of Raspberry pi and the focus is to improve the processing power by delegating between the three of them. The three ROOF nodes interact using WIFI. As the fog layer, a laptop with Intel® Core™ i3-3227U CPU @ 1.90GHz × 4 and Ubuntu 18.04.4 LTS as the operating system. In the fog layer, it provides a special feature. As explained earlier lower hierarchies check the accuracy of its higher levels and obtain weight matrixes to obtain the so-called accuracy to the lower layers. But in the fog layer rather than comparing with its own vehicle data, it checks the accuracies of its closer vehicles model, and if another vehicle has achieved higher accuracy then that model’s weight matrixes are used as a global variable and send those weight matrixes for lower levels. 

We have used the Google Cloud Platform to provide cloud computing services at the cloud level. For that a machine type of e2-medium (2 vCPUs, 4 GB memory) with Ubuntu 18.04.5 LTS as the operating system. To communicate with these three layers, the Restful API method is used.
Further, the same special service that we used in fog also implemented in the cloud. But in the cloud rather than comparing with closer vehicles, it can compare with a whole lot of vehicles because cloud storage (Firestore) has all the data from all the vehicles.

And further, we have developed a mobile app that is interconnected with a special service provided by from cloud. The service is to give a fuel consumption assumption for the user with the speed and ac control data. The mobile app is for the user and the user can give the current location and destination with the available amount of fuel. Those data are sent to a service running in the cloud which calculates the rough assumption of fuel consumption and the result is sent back to the mobile app. Due to the less processing power of ROOF layer (Raspberry Pis)  some policies are made via ROOF and Fog layers. At the ROOF layer, the performance of CPU usage and memory usage of the Raspberry Pis are used to make the policies. One policy is made as if the ROOF node exceeds 80\% of memory and CPU usage, then the data is sent to the fog layer and the fog layer continue with the processing. From fog to cloud the data processed are sent to the cloud whenever the laptop is not using much processing power. Another policy is higher layers send the weight matrices to lower levels if the accuracy is less than it which improves the models.

## Results and Analysis

## Conclusion

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
