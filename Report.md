# ECE539 Project Report

__PROJECT TITLE__: Singing livestream segmentation assistant

__TEAM MEMBERS__: 
- Avi BALAM, 9086006591, [abalam@wisc.edu](abalam@wisc.edu), Undergraduate
- YUSHANG JIN, 9083280140, [yjin248@wisc.edu](yjin248@wisc.edu)
- ZALISSA ZONGO KAFANDO, 9084045047, [zongokafando@wisc.edu](zongokafando@wisc.edu)
  
__Date of submission__: 11/18/2023

__ABSTRACT__:
A comprehensive approach to audio classification was developed and implemented. The project involved the loading and preprocessing of audio data, transforming the waveform into a spectrogram using short-time Fourier transform (STFT). A pre-trained convolutional neural network (CNN) model was then employed to predict class probabilities for each chunk of the audio stream, distinguishing between singing and speech. The predictions were further refined using a multilayer perceptron (MLP) model to reduce noise. The accuracy of the predictions was evaluated by comparing them with actual labels, demonstrating the effectiveness of the approach.

__Introduction__:
Our target is to assist in slicing singing livestream videos, that is help cutting the singing parts out from the whole livestream recording, by highlighting the potential singing partitions. The core is audio classification that distinguishes between singing and speech. "Classifying Music and Speech with Machine Learning" by Code AI demonstrated an approach to classifying audio into music or speech categories. They transfer audio into spectrogram using FFT and use a CNN model for classification. With gtzan dataset (see below) the validating accuracy reaches 100%.

### Method
We have reproduced the previous work mentioned above and applied it to our use case. The procedures, outcomes, and analysis are below.

#### Reproduce previous work
[Our Jupyter Notebook](https://github.com/EricEricEricJin/ECE539-Group-Project/blob/master/music_speech_clf.ipynb)

- Data preprocessing: 

    We want the frequency domain features, so preprocessing requires transfer each 30-second audio into spectrogram (using FFT, chunk size and step size are hyper parameters to be tuned) and normalize the amplitude.

- Model:

    With above preprocessing, each input is a spectrogram matrix whose ith row is the ith chunk's frequency spectrum. Output is by one-hot coding, (e.g., music is [0 1] and speech is [1 0]). Then use CNN to connect input and output, and fit, evaluate the model.

- Result: 

    Below is the validating accuracy against epoch number of the model with `xxm_splitted` dataset. We can see Code AI didn't lie and the accuracy of its model is very high. 

    ![post outcome](Figure/post_outcome.png)

#### Apply previous work to our use case

Below is the block diagram of our current implementation:

```
    [Long audio]-->[CHUNK 1][CHUNK 2] ... [CHUNK N]
                        |
                        V
                    (FFT)-->[Spectrum]-->(CNN)-->[Probability of each chunk]
                                                            |
                                                            V
[Predict outcome]<--(Thredhold)<--[Filtered probability]<--(FIR)                                           
    * The [CNN] network is trained with xxm_splitted dataset as mentioned above. 
```

Below is the outcome, blue line is the prediction (1 for singing, 0 for speech) and red dot is actual label showing starting of singing. 

![outcome](Figure/10-20_outcome.png)

We (human) listened to the false positive points and find at those points there is background music making the model predict them as singing. To fix this issue, speaker recognition may be applied to recognize the specific person's voice print.

Also, the FIR filter I applied is used to detect rising edges, it will filter out long continuous positive points. This is consistent with our goal since we assume each song is in certain length and there is no continuous singings.

### Progress So Far
The project initiation commenced with the formulation of a detailed project proposal on 10/20/2023, delineating the project's objectives, methodologies, and anticipated outcomes. The subsequent phase involved the establishment of a collaborative development environment utilizing Google Colab and GitHub, wherein all pertinent project-related documents were meticulously organized within the GitHub repository.

To ascertain the viability of the project, the team diligently examined the previous works model, critically analyzing its components and evaluating the applicability of Tensorflow, a fundamental framework for machine learning. Subsequently, an exhaustive review of extant models within the realm of online videos on the chosen platform was conducted, with a specific emphasis on identifying potential optimizations for the audio classification model.

The pivotal step of data collection and preprocessing ensued, wherein data from designated sources was systematically acquired and refined to ensure cleanliness, appropriate formatting, and readiness for integration into the classification model. Concurrently, the team embarked on the construction of a Convolutional Neural Network (CNN) model, delving into the intricacies of CNNs and leveraging TensorFlow for model development. This phase marked a crucial juncture in the project, laying the foundation for the subsequent stages of model refinement and evaluation.


