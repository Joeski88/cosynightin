# CosyNightIn - Film finder

![Responsive Mockup](documentation/features/)

*The link to [CosyNightIn](https://8000-joeski88-cosynightin-e6en1er8oxr.ws.codeinstitute-ide.net/)*

## About

CosyNightIn is an app that allows you to search for the perfect film to watch depending on your mood, it will use a varity of filters to narrow down the choice and provide a relaxed way to pick what to watch.

---

## User Experience Design

### Strategy

* The aim of this app is to give users a platform to be able to search and filter a movie database to find themselves a film to watch. It's desgined to be easy and quick to use, while also providing all the information needed to make an informed decision and pick the perfect movie for your evening.  

---

### Target Audience

* The app is aimed at anyone movie lovers, family, friends and partners that you always seem to argue with about what to watch.



## User Stories
### First Time Visitor Goals:

| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/Joeski88/cosynightin/issues/17)| As a First Time Visitor, I want to be able to easily creat an account to be able to access the main features of the app.|
|[#2](https://github.com/Joeski88/cosynightin/issues/18)|As a First Time Visitor, I want to be able to find and discover films to watch based on how im feeling and what kind of mood im in.|
|[#3](https://github.com/Joeski88/cosynightin/issues/3)|As a First Time Visitor, I want to be able to easily log out of my account for security reasons, after I have found the film I want to watch.|
|[#4](https://github.com/Joeski88/cosynightin/issues/4)|As a First Time Visitor, I want to be able to see detailed information of each film I look at to be able to make an informed decision on what to watch.|
|[#5](https://github.com/Joeski88/cosynightin/issues/7)|As a First Time Visitor, I want to be able to see detailed information of each film I look at via a link to the rotten tomatoes page (opened in a different tab) to be able to make an even more informed decision on what to watch.|
|[#6](https://github.com/Joeski88/cosynightin/issues/15)|As a First Time Visitor, I want to be able to use filters to streamline my search to narrow down the results to make my decision easier to make.|
|[#7](https://github.com/Joeski88/cosynightin/issues/10)|As a First Time Visitor, I want to be able to have the ability to read reviews of other users to help aid me make my decision.|


### Frequent Visitor Goals:

| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/Joeski88/cosynightin/issues/1)|As a Frequent Visitor, I want to be able to easily be able to reset my password if i have forgotten my details to be able to access my account whenever needed. |
|[#2](https://github.com/Joeski88/cosynightin/issues/8)|As a Frequent Visitor, I want to be able to rate films ive watched to help other users make a decision.|
|[#3](https://github.com/Joeski88/cosynightin/issues/9)|As a Frequent Visitor, I want to be able to comment on reviews left by others to agree with or disagree with other users and offer my insight too. Also to thank others who leave comments on my reviews. |
|[#4](https://github.com/Joeski88/cosynightin/issues/5)|As a Frequent Visitor, I want to be able to search using keywords or film titles to get information on specific films i could potentially watch. |
|[#5](https://github.com/Joeski88/cosynightin/issues/6)|As a Frequent Visitor, I want to be able to search using actor and actress names to get information on specific films i could potentially watch. |
|[#6](https://github.com/Joeski88/cosynightin/issues/12)|As a Frequent Visitor, I want to be able to filter by film rating (provided by rotten tomatoes) to narrow down the search for what I want. |
|[#7](https://github.com/Joeski88/cosynightin/issues/11)|As a Frequent Visitor, I want to be able to search using specfic genre names to get information on specific films i could potentially watch. |

### Admin Goals:

| Issue ID    | User Story |
|-------------|-------------|
|[#1](https://github.com/Joeski88/cosynightin/issues/13)| As an admin user, I want to be able to easily understand the main purpose of the app, so that I can learn more about this app. |
|[#2](https://github.com/Joeski88/cosynightin/issues/20)|As an admin user, I want to be able to add and approve new members/users so that I can manage the account and ensure the process and app is clean and restrict an abusive behaviour/language. |

---

## Features
  
  - Home page will provide and carousel of trending movies currently availabble to stream, for potentially a quick decision in what to watch. All will contain an external rotten tomatoes link to provide extra details on each film.

  - Once logged in the user will be able to use a variety of filters to use to streamline the result output and narrow down their search to make an easier choice.

  - Users will have the option of leaving reviews and comments on other reviews made by other users.


![loading Program](documentation/features/)

![loading Program](documentation/features/)

![loading Program](documentation/features/)

![loading Program](documentation/features/)

---

## Flowchart & Entity Relationship Diagrams

The flowchart represents the logic of the application:

  ![Flow chart Page](/static/images/flowchartprocess.png)

---

The entity relationship diagrams for all models used in the application:

  ![ERDscreenshots](/static/images/erdiagrams.png)

---

The relationships used in the application:

  ![Relationships](/static/images/relationships.png)

## Technologies Used

### Languages:

- [Python 3.8.5](https://www.python.org/downloads/release/python-385/): used to anchor the project and direct all application behavior

- [JavaScript](https://www.javascript.com/): used to provide the start script needed to run the Code Institute mock terminal in the browser

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) used to construct the elements involved in building the mock terminal in the browser

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) used to edit and adjust the styling and color scheme throughout the app production

### Frameworks/Libraries, Programmes and Tools:

- [Django](https://www.djangoproject.com/): python framework used to create the project.
- [jQuery](https://jquery.com/): was used to control click events.
- [Bootstrap](https://getbootstrap.com/): Frameworks used to style parts of the app.

#### Python modules/packages:

- [SQLite](https://www.sqlite.org/): was used to store rotten tomatoes database.
- [PostgreSQL](https://www.postgresql.org/): the database used to store all the data on admin side.

##### Standard library imports:

##### Third-party imports:

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
- [FaviconGenerator](https://favicon.io/favicon-generator/) Used to create custom favicon.
- [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
- [Gunicorn](https://gunicorn.org/): the webserver used to run the website.
- [Spycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
- [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.
- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
- [JShint](https://jshint.com/): was used to validate JS code for the website.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
- [BGjar](https://bgjar.com/colored-shapes): I used this tool to create my background image for the app.
- [pixillionfileconverter](https://www.nchsoftware.com/imageconverter): Used to convert my background image file type from svg to jpg.
- [Canva](https://www.canva.com/): I used canva to create CNI app logo.
- [Googlefonts](https://fonts.google.com/specimen/Roboto): Used to find the font needed for the app.  

---

## Bugs

*Bug*
- Initial heroku deployment returned an error message. (solution - I forgot to add the Procfile before initial deployment)

*solution:*
![Screenshot](/static/documentation/debugging/procfilesolution.png)

*Bug*
- When trying to add the filter models/view to the browser, the code was running without an error but the view didnt appear in the browser. 

*Solution* 
- I forgot to add the model to admin.py therefore it wasnt looking for it.
![Screenshot](/static/documentation/debugging/adminsolution.png)

*Bug*
- Struggled to connect external database to app using sqlite db.

*Solution*

*Bug*
- Was unable to add a background image due to the file type being ".svg" had to download a file type converter online to convert to a .jpeg. This solved the issue. 
![Screenshot](/static/documentation/debugging/bgimagebug.png)

*Solution:*
![Screenshot](/static/documentation/debugging/bgimagesolution.png)

*Bug*
- Struggling to add the model, views and forms for users to have the ability to leave movie reviews.

*Solution*
- Updated database to include movie_id in the reviews table as a foreign key in SQLite3 desktop app, pointing to the primary key id in the movies table. Then created a view model and form for the reviews, this included adding a review, via a form, adding a filter to extract all reviews for the specific movie, and display as part of the movie_detail view.

*Bug*
- Bootstrap carousel and search filter pushing header and footer off the page. 

*Solution*
- Added 100vh to the main and removed the position on the footer.

*Bug*
- Log in/out & sign up html pages not inheriting the base html as they should in regards to styles (background image and font colours etc) despite the static files being loaded at the top of the page.

*Solution* 
- Forgot to add the ".main-bg" class to the main of each html page, including the log in and log out pages. 


## Information Architecture

### Database
### Data Modelling


## Design

### Color Scheme

The Color scheme I decided to use was a dark Navy Blue as the main colour. the shapes I used a RGB color index to find the suitable colors for the effect I wanted.

![Screenshot](/static/documentation/screenshots/backgroundcolourscheme.png)

### Typeography

The main font used on the page is a standard and widely used font called Roboto taken from [googlefonts](https://fonts.google.com/specimen/Roboto).

![Screenshot](/static/documentation/screenshots/font2.png)

The backup font made available is called Lato [googlefonts](https://fonts.google.com/specimen/Lato). 

![Screenshot](/static/documentation/screenshots/font1.png)

They were picked as they are good for most styles of app and have a clear letter definition which makes it easy to read throughout the app. 

### Imagery

All images in the home page carousel were taken from the [RottenTomatoes](https://www.rottentomatoes.com/) website via a google search.

The background image was designed on [BGjar](https://bgjar.com/colored-shapes).

The CNI logo used in the Header is also a custom design using [Canva](https://www.canva.com/).

### Wire Frames

- Home Page

![Screenshot](/static/documentation/screenshots/homepagewf.png)

- Search Filter Page

![Screenshot](/static/documentation/screenshots/filterpagewf.png)

- Search Results Page

![Screenshot](/static/documentation/screenshots/searchresultswf.png)


## Testing


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

| Feature | Action | Expected Result | Tested | Passed | Comments |
| --- | --- | --- | --- | --- | --- |
| Home Page | | | | | |
| Bootstrap Carousel Image Slides | Visual aspect to add an appealing style to the home page, hammers home eactly what the site is about. | Aligned properly and clearly visible, 'active' feature to make slides automatically change working. | Yes | Yes | - |
| Sign Up | Option to create account as a user | The user is redirected to sign up page | Yes | Yes | - |
| Sign In | User inputs login details to gain access to full site | Input taken and data used to start the game | Yes | Yes | - |
| Sign Out | User asked for number of players and player names | Input taken and data used to start the game | Yes | Yes | - |
| Search Filter Feature | | | | | |
| Search by Film Name | Search by specific film name | Search results shnow a list of the movie or movies that match the text in the search field input.  | Yes | Yes | Can show multiple film titles as part of a set, (eg Harry Potter), as well as idividual movies |
| Search by Genre | Search by specific genre (eg Horror, comedy) | As above, however, search result based up genre input | Yes | Yes | - |
| Search by Actor| Search by specific Actor/Actress | Any film featuring the named actor/actress will be listed in search results | Yes | Yes | - |
| Search by Release Date | Search by specific Year of release | Define which year you wish the results to yield from (eg 1991) and all films released in that year are listed in the search results | Yes | Yes | - |
| Search by Rotten Tomato Rating | Search by rating | Any film with the specified rating or higher will be listed in the search results | Yes | Yes | - |
| Reviews & Comments | | | | | |
| Leaving a Review | The rules are listed numerically, in a different color font | The user can gain a clear understanding of the game and how to play it | Yes | Yes | - |
| Adding Comments | Select this menu option to leave the game | The user is given a goodbye message and the programme exits back to the python terminal | Yes | Yes | - |
| 'Like' Button | Select this menu option to leave the game | The user is given a goodbye message and the programme exits back to the python terminal | Yes | Yes | - |
| Admin Testing | | | | | |
| Add a User | Search by specific film name | Search results shnow a list of the movie or movies that match the text in the search field input.  | Yes | Yes | Can show multiple film titles as part of a set, (eg Harry Potter), as well as idividual movies |
| Remove/Delete User | Search by specific genre (eg Horror, comedy) | As above, however, search result based up genre input | Yes | Yes | - |
| Approve Reviews/Comments | Search by specific Actor/Actress | Any film featuring the named actor/actress will be listed in search results | Yes | Yes | - |
| Delete Reviews/Comments | Search by specific Year of release | Define which year you wish the results to yield from (eg 1991) and all films released in that year are listed in the search results | Yes | Yes | - |
| Search by Rotten Tomato Rating | Search by rating | Any film with the specified rating or higher will be listed in the search results | Yes | Yes | - |


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
- Rotten Tomatoes for the links and data [RottenTomatoes](https://www.rottentomatoes.com/) Used Rotten tomatoes and a reference for all movies provided to the database.
- Kaggle [Kaggle](https://www.kaggle.com/datasets?search=rotten+tomatoes) Database hub that I pulled the movie databse from.
- Bootstrap [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) Used Bootstrap documentation to help guid me to the correct code to use and what its for.



## Acknowledgements
- My Mentor Iuliia Konovalova. I had issues with the help i was recieving with my previous mentor, 
  but i noticed a huge difference with the way Julia spoke to me and how she managed my situation, 
  she deserves alot of credit and praise for 