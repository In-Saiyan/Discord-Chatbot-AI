# Discord-Chatbot-AI
An AI made with Keras ( used the code of <a href="https://github.com/NeuralNine/neuralintents">NeuralNine's NeuralIntents</a>) to implement Speech Recognition. This pairs the neuralintents with the discord.py inorder to make a chatbot that can recognise speech based on patterns and give recorded responses.


<h1>Deployment:</h1>
This will guide through on How to deploy your own bot.
<h3>Dependencies:</h3>

 * <a href="https://www.python.org/downloads/">Python</a>
 
 
 After Installing it should show something like:

 
 ![image](https://user-images.githubusercontent.com/91674437/186214289-3fb6b5a7-4de5-415e-b8a4-11ddf0b25a38.png)

 
 If it doesn't well. Reinstall. Or you might want to check the "Add to PATH option" (You can do it mannually)
 
 * Discord.py
   - After installing Python and adding the executable to the PATH in your environment variable(It happens automatically but in case if it doesn't works you have to do it mannually.)
   - Type in the Command Prompt/ PowerShell in Windows or Terminal in Mac/Linux:
 
Windows:

```
 pip install discord.py
```
 Mac/Linux:
```
 pip3 install discord.py
```

 
 * Tensorflow
   - Install it using pip.

Windows:

```
 pip install tensorflow
```
 Mac/Linux:
```
 pip3 install tensorflow
```



   - Now you're good to go.
<h3>Get Your Token</h3>
 Too lazy to explain (XD) so I will recommend Tyrrrz' Guide to otain your bot token <a href = "https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-a-bot-token">here</a>. 

<h3>Adding the token to the config.</h3>
Since the bot is in the development stage and it's simple as hell...(Probably not cuz I'm lazy, I'm just dumb XD)~ Anyways, there's only one option as of now just replace the "<TOKEN>" by your actual bot token in the [.env file](/.env) .
  
<h3>Running the bot</h3>
  Bro you're for real?
  Open the terminal and change the directory to the main folder where main.py is present, then type in:

  
Windows:
```
 python bot.py
```
Mac/Linux
  ```
  python3 bot.py
  ```


 
 <b>NOTE: The commented line are the ones that will enable the logging, if you want to log the messages be sure to use it but there's a problem in using them in Windows, it works perfectly on Mac and Linux though.</b>
 
 If you want to contribute in making this something good you can <a href="https://discord.gg/YM74PGgYPq">Join us on Discord.</a>.
