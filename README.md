# Singing livestream segmentation assistant
ECE539 Course Project

Contributors: [YUSHANG JIN](https://github.com/EricEricEricJin), [Avi BALAM](https://github.com/AviRaj1109), [ZALISSA](https://github.com/Zaliss)

<!-- [Project proposal](proposal/proposal.md), [Progress report](progress_report/progress_report.md),  -->
[Final report](project_report/ece539_report.pdf)

__Keywords__: Audio classification, CNN, Time series, LSTM


__Abstract__: In this project we developed a program to assist cutting the singing parts out from singing
livestream recordings. We used data from Bilibili, trained a CNN model that classifies each chunk of audio
into speech or singing, and a LSTM model that detects the start of singing from the CNN model output.
Then we developed our application method, that get the predicted timestamps of start of singing from the
LSTM output, and developed a convincing evaluation method that gives performance metrics by comparing
the output and true label.