# ViewerOnLoL

```
 _      ______          _____ _    _ ______          __   _      ______ _____ ______ _   _ _____   _____ 
| |    |  ____|   /\   / ____| |  | |  ____|        / _| | |    |  ____/ ____|  ____| \ | |  __ \ / ____|
| |    | |__     /  \ | |  __| |  | | |__      ___ | |_  | |    | |__ | |  __| |__  |  \| | |  | | (___  
| |    |  __|   / /\ \| | |_ | |  | |  __|    / _ \|  _| | |    |  __|| | |_ |  __| | . ` | |  | |\___ \ 
| |____| |____ / ____ \ |__| | |__| | |____  | (_) | |   | |____| |___| |__| | |____| |\  | |__| |____) |
|______|______/_/    \_\_____|\____/|______|  \___/|_|   |______|______\_____|______|_| \_|_____/|_____/ 
```



## Description
ViewerOnLoL is a  tool designed for League of Legends players looking to deepen their understanding of the game. Whether you're a beginner seeking to improve your skills or a veteran looking to fine-tune your strategy, ViewerOnLoL provides a detailed analysis of your profile and your matches.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- Python
- GitBash

- A Database (we used SQLite)
- A Riot API Key


### Installation
1. Get an API Key at [https://developer.riotgames.com/](https://developer.riotgames.com/) (_Must have an Riot Games account_)


2. Clone the repo
   ```bash
   git clone https://gitlab.com/projet-info-2a-groupe-11/outil-analyse-lol
   ```

3. Install all the necessary libraries

   ```bash
   pip install -r requirements.txt
   ```

4. Enter your API & Database Access in `.env`
   ```js
   HOST_WEBSERVICE_EUW1 = https://euw1.api.riotgames.com
   HOST_WEBSERVICE_EUROPA = https://europe.api.riotgames.com
   API_KEY = RGAPI-e6747bea-8be1-485f-aa91-3da5d892b425

   HOST=sgbd-eleves.domensai.ecole
   PORT=5432
   DATABASE=id2321
   USER=id2321
   PASSWORD=id2321
   ```

5. Execute the script

   ```sh
   python "src/__main__.py" 
   ```



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

## Contact
