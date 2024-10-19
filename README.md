# CosyNightIn - Film finder

![Responsive Mockup](documentation/features/)

*The link to [CosyNightIn]()*

## About

CosyNightIn is an app that allows you to search for the perfect film to watch depending on your mood, it will use a varity of filters to narrow down the choice and provide a relaxed way to pick what to watch.

---

## User Experience Design

### Strategy
  1. 

  2. 

  3. 

  4. 

  5. 

  6.  

  7.  

  8. 

  9. 

  10. 

  11. 

  12. 

---

### Target Audience

1. 



## User Stories
### First Time Visitor Goals:

* As a First Time Visitor, I want to quickly understand the program's primary purpose so that I can learn more about this program.

* As a First Time Visitor, I want to navigate through the program easily so that I can find the content.

* As a First Time Visitor, I want to find the program useful for myself so that I can fulfill my expectations and have fun.

* As a First Time Visitor, I want to see different text colors so it looks more enticing, and the different parts of the game are easily distinguishable.


### Frequent Visitor Goals:

* As a Frequent User, I want to be able to play as many times as I like and not worry about a word being repeated, variation is key in this game.
* As a Frequent User, I will want to explore the other game option, multiplayer.

---

## Features
  
  - 

  - 

  - 

  - 


![loading Program](documentation/features/)

![loading Program](documentation/features/)

![loading Program](documentation/features/)

![loading Program](documentation/features/)

---

## Flowchart

The flowchart represents the logic of the application:

  ![Flow chart Page](documentation/features/flowchart.png)

---

## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) used to edit and adjust the styling and color scheme throughout the app production

### Frameworks/Libraries, Programmes and Tools:

#### Python modules/packages:

##### Standard library imports:

- [random](https://docs.python.org/3/library/random.html) was used to implement pseudo-random word selection from word bank.
- [os](https://docs.python.org/3/library/os.html) was used to clear the terminal before running the program.
- [String](https://docs.python.org/3/library/string.html) processes standard strings in various ways in python.

##### Third-party imports:

- [Random Lists](https://www.randomlists.com/data/words.json) Word bank used for word pool for the game.
- [Colorama](https://pypi.org/project/colorama/) was used to add colors and styles to the project.


#### Other tools:

- [VSCode](https://code.visualstudio.com/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.
- [Techsini](https://techsini.com/) used to create the head mock up picture for the readme.
- [Miro](https://miro.com/app/dashboard/) was used to make a flowchart for project planning and the README file.
- [Gitpod](https://gitpod.io/workspaces) was used to create the workspaces.
- [Heroku](https://id.heroku.com/) Used to deploy finished project.
- [CIlintercheck](https://pep8ci.herokuapp.com/) Code institute Linter validator for python. Used to validate all python files.
- [SQLite3](https://sqlitebrowser.org/) SQLite3 was used to import external DB for filter use.
- [FaviconGenerator](https://favicon.io/favicon-generator/) Used to create custom favicon
---

## Bugs

- Initial heroku deployment returned an error message. (solution - I forgot to add the Procfile before initial deployment)

- Wehn trying to add the filter models/view to the browser, the code was running without an error but the view didnt appear in the browser. (Solution - I forgot to add the model to admin.py therefore it wasnt looking for it.)

![Screenshot](documentation/bug_screenshots/)

#### The next screen shots show the code added to prevent this happening.

![Screenshot](documentation/bug_screenshots/)

![Screenshot](documentation/bug_screenshots/)

![Screenshot](documentation/bug_screenshots/)

2. 

*Solution:* 

- 

![Screenshot](documentation/bug_screenshots/)

3. 

*Solution:*

-

![Screenshot](documentation/bug_screenshots/)

![Screenshot](documentation/bug_screenshots)

![Screenshot](documentation/bug_screenshots/)

4. 

![Screenshot](documentation/bug_screenshots/)

*Solution:* 

- 

5. 

*Solution:*

- 

![Screenshot](documentation/bug_screenshots/)

6. 

![Screenshot](documentation/bug_screenshots/)

*Solution:*

- 

![Screenshot](documentation/bug_screenshots/)

7. 

![Screenshot](documentation/bug_screenshots/)

![Screenshot](documentation/bug_screenshots/)

## Information Architecture

### Database
### ER Diagram
### Data Modelling


## Design

### Color Scheme

### Typeography

### Imagery

### Wire Frames

### Flow Charts

## Testing

- 

- ![screenshot](documentation/validation/)

- Testing was carried out using the CI Linter check web page [CI Linter Validation](https://pep8ci.herokuapp.com/#)

- Please see below for validation screen shots.

## Validation

### run.py Linter Validation

![Screenshot](documentation/validation/)

### player.py Linter Validation
![Screenshot](documentation/validation/)

### words.py Linter Validation
![Screenshot](documentation/validation/)

## Manual testing

| feature | action | expected result | tested | passed | comments |
| --- | --- | --- | --- | --- | --- |
| Main Title and Menu | | | | | |
| Main title | Visual representation of the game | Aligned properly and clearly readable | Yes | Yes | - |
| Menu Display | Select the menu option number desired | The user is redirected to either the rules, a new game or the exit screen | Yes | Yes | - |
| Game start | User asked for number of players and player names | Input taken and data used to start the game | Yes | Yes | - |
| Main Game | | | | | |
| 1 Player Game | Play a solo game | Go through a solo game with no errors and all potential bugs thought about and dealt with | Yes | Yes | - |
| 2 & 3 Player Game | Play a 2 or 3 player game | As above, however, each player is different colours and its clearly defined | Yes | Yes | - |
| Game Ending | When a player either guesses the correct word or runs out of guesses | The user is told if they won or lost, if they lost the word will be revealed | Yes | Yes | - |
| Playing the game | Play the game, without issues | The game is played, the players amount of guesses and letters already guessed is clearly displayed along with the word your attempting to guess. The correct letters appear in the correct space and constantly on display | Yes | Yes | - |
| Rules | | | | | |
| List of rules | The rules are listed numerically, in a different color font | The user can gain a clear understanding of the game and how to play it | Yes | Yes | - |
| Exit | | | | | |
| Exit button | Select this menu option to leave the game | The user is given a goodbye message and the programme exits back to the python terminal | Yes | Yes | - |


## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com).
- The program can be reached by the [link](https://hang-man888-99eb4815e363.herokuapp.com/)

### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  2. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/Joeski88/hang_man)
  2. Click the Code button and download the ZIP file containing the project.
  3. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  2. Run the following command
  - `git clone https://github.com/Joeski88/hang_man`

- Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

  [![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Joeski88/hang_man)

  1. Install Python module dependencies:
     
      1. Navigate to the folder hang_man by executing the command:
      - `cd hang_man`
      2. Run the command pip install -r requirements.txt
        - `pip3 install -r requirements.txt`

### To deploy the project to Heroku so it can be run as a remote web application:
- Clone the repository:
  1. Open a folder on your computer with the terminal.
  2. Run the following command
    - `git clone https://github.com/Joeski88/hang_man.git`
  3. Create your own GitHub repository to host the code.
  4. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.
  5. Push the files to your repository with the following command:
    - `git push`
  6. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).
  7. Create a new Heroku application on the following page here [New Heroku App](https://dashboard.heroku.com/apps):
  8. Go to the Deploy tab. 
      - ![Deploy](documentation/deployment/heroku_deploy_tab.png)
  9. Link your GitHub account and connect the application to the repository you created. 
      - ![github](documentation/deployment/deployment_method.png)
  10. Go to the Settings tab.
  11. Click "Add buildpack". 
  12. Add the Python and Node.js buildpacks in the following order.
      - ![Buildpack](documentation/deployment/buildpacks.png)
  13. Click "Reveal Config Vars." 
  14. Add 1 new Config Vars:
      - Key: PORT Value: 8000
      - *This Config was provided by [CODE INSTITUTE](https://codeinstitute.net/)*.
      - ![ConfigVars](documentation/deployment/config_vars.png)
  15. Go back to the Deploy tab.
  16. Click "Deploy Branch".
        - Wait for the completion of the deployment. 
        - ![Deploy](documentation/deployment/deploy.png)
  17. Click "Open app" to launch the application inside a web page.


## Credits

- Favicon Design Tool [Favicon](https://favicon.io/favicon-generator/).
- Rotten Tomatoes for the links and data [Rotten Tomatoes](https://www.rottentomatoes.com/) Used Rotten tomatoes and a reference for all movies provided to the database.
- Kaggle [Kaggle](https://www.kaggle.com/datasets?search=rotten+tomatoes) Database hub that I pulled the movie databse from.
- Bootstrap [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) Used Bootstrap documentation to help guid me to the correct code to use and what its for.



## Acknowledgements
- My Mentor Iuliia Konovalova. I had issues with the help i was recieving with my previous mentor, 
  but i noticed a huge difference with the way Julia spoke to me and how she managed my situation, 
  she deserves alot of credit and praise for 