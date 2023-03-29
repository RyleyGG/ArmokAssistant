# The Armok Assistant

## Purpose
Leveraging the OpenAI API (currently GPT-3.5, soon-to-be GPT-4), the Armok Assistant aims to aid in day-to-day tasks. By integrating with third-party API's and other services (and with the switch to GPT-4 once I get access), the scope of action available to the Armok Assitant will increase over time.

## Interface
The Armok Assistant is meant to run as a background service, wherein the user and Armok interact primarily via speech. To safeguard information, Armok must be prompted by saying "Armok" before speech will be collected and sent off. With that said, the best practice remains to NOT divulge any sensitive information of any sort to Armok, ChatGPT, or indeed any other LLM.

## Planned Capabilities
* Interact with Spotify
    * Start a specific playlist or song
    * Recommend a song based on a playlist/user taste
* Interact with Google Calendar
    * Describe upcoming events
    * Edit events
* Help with math or physics problems
    * Given a problem, solve the problem for the user while explaining the steps
    * Given a problem, give the user hints as they request it
    * Given a concept (i.e. integration), generate an appropriate problem for the user to solve
* General Assistance/Conversation
    * Given that the Armok Assistant will be leveraging the OpenAI API, it should be capable, even without specific third-party integrations, of the level of assistance and conversation as ChatGPT normally is.