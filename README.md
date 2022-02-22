# Project 1 Generative Text

Reid Brockmeier, rbrockmeier2@unl.edu

Result video: [Pokemon, but you cannot see them, they are invisible!](https://www.youtube.com/watch?v=x1_liPYByMQ)

## Abstract


The original concept for this project was to gather a list of the most popular/trending videos on YouTube and use it as training data to generate YouTube video titles in order to solve the algorithm in a way. To prove this concept, I planned to create a video based on this generated title. While gathering the data, the source of it changed a bit. I discovered a repository to scrape all the titles from a list of channels, and with this I was able to hand pick channels that went more with my category of video creation. The goal of the project also shifted from generating a title that will perform well to using it as a tool for generating video ideas. I modified the video-scraper a bit and provided a list of channels that I wanted to emulate. I ran 2 python scripts to produce a txt file with over 45,000 titles. This list was used as training data to create a GPT-2 model that generates titles. This was implemented within a version of the class example GPT-2 notebook that had modified parameters and some removed cells. I specified a prefix of "Pokemon, but" to produce Pokemon challenge ideas because that is most of what I post on my channel. A list of 100 titles with this prefix was generated. These titles were, for the most part, coherent and usable. I chose the second one, being, "Pokemon, but you cannot see them, they are invisible!" With the title, I created a custom ROM of Pokemon FireRed and played through it as a challenge. This was streamed and edited into a 20 minute YouTube video. As of the first 11 hours of being live on YouTube, the video is performing quite a bit worse than the average does on my channel, but high video performance is no longer the goal. I am glad that with the shifted data source, my goal for this project shifted as well. It would be unrealistic to expect good performance on a video just based on a title because many other factors play a large role in the YouTube algorithm. This alleviates the stress that my human error would inevitably cause. I feel that this project was a success in the fact that this could genuinely be used as a tool for video concepts. It is not exclusive to creating Pokemon titles; simply adjusting the prefix would produce an entirely different list. I am very happy with how this project turned out, and I will likely refer back to the list produced and generate more in the future.

## Model/Data

Training Data:

- The training data was collected from the titles of all videos from a list of channels that I chose specifically using minimaxir's youtube video scraper repository. Slight modifications were made, such as a few lines to create a txt file from the csv in order to be used as training data.

     - Minimaxir's Repository:
         - [YouTube Video Scraper](https://github.com/minimaxir/youtube-video-scraper)


- The channels chosen were all gaming-related and consist of many of the top channels on the site and some that I would like to emulate. This text contained 717405 tokens.

- The code to produce this is included in [video-scraper](https://github.com/unl-ml-art/generative-text-ReidDotO/tree/master/video-scraper)

    - List of over 46,000 titles:
        - [titles.txt](titles.txt)

Trained models:
- I was unable to get the trained model to push to git, it kept having errors while pushing. (could be due to the large file sizes)


- Process and results from training/generating are documented within:
    - [gpt2-generate-finetune.ipynb](gpt2-generate-finetune.ipynb)


- The model was trained with the [titles.txt](titles.txt) file.


- Mostly default values were used and it ran 1 run with 200 steps total. This was all that was necessary for the fairly large training data that was used.

## Code

Training Data Code:
- [video-scraper](https://github.com/unl-ml-art/generative-text-ReidDotO/tree/master/video-scraper)


Text Generation Code:
- [gpt2-generate-finetune.ipynb](gpt2-generate-finetune.ipynb)

## Results

- File containing 100 different generated titles:
    - [output_20220219_202058.txt](output_20220219_202058.txt) 


- The results were on a wide variety of games/topics. It is for this reason that I chose a small length and large sample size. This way it provided many titles with my desired prefix.


- Chosen Title
    - "Pokemon, but you cannot see them, they are invisible!"
        - This was the second result using the prefix, "Pokemon, but"
        - Chosen because it provided an interesting concept that was feasible. 

         
Finished YouTube Video:
- [Pokemon, but you cannot see them, they are invisible!](https://www.youtube.com/watch?v=x1_liPYByMQ)

## Technical Notes

It is possible to recreate this with different channels' videos used as the training data:
- To do this, you need your own API Key for the YouTube Data v3 API. 
    - Refer to: [README-SCRAPER.md](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/README-SCRAPER.md)
- Change the [config.yml](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/config.yml) file with your desired YouTube channel ID's
- Add a data folder within the video-scraper directory.
- Run [youtube_video_scraper.py](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/youtube_video_scraper.py)
    - In command line: "python youtube_video_scraper.py"
- Run [youtube_video_titles.py](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/youtube_video_titles.py)
    - In command line: "python youtube_video_titles.py"
- This will create "titles.csv" and "titles.txt" The txt file will be used later in the text generation.

To train and generate titles in the same manner, run each cell from the beginning of:
- [gpt2-generate-finetune.ipynb](gpt2-generate-finetune.ipynb)

Notes on video creation process:
- I had to create my own ROM Hack of a Pokemon game (FireRed) in order to do the challenge provided by the generated title.
    - I created my own custom sprite (image of pokemon used in-game) to replace each existing one. It had to be an indexed image 64x64 pixels with less than 16 colors. I made some slightly different colored dots scattered around.
    - I used a ROM hacking tool called [unLZ-GBA](https://www.romhacking.net/utilities/362/) to replace the different sprites.
        - This was a very long and dull process; I had to replace over 800 images with the app.


- To block out the pokemon names, rather than implementing it within the ROM, I made a group of images to cover the menuing and names that displayed in OBS. I played viewing the OBS scene projection and manually turned the overlay on/off with a hotkey each time I was in battle.


- I streamed the process of creating the ROM and playthrough on my Twitch channel: [ReidDotO](https://www.twitch.tv/ReidDotO)
    - [Creation VOD](https://www.twitch.tv/videos/1303767712)
    - [Gameplay VOD 1](https://www.twitch.tv/videos/1304016040)
    - [Gameplay VOD 2](https://www.twitch.tv/videos/1304712647)


- The gameplay took just over 12 hours to complete, and the editing process was about 8 hours.

## Reference

- Repositories
    - [YouTube Video Scraper](https://github.com/minimaxir/youtube-video-scraper)
    - [GPT-2 Text Generation (in-class example)](https://github.com/roberttwomey/ml-art-code)


- YouTube Channels
    - [PewDiePie](https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw)
    - [Markiplier](https://www.youtube.com/channel/UC7_YxT-KID8kRbqZo7MyscQ)
    - [SSSniperwolf](https://www.youtube.com/channel/UCpB959t8iPrxQWj7G6n0ctQ)
    - [Ninja](https://www.youtube.com/channel/UCAW-NpUFkMyCNrvRSSGIvDQ)
    - [WILDCAT](https://www.youtube.com/channel/UC-kOXc3gBwksVfmndSEz7jg)
    - [Ludwig](https://www.youtube.com/channel/UCrPseYLGpNygVi34QpGNqpA)
    - [SmallAnt](https://www.youtube.com/channel/UC0VVYtw21rg2cokUystu2Dw)
    - [Dream](https://www.youtube.com/channel/UCTkXRDQl0luXxVQrRQvWS6w)
    - [jacksepticeye](https://www.youtube.com/channel/UCYzPXprvl5Y-Sf0g4vX-m6g)
    - [DanTDM](https://www.youtube.com/channel/UCS5Oz6CHmeoF7vSad0qqXfw)
    - [SwaggerSouls](https://www.youtube.com/channel/UCMdGPato0IC5-zZjJIf-P9w)
    - [penguinz0](https://www.youtube.com/channel/UCq6VFHwMzcMXbuKyG7SQYIg)
    - [NICKMERCS](https://www.youtube.com/channel/UCDvm7YoLE5r3ZZ6MWyD2vGQ)
    - [Disguised Toast](https://www.youtube.com/channel/UCUT8RoNBTJvwW1iErP6-b-A)
    - [NoahJ456](https://www.youtube.com/channel/UCP9tAErY_RlX4RFKssE4ogg)
    - [MrBeast Gaming](https://www.youtube.com/channel/UCIPPMRA040LQr5QPyJEbmXA)
    - [Austin John Plays](https://www.youtube.com/channel/UCIIPl-DSCC0prKxGGnJrdGQ)
    - [DrDisRespect](https://www.youtube.com/channel/UCcJL2ld6kxy_nuV1u7PVQ0g)
    - [jschlattLIVE](https://www.youtube.com/channel/UC2mP7il3YV7TxM_3m6U0bwA)
    - [Mizkif](https://www.youtube.com/channel/UChl76B7zqfMcNzfMi9vJruw)
    - [Clint Stevens](https://www.youtube.com/channel/UCYsGgfAcQ91Fpda3_O-h0LA)
    - [Pokemon Challenges](https://www.youtube.com/channel/UCvjsnl6wNtVIm0i1sCpN9Uw)
    - [SMii7Y](https://www.youtube.com/channel/UCzXwjTI6c6mVn6oui_p6oiw)
    - [FaZe Jev](https://www.youtube.com/channel/UC7trU46U_9XPDtMnDbiDPUQ)
    - [VanossGaming](https://www.youtube.com/channel/UCKqH_9mk1waLgBiL2vT5b9g)
    - [LazarBeam](https://www.youtube.com/channel/UCw1SQ6QRRtfAhrN_cjkrOgA)


- Other Tools:
    - [unLZ-GBA](https://www.romhacking.net/utilities/362/)
    - [Custom Sprite How to](https://www.pokecommunity.com/showthread.php?t=208837)