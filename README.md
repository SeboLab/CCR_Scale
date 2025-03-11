# CCR Scale Study 1-3 Data Analysis

## Study 1

* nFactors.R
  * Purpose: Determines the number of factors.
  * Input Data: `Study1Data.csv`, containing ratings from 288 participants on 27 scale items, each responding to one of four videos (Exercise, Service, Companion, Argument). The videos can be accessed [here](https://osf.io/5ezga/?view_only=f857949cfe1e49dd8f75ce1aac206b9f).
  * Result Interpretation: Very Simple Structure (VSS), particularly VSS complexity 2 = 0.99, and empirical BIC suggested two factors. 
* parallelAnalysis.R
  * Purpose: Determines the number of factors.
  * Input data: `Study1Data.csv`.
  * Result Interpretation: Kaiser's Rule, applied to the unadjusted eigenvalues (retaining factors with eigenvalues > 1), suggested two factors.
* factorAnalysis.R
  * Purpose: Performs exploratory factor analysis with two factors using Promax rotation to examine factor loadings.
  * Input data: `Study1Data.csv`.
  * Result Interpretation: Retaining scale items with at least one loading >= 0.6 and no cross-loadings >= 0.3 resulted in 19 items across both factors. The factors were named Connection and Coordination based on the contextual meanings of the scale items.
* cronbachAlpha.R
  * Purpose: Assesses the internal reliability of the remaining 19 scale items using Cronbach's alpha.
  * Input data: `Study1Data.csv`.
  * Result Interpretation: Cronbach's alpha = 0.96, indicating very high internal reliability.
* omega.R
  * Purpose: Evaluates the internal reliability of the remaining 19 scale items using McDonald's omega.
  * Input data: `Study1Data.csv`.
  * Result Interpretation: McDonald's omega = 0.97, indicating very high internal reliability.

## Study 2

* CFA.R
  * Purpose: Performs confirmatory factor analysis with 18 items, excluding "Deep Conversation."
  * Input data: `Study2Data.csv`, containing ratings from 201 participants on 19 scale items across all four videos (Healthcare, Hold Hands, Pet, Conversation). The videos can be accessed [here](https://osf.io/5ezga/?view_only=f857949cfe1e49dd8f75ce1aac206b9f).
  * Result Interpretation: The CCR scale demonstrates good fit based on the Comparative Fit Index (CFI), Tucker-Lewis Index (TLI), and Standardized Root Mean Square Residual (SRMR): CFI = 0.997 (>= 0.95), TLI = 0.996 (>= 0.95), and SRMR = 0.046 (<= 0.08). However, the Root Mean Square Error of Approximation (RMSEA) indicates only a moderate fit: RMSEA = 0.096 (<= 0.08).

* CorrelationCoefficient.R
  * Purpose: Compare the correlation between the 18-item CCR Scale and the Gratch Rapport Scale.
  * Input data: `Study2DataForOrdinalRegression.csv`, containing five columns: Video (Healthcare, Hold Hands, Pet, Conversation), Ranking (rapport ranking from 1 = lowest to 4 = highest), Gratch (Gratch Rapport Scale score), CCR (CCR Scale score), and Subject (participant ID from 1 to 201).
  * Result Interpretation: The correlation coefficient is 0.84, indicating a strong positive correlation.
* ordinalRegression.R
  * Purpose: Evaluate model fit using AIC for the ordinal regression of the CCR Scale and the Gratch Rapport Scale.
  * Input data: `Study2DataForOrdinalRegression.csv`.
  * Result Interpretation: The AIC for the CCR Scale model is 1874.23, while the AIC for the Gratch Rapport Scale model is 1914.33. CCR Scale model is a better model because it is more than 2 units lower than Gratch Rapport Scale model.
* NagelkerkeRsquared.R
  * Purpose: Compute Nagelkerke R-squared for the ordinal regression of the CCR Scale and the Gratch Rapport Scale.
  * Input data: `Study2DataForOrdinalRegression.csv`.
  * Result Interpretation: The Nagelkerke R-squared value is 0.39 for the CCR Scale and 0.35 for the Gratch Rapport Scale. A higher Nagelkerke R-squared value indicates a better model fit.
* cronbachAlpha.R
  * Purpose: Assess the internal reliability of the 18-item CCR Scale and the Gratch Rapport Scale using Cronbach's alpha.
  * Input data: `Study2Data.csv` and `Study2GratchAlreadyReversed.csv`, where we have already reverse-coded the items that need to be reverse-coded.
  * Result Interpretation: The Cronbach's alpha for the CCR Scale is 0.97, and the Cronbach's alpha for the Gratch Rapport Scale is 0.89.
* omega.R
  * Purpose: Assess the internal reliability of the 18-item CCR Scale and the Gratch Rapport Scale using McDonald's omega.
  * Input data: `Study2Data.csv` and `Study2GratchAlreadyReversed.csv`.
  * Result Interpretation: McDonald's omega for the CCR Scale is 0.97, and McDonald's omega for the Gratch Rapport Scale is 0.94.

## Study 3

* CorrelationCoefficient.R
  * Purpose: Compare the correlation between the 18-item CCR Scale and Perceived Robot Responsiveness ratings.
  * Input data: `Study3_CorrelationCoefficient.csv`, containing three columns: rapportscore (CCR Scale score from 44 participants), condition (0 = Unresponsive Condition, 1 = Responsive Condition), perceived_robot_responsiveness (ratings from 44 participants).
  * Result Interpretation: The correlation coefficient is 0.83, indicating a strong positive correlation. In the paper, we made a small mistake by marking it as 0.75.
* cronbachAlpha.R
  * Purpose: Assess the internal reliability of the 18-item CCR Scale using Cronbach's alpha.
  * Input data: `Study3Data.csv`.
  * Result Interpretation: The Cronbach's alpha for the CCR Scale is 0.95.
* omega.R
  * Purpose: Assess the internal reliability of the 18-item CCR Scale using McDonald's omega.
  * Input data: `Study3Data.csv`.
  * Result Interpretation: McDonald's omega for the CCR Scale is 0.96.
* study3.Rmd
  * Purpose: Analyze the data (e.g., CCR Scale ratings) across the two conditions. Click on the knit function to generate a html file summarizing the results.
  * Input data: `Study3Data.csv` containing data collected during Study 3, and `Study3QualitativeData.csv` containing qualitative coding of participants' interactions.
  * Result Interpretation: Refer to Table III in the paper for the statistical results.

# CCR Scale Study 3 Robot Code

If you have not previously used ROS2 and Misty, or do not have the necessary Python packages, see the prerequisites for software installation instructions.

* **personal laptop mac** denotes the Wizard of Oz laptop but not in the virtual machine.
* **personal laptop virtual machine** denotes that same laptop but in the virtual machine.
* **slides laptop** denotes the lab laptop displaying slides.
* **video laptop** refers to the laptop connected to a webcam and using Zoom and Cheese.

## Experiment Setup
<img src="https://github.com/SeboLab/CCR_Scale/blob/1eba5b2ad4567e669233c10af126aed3be9b6ab0/Study3_Code/Study3Setup.png" width="600">

## Using the virtual machine

1. Connect the personal laptop mac to the Sebo-Lab-01 wifi network.
2. In the terminal of the personal laptop mac, run `python3 -m http.server`. 
3. Launch the UTM virtual machine. It might take several minutes to load.
4. In the terminal window in the personal laptop virtual machine, run `python3 -m http.server`
5. Open the MistySubscriber2.py file using your preferred code editor.

## Using Misty

### Connecting to Misty

1. Turn on Misty using the switch in the back. Misty should be on the Sebo-Lab-01 network.
2. Use the Misty App to find Misty's IP address.
3. Change the `misty_ip` in MistySubscriber2.py to match. 
4. In the MistySubscriber2.py file, change `my_ip` to be your personal laptop mac's IP address when connected to the Sebo-Lab-01 wifi network. This is the same IP address used for port forwarding.
5. In the virtual machine, in a seperate terminal window from the one doing port forwarding, build the ROS2 workspace (`cd ~/ros2_ws` then `colcon build` then `source install/setup.bash`). 

### Changing Misty's Voice and Volume

Put Misty's IP address in a new tab in a web browser on the personal laptop mac. Change the voice using the dropdown and change the volume using the slider at the top of the screen. For changing Misty's voice, you might have to play something using the web browser in order to get the voice to actually change.

## Running the Study

1. Follow the above instructions for starting the virtual machine and Misty.
2. Connect the slides laptop to the Sebo-Lab-01 wifi. 
3. On the personal laptop mac in a seperate terminal window from the one runnin `python3 -m http.server`, run the socketServer.py file (`python3 socketServer.py`).
4. On the slides laptop, change the `server_ip` in socketClient.py (on the Intro Robo L01 it is called socketClient1.py and in the Documents folder) to the personal laptop mac's ip address when connected to the Sebo-Lab-01 wifi.
5. On the slides laptop, run the socketClient.py file using `python3 socketClient.py`.
6. In the prompt that pops up (->) type the word "address". It should display two lines that both read "Received from server: ADDRESS".
7. In the personal laptop virtual machine, in the SlidesSubscriber.py file, change `self.server_ip` to be the ip address of the personal laptop mac.
8. In the personal laptop virtual machine in the ros2_ws directory (`cd ~/ros2_ws`), run `colcon build` then `ros2 launch rapport rapport_launch.py`. It will then pop up with the window for controlling Misty and the slides.
9. You can test that things are working by changing the slide using the window in the virtual machine and make sure that the slides laptop prints "Received from server: \[number\]" in the terminal window with the socketClient.py file running.
10. Click the Blank slide button in the pop window on the personal laptop virtual machine.
11. In a seperate terminal window on the slides laptop from the one that is running socketClient.py, run the display.py file (on the Intro Robo L01 it is called display1.py and in the Documents folder) with `python3 display.py`. If you need to close the display on the slides laptop and cannot access it from the personal laptop virtual machine, use the hidden button located at the top of the screen slightly to the right of the webcam. The button will turn gray when the mouse is over it. You may need to click this button multiple times.
12. Try changing the slides using the pop up in the personal laptop virtual machine. For each slide, before you show the next one, make sure to click the Blank slide button so that the text does not appear on top of each other.
13. Press the slow head nod button and make sure Misty's head is moving appropriately. You may need to press this button a few times.
14. Connect the video laptop and your phone to a wifi network other than the Sebo-Lab-01 network.
15. Connect the video laptop to a webcam and the USB microphone
16. Start a zoom meeting using your phone, turn off your video, and mute your microphone. You might want to use headphones to hear the audio.
17. Join the zoom meeting on the video laptop and turn off video, mute the volume, but unmute the microphone. Change the microphone in the Zoom meeting to the USB microphone. Change the video in the Zoom meeting to the built in camera (not the webcam).
18. Open Cheese on the video laptop and start recording.
19. Set up the stand alone camera and start recording.
20. Reference the experimenter script for how to run the study.

### Shutting down the devices

1. Shut down the slides using the Shut down slides button in the pop up window. 
2. Stop all the programs running in terminal windows in the virtual machine and on the slides laptop using control+C. 
3. Shut down the virtual machine using the button inside the virtual machine to shut it off, not the button on UTM.
4. Turn off Misty using the switch in the back. 
5. Shut down the terminal programs on the personal laptop mac.

### Other notes

* The speak button and the unresponsive speech buttons stop and reset the timer, and the slide buttons start the timer.
* If the slides laptop is not responding to anything while displaying slides, turn it off and on twice using the power button.
* If you would like the displaying slides to still be controllable from the user, comment out the `win.attributes('-fullscreen',True)` line and uncomment the `win.geometry("500x500")` line (you can change the width and height to better fit the screen).

## Prerequisites

The following hardware and software is necessary for running this experiment:
1. Mac laptop
    - Python3 with socket library
         -  Download the socketServer.py file (located in the other_devices folder) onto the personal laptop mac
    - UTM Ubuntu 24.04 virtual machine with ROS2 Jazzy, Python3, and port forwarding set up if necessary
         - Have this git repository cloned into the `~/ros2_ws/src` directory
    - Misty App
3. Ubuntu laptop
    - Python3 with tkinter, csv, and socket libraries
         - Download the display.py and socketClient.py (located in the other_devices folder) files onto the slides laptop
4. Ubuntu laptop
    - With Zoom and Cheese applications
    - USB webcam and microphone
5. Misty robot
6. Stand alone camera
7. Wifi router
    - In this case, we are using a router called Sebo-Lab-01

### Virtual machine installation instructions

Installation [Instructions](https://techblog.shippio.io/how-to-run-an-ubuntu-22-04-vm-on-m1-m2-apple-silicon-9554adf4fda1) for Ubuntu in a UTM virtual machine for Mac computers with an M1 or M2 chip
> [!IMPORTANT]
> In step 2 where it says to download Ubuntu server 22.04-arm64, download [24.04](https://ubuntu.com/download/server) instead

### ROS2 installation instructions

Installation [instructions](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debians.html) for ROS2 Jazzy. Install the Desktop Install instead of the ROS-Base Install.

Then [configure your ROS2 environment](https://docs.ros.org/en/jazzy/Tutorials/Beginner-CLI-Tools/Configuring-ROS2-Environment.html) using steps 1 and 2.

Instructions for creating a ROS2 workspace: 
* First [install colcon](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html)
* Then create a workspace following the first two steps of this [tutorial](https://docs.ros.org/en/jazzy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)

You might also want to [add your SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) into the virtual machine or create a personal access token in order to access this github repository.

### Python Packages needed in the virtual machine

You can install packages using `python3 -m pip install <package name>` or `apt install python3-<package name>`. The packages you might need to install are:
* tkinter
* requests
* socket

If it gives you an error when you try to install them, it likely means the packages are already installed. 

### Set up port forwarding

To set up port forwarding in UTM, before you launch the virtual machine, first connect to the Sebo-Lab-01 wifi. Then open up the UTM settings of the virtual machine and change network mode to Emulated VLAN. Go to Devices > Network > Port Forwarding. Add a new port forwarding that should be Protocol: TCP, Guest Address: 10.0.2.15, Guest Port: 8000, Host Address: <your computer's ip address>, Host Port: 8000.

To find your <your computer's ip address> on Mac, go to WiFi (assume you are connected to Sebo-Lab-01), go to Details..., and find IP address.

### Misty App installation instructions

You can find the app in the app store and install it on your Mac computer.

### Using this repository

Clone this repository into the src folder of ros2_ws in the virtual machine.

Locate the Rapport/rapport/other_devices folder in the github and put the socketServer.py file on the personal laptop mac and the socketClient.py and display.py files on the slides laptop. 

## Bibtex Citation

```bibtex
@inproceedings{10.5555/3721488.3721594,
author = {Lin, Ting-Han and Dinner, Hannah and Leung, Tsz Long and Mutlu, Bilge and Trafton, J. Gregory and Sebo, Sarah},
title = {Connection-Coordination Rapport (CCR) Scale: A Dual-Factor Scale to Measure Human-Robot Rapport},
year = {2025},
publisher = {IEEE Press},
abstract = {Robots, particularly in service and companionship roles, must develop positive relationships with people they interact with regularly to be successful. These positive human-robot relationships can be characterized as establishing ''rapport,'' which indicates mutual understanding and interpersonal connection that form the groundwork for successful long-term human-robot interaction. However, the human-robot interaction research literature lacks scale instruments to assess human-robot rapport in a variety of situations. In this work, we developed the 18-item Connection-Coordination Rapport (CCR) Scale to measure human-robot rapport. We first ran Study 1 (N = 288) where online participants rated videos of human-robot interactions using a set of candidate items. Our Study 1 results showed the discovery of two factors in our scale, which we named ''Connection'' and ''Coordination.'' We then evaluated this scale by running Study 2 (N = 201) where online participants rated a new set of human-robot interaction videos with our scale and an existing rapport scale from virtual agents research for comparison. We also validated our scale by replicating a prior in-person human-robot interaction study, Study 3 (N = 44), and found that rapport is rated significantly greater when participants interacted with a responsive robot (responsive condition) as opposed to an unresponsive robot (unresponsive condition). Results from these studies demonstrate high reliability and validity for the CCR scale, which can be used to measure rapport in both first-person and third-person perspectives. We encourage the adoption of this scale in future studies to measure rapport in a variety of human-robot interactions.},
booktitle = {Proceedings of the 2025 ACM/IEEE International Conference on Human-Robot Interaction},
pages = {869–879},
numpages = {11},
keywords = {human-robot interaction, human-robot rapport, rapport, scale development},
location = {Melbourne, Australia},
series = {HRI '25}
}

```
