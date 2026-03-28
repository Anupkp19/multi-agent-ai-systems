
### The not-so-dreaded setup instructions

Perhaps famous last words: but I really, truly hope that I've put together an environment that will be not too horrific to set up!

- Windows people, your instructions are [here](setup/SETUP-PC.md)
- Mac people, yours are [here](setup/SETUP-mac.md)
- Linux people, yours are [here](setup/SETUP-linux.md)

Any problems, please do contact me.

Windows PC users: you will need to have checked the "gotcha #4" at the top of the [SETUP-PC](setup/SETUP-PC.md) instructions -- installing Microsoft Build Tools.  
If you don't do this, then CrewAI will fail with an obscure error involving Chroma..


Then, you will need to run this command in a Cursor Terminal in the project root directory in order to run the Crew commands:  
`uv tool install crewai==0.130.0 --python 3.12`   
And in case you've used Crew before, it might be worth doing this to make sure you have the latest:  
`uv tool upgrade crewai==0.130.0 --python 3.12`  

This command pins Crew to the same version that I use on the course. If you have any problems with Crew, you could try using the latest version instead, by running this command:  
`uv tool upgrade crewai --python 3.12`  

At any point, you can see which version of Crew you have installed with this:  
`uv tool list`




### API costs - please read me!

This course does involve making calls to OpenAI and other frontier models, requiring an API key and a small spend, which we set up in the SETUP instructions. If you'd prefer not to spend on API calls, there are cheaper alternatives like DeepSeek and free alternatives like using Ollama!

Details are [here](guides/09_ai_apis_and_ollama.ipynb).

Be sure to monitor your API costs to ensure you are totally happy with any spend. For OpenAI, the dashboard is [here](https://platform.openai.com/usage).