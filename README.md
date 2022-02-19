# Project 1 Generative Text

Reid Brockmeier, rbrockmeier2@unl.edu

## Abstract

Include your abstract here. This should be one paragraph clearly describing your concept, method, and results. This should tell us what architecture/approach you used. Also describe your creative goals, and whether you were successful in achieving them. Also could describe future directions.

For this project, I will make a YouTube video based on a generated title. For the data to train from, I will compile a large list of titles of popular videos, including all from the trending tab and other large creators. If the amount of text I am able to gather is not enough to provide reasonable outputs, I would consider using the descriptions of the videos as well. With this, I expect to get a variety of interesting titles that are proven to catch the viewers' attention and get a large number of views. I will pick a title that provides a feasable concept for a video and actually make and upload it to YouTube to see how well the result performs. The title may end up not being exactly representative of the video, but it will be interesting to see how much of an impact the title has, especially when it is derived directly from the most popular videos on YouTube.

## Model/Data

Briefly describe the files that are included with your repository:

Trained models:

Training Data:

- The training data was collected from the titles of all videos from a list of channels that I chose specifically using minimaxir's youtube video scraper repository. Slight modifications were made, such as a few lines to create a txt file from the csv in order to be used as training data.

     - Minimaxir's Repository:
         - [YouTube Video Scraper](https://github.com/minimaxir/youtube-video-scraper)


- The channels chosen were all gaming-related and consist of many of the top channels on the site and some that I would like to emulate.

    - List of over 63,000 titles:
        - [titles.txt](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/titles.txt)

## Code

Training Data Code:
- [youtube_video_scraper.py](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/youtube_video_scraper.py)
- [youtube_video_titles.py](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/youtube_video_titles.py)
- [config.yml](https://github.com/unl-ml-art/generative-text-ReidDotO/blob/master/video-scraper/config.yml)

Text Generation Code:
- [gpt2-generate-finetune.ipynb](gpt2-generate-finetune.ipynb)

## Results

- Documentation of your generative text in an effective form. A file with your generated text (.pdf, .doc, .txt). 

- Talk about my different results

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

## Reference

References to any papers, techniques, repositories you used:
- Papers
  - [This is a paper](this_is_the_link.pdf)
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
    - [Northernlion](https://www.youtube.com/channel/UC3tNpTOHsTnkmbwztCs30sA)
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
