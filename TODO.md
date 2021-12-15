# TODO List for ThreeFifteen

## General App

- [x] Complete design
- [x] Create basic server with Flask
- [ ] Finish client frontend UI
- [ ] Finish dashboard frontend UI
- [ ] Accessibility testing
- [ ] Finish dashboard sign-in system and server authentication
- [ ] Allow dashboard to update server data
- [ ] Allow client app to access server data in realtime
- [ ] Alpha testing
- [ ] Tours
- [ ] Write automated tests & run them
- [ ] Internationalization & Localization
- [ ] Open-source app and publish all source code on GitHub
- [ ] Client + Dashboard bundling and deployment on GitHub pages
- [ ] FSF LibreJS compliance and add FSF end software patents logo
- [ ] Decide if we will self-host the app or host it on an external service
  - [ ] Find a good provider for hosting the server (e.g. Heroku or PythonAnywhere)
- [ ] Deploy server
- [ ] App release announcement + Beta testing in-school
- [ ] Handover (the school switches over to ThreeFifteen once it's been proven to work reliably)

## Backend

## Frontend - Client

The client frontend does not need sign-in, local data (e.g. user preferences and bus number) is stored persistently with `Store.js` across user sessions.

This is for the purpose of user privacy; data stored on-device never gets sent to the server, and as a result your data is completely private and in
your control.

### All buses page

- [x] Semantic HTML
- [ ] Alpine.js interactivity
- [ ] CSS styling
- [ ] Smooth Alpine.js transitions

### Your bus page

### Map view page

### Settings page

## Frontend - Dashboard

The dashboard frontend requires admins to sign-in with the correct credentials. There is no sign-up; trusted operators will be manually sent an email
informing them of their credentials.

All operators using the dashboard have permissions to change the data present on the server, and their changes are visible to everyone else instantly.

The client dashboard updates in real-time whenever a change of the server data is made.

### Login System

The login system is a commonly shared set of passwords that sign-ins must use. It has no username, just a password. Additionally, the personal
preferences of each of the admins (e.g. accessibility settings, theme settings, font settings) are stored locally for enhanced privacy. The only thing
that is stored to the server is the school bus data.

All operators tasked with the frontends (in other words the school bus guards) will be given a set of confidential passwords in secret.

The passwords are automatically changed, and the Flask web server generates them randomly every two weeks, and sends the admins an email automatically.
The email will tell them the new password

The operators will use the same set of passwords to login.
