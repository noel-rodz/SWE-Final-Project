# Music Playlist App (MPLApp)

## Description
MPLApp is a social web application built with Django that lets users create,
share and discover music playlists. Users can build their own playlists, share
them with others, and rate playlists made by the community. In the future, users may also be able to collaborate on playlists by adding songs.

MPLApp solves the problem of sharing music taste in one place: instead of
sending scattered song links, users get a single page per playlist where
others can view songs and leave ratings. Eventually they'll be able to access playlist links as well.

This is the final project for CSCI-3340 (Software Engineering I).

## Objectives
- Allow users to register, log in, log out, and edit their profile information.
- Let logged-in users create playlists with a title and description.
- Allow playlist owners to edit and delete their playlists.
- Let playlist owners add, edit, and remove songs (song title, artist, and music link).
- Give users a page where they can view and manage their own playlists.
- Allow users to browse and search playlists created by others.
- Make playlists shareable through a unique link.
- Let logged-in users rate other users' playlists from 1 to 5 stars and display the average rating.

## Planned Features

### Priorities
- User accounts (register, login, logout, edit profile)
- Playlist management (create, view, edit, delete)
- Songs per playlist (title, artist, link)
- Ratings (1-5) with an average per playlist
- Browse and search playlists

### Possible Future Additions
- Collaborators on playlists
- Playlists with public/private option
- Comments and reviews on playlists
- Share playlists through a link

## Planned Pages and Layout

The application will use multiple  pages connected through a navigation bar. Each page will focus on a specific feature to keep the application organized and easy to use.

### 1. Home / Browse Page
This will be the main page users see when opening MPLApp.

- Display playlists created by users.
- Include a search bar to find playlists by title.
- Show basic playlist information (title, creator, average rating).
- Each playlist will have a **View Playlist** button.
- Navigation bar with **Home**, **My Playlists**, **Login/Register**, or **Logout** depending on whether the user is logged in.

### 2. Register / Login Pages
These pages will allow users to create an account or access an existing one.

- **Register:** Username, email, password, and Sign Up button.
- **Login:** Username, password, and Login button.
- After logging in, users can access their playlists and create new ones.

### 3. My Playlists Page
This page will display all playlists created by the logged-in user.

- List of playlists owned by the user.
- **Create Playlist** button.
- **View**, **Edit**, and **Delete** buttons for each playlist.

### 4. Create / Edit Playlist Page
This page will allow users to create new playlists or update existing ones.

- Form with playlist title and description.
- **Save Playlist** button.
- **Cancel** button to return to the previous page.

The same form can be reused for creating and editing playlists.

### 5. Playlist Details Page
This page will display the contents of a selected playlist.

- Playlist title, description, and creator.
- List of songs showing title, artist, and possibly a link to listen.
- Average rating displayed.
- **Rate Playlist** option (1-5 stars) for logged-in users viewing someone else's playlist.
- **Share** button to copy the playlist URL.

If the logged-in user owns the playlist, additional buttons will appear:
- **Add Song:** Opens a form to enter song title, artist, and music link.
- **Edit Song:** Updates an existing song.
- **Remove Song:** Deletes a song from the playlist.
- **Edit Playlist:** Changes the playlist title or description.
- **Delete Playlist:** Deletes the playlist.

### 6. Profile Page
A simple page where logged-in users can view and update their account information.

- Display username and email.
- **Edit Profile** button.
- **Save Changes** button.

## Technologies
- **Language:** Python 3.12
- **Framework:** Django
- **Database:** SQLite
- **Frontend:** Django templates, HTML, CSS
- **Version control:** Git / GitHub
- **Planning:** GitHub Projects: https://github.com/users/noel-rodz/projects/2

## Environment Setup
1. Clone the repository: `git clone https://github.com/noel-rodz/SWE-Final-Project.git`
2. Create a virtual environment: `python -m venv virt`
3. Activate it: `source virt/bin/activate` (Windows: `virt\Scripts\activate`)
4. Install dependencies: `pip install -r requirements.txt`
5. Go into the project folder: `cd MPLApp`
6. Apply migrations: `python manage.py migrate`
7. Run the server: `python manage.py runserver`

## Agile Planning
**Methodology:** Scrum, adapted for a two-person team

| Item | Detail |
|------|--------|
| Sprint length | 7 days |
| Product backlog | https://github.com/users/noel-rodz/projects/2 |

### Roles
| Name | Role |
|------|------|
| Iris Galicia | Product Owner/Scrum Master, Developer |
| Noel Rodriguez | Product Owner/Scrum Master, Developer |

### Roadmap
| Sprint | Goal |
|--------|------|
| 1 | Repository, environment, README, requirements, roles setup |

## Team
- Noel Rodriguez
- Iris Galicia