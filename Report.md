# ECE539 Project Report

__PROJECT TITLE__: Singing livestream segmentation assistant

__TEAM MEMBERS__: 
- Avi BALAM, 9086006591, [abalam@wisc.edu](abalam@wisc.edu), Undergraduate
- YUSHANG JIN, 9083280140, [yjin248@wisc.edu](yjin248@wisc.edu)
- ZALISSA ZONGO KAFANDO, 9084045047, [zongokafando@wisc.edu](zongokafando@wisc.edu)
  
__Date of submission__: 11/18/2023

__ABSTRACT__
A comprehensive approach to audio classification was developed and implemented. The project involved the loading and preprocessing of audio data, transforming the waveform into a spectrogram using short-time Fourier transform (STFT). A pre-trained convolutional neural network (CNN) model was then employed to predict class probabilities for each chunk of the audio stream, distinguishing between singing and speech. The predictions were further refined using a multilayer perceptron (MLP) model to reduce noise. The accuracy of the predictions was evaluated by comparing them with actual labels, demonstrating the effectiveness of the approach.

__Introduction__
Our target is to assist in slicing singing livestream videos, that is help cutting the singing parts out from the whole livestream recording, by highlighting the potential singing partitions. The core is audio classification that distinguishes between singing and speech. "Classifying Music and Speech with Machine Learning" by Code AI demonstrated an approach to classifying audio into music or speech categories. They transfer audio into spectrogram using FFT and use a CNN model for classification. With gtzan dataset (see below) the validating accuracy reaches 100%.

