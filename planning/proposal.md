### Your group members and scrum leader (if applicable) 
N/A
### Your project idea 
>Brief 2-3 sentence description of your app

uTube is a full stack app platform designed to allow users and content creators to share videos, leave comments, and upload videos. Users and content creators will have the ability to edit and delete contents such as comments and videos.

### Your tech stack (frontend, backend, database)
This app will be built using Python3 and Django and styled with Tailwind/Bulma.
### List of backend models and their properties
- Users
    - email
    - password
    - videos
    - comments (one-to-many)
    - playlists (stretch goal)
    - sign up date
    - etc
- Videos
    - description
    - owner (uploader)
    - upload date
    - views
    - comments (many-to-one)
    - playlists (stretch goal) (one-to-many)
- Comments
    - owner (one-to-one)
    - body
    - create date
### React component hierarchy (if applicable)
n/a
### User stories
- As a user, I would want to be able to navigate to the homepage and browse the videos that are newly added to the platform.

- As a user, I would want to be able to watch a specific video I click on.

- As a user, I would like to leave comments for videos, edit my comment, delete my comment.

- As a user, I would like to see details of the video I am watching.

- As a content creator, I would like to have the ability to upload videos onto the platform for others to view.

- As a content creator, I would like to have the ability to edit and delete my videos if needed.

## Stretch Goals

- As a user, I would like to have the ability to create, edit and delete custom playlists for videos I would like to save.

### Wireframes

### Anything else your squad lead should know
