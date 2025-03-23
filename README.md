For those who are familiar with python: You can just download .ipynb file to convert m4a files.

For those who are not familiar with python: Download the "m4a_to_wav_converter.exe"

The code is to convert m4a files into wav files with format of:
PCM_S16LE, 48000hz sampling rate, mono

You need to install ffmpeg to get the .exe file work.
For Windows 10 or further version only. No Mac.

How to install ffmpeg
1. Run windows powershell
2. when prompt comes up, type "winget install ffmpeg". It will automatically set environment variable for most cases.

How to use .exe file
1. when executed, python prompt window and small dialogue box will appear. Click the "select m4a files to convert" in the dialogue box.
2. Explorer box will appear. Select the m4a files to convert. Files other than m4a will lead to error.
3. If it went well, wav files will be saved in the same folder with same file name but extension(.wav)


Please enjoy!
