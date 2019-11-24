# SpleeterBox
SpleeterBox is an implementation of Deezer's Spleeter library, that allows audio separation through the use of Machine Learning, this project is nothing fancy but I hope it helps some people out there. 
<br>
<br>

I created this GUI implementation due to the requests on Dylan Tallchief’s video about the Library, I think this way is better than writing the command using CMD or Powershell every time you want to separate a song. <br>

<b>Relevant Info<b/>: <br>
Dylan's Video: https://www.youtube.com/watch?v=tgnuOSLPwMI

If you guys find it useful you can <br>
invite me a coffee via paypal here <br>
<b>Donations<b/>: https://paypal.me/jramirezp332?locale.x=es_XC

# First Use
When you first Use the GUI App it will take a while to finish the separation process, this happens since it needs to download the pretrained models from Deezer's sources, then the app creates a folder inside the SpleeterBox folder named pretrained_models and it stores the models there, this process is the same for every new model you use (every separation option), but it happens just the first time you use every option, then when you use that option again it will be a lot faster cause it already saved the models.
The duration of the first time you use every model (Separation Option) will depend on your connection speed

<b>Pretrained Models Estimated Sizes<b/> <br>
 2 Stems -> 75,7 MB <br>
 4 Stems -> 151 MB <br>
 5 Stems -> 189 MB <br>

# Usage
The usage is very simple, first you just need to make sure you had installed and tested python and spleeter as explained in Dylan's Video (The one up there &#8593;), once you have done that you just need to download this project as a .zip
<br>
<img src="Images/Download.png" width="">

Once you have the zip file you just need to extract the folder using Winrar or windows default zip files manager, then you should move the folder to a location like My Documents just to make sure you won't delete it by accident then when you have the folder with the files in a secure place you just need to go inside it and double click the .cmd file to execute the python app
<br>
<img src="Images/cmdexe.png" width="">

 Then it will open a window like this

<br>
<img src="Images/OpenCMD.png" width="">

It opens a CMD Window as well but you don't have to worry about it, you can just minimize that one and use the GUI window 

# Interaction

There are 3 buttons you can interact with 
<br>
1-Select File -> Opens Up a window to navigate the folders in your PC and select the file you want to separate
<br>
2-Select Dir -> Opens Up a window to navigate the folders in your PC and select the folder you want to save the resulting files
<br>
3-Separate Audio -> Once you've selected both File and Dir it starts the process of audio separation

<b>Separation Options:<b/>

These are the ways you can split the audio, you just need to click the one you desire and then click on the Separete Audio button start the process
<br>
<img src="Images/options.png" width="">

# Upadting Pretrained Models
<b>Deezer<b/> will probably update their pretrained models in the future so in order to update the ones inside the App you just need to go inside the SpleeterBox folder(where ever you put it) and then go inside the pretrained_models folder and delete the one you desire to update, and then the next time you use that option it will download the latest model from Deezer's Sources
 
<img src="Images/UpdateModels.png" width="">
  

