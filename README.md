# Project One: Boulder Logs
Python, HTML, CSS project

## The first project of many! 

The application is drastically bare bones as we were only allowed to create them using:
  - HTML / CSS
  - Python
  - Flask
  - PostgreSQL and the psycopg

## The Brief

<p>From four briefs I chose the "Travel Bucket List" option as it was the most alike an idea I've been kicking around in my head for a while.</p>
The actual Brief:

> The app should allow the user to track countries and cities they want to visit and those they have visited.
> The user should be able to create and edit countries
> Each country should have one or more cities to visit
> The user should be able to create and delete entries for cities
> The app should allow the user to mark destinations as visited or still to see  

<p>The aim was to create an application that would allow the user to log climbs- much like a person would log places in a bucket list- and mark them as being completed or uncompleted - much like bucket list items are marked as being completed or not, you see how this works. These climbs, or blocs (name for individual boulder climbs because I have focused my application on bouldering specifically) would also need to have a specific boulder that they belong to- this is because this is how climbing works.</p>


## Anything to add?

There is a lot I would love to build onto the bare bones of the application in its current state, here are a few examples:
- A Crag Class, in much the same way that a bloc is saved to a boulder, boulders will belong to a crag. Crags will have a name, a rock-type that is inherited and a climb count. You will be able to create and delete Crags and they would be auto filled as completely if all blocs were completed.
- Image uploading and better topographical maps. The whole concept of Boulder Logs was created to fill the need for up-to-date typography that I always found to be lacking when climbing outdoors. Often times photos and even diagrams are either outdated to near uselessness requiring you have a guide, or not even remotely accurate resulting in half of your time just trying to find the rock you decided you wanted to try. 
- Boulder Logs could easily be an open-source Crag Guide and logging system offering all of the convenience and use for Trad Climbing, Sport Climbing and even Scrambling. In fact it could be used to track new ascents and burgeoning areas of climb potential.
- JavaScript based interactive Maps for viewing and searching functionality.

## Installation
1. You'll need to install flask if not done so already.
2. Install something to manage SQL, PostgreSQL is what we used for the project and so comes highly recommended.
3. Install Psycopg for Python and PSQL to interact.
4. Get the Repo contents however you so wish.
5. Create an empty database called boulderblocs
```bash
createdb bouldersblocs
```
6. In the root directory of repository files run the following code to create tables:
```bash
psql -d bouldersblocs -f ./db/boulders_blocs.sql
```
7. Then run flask within repository's root directory in order to interact with the app.
```
flask run
```
8. Open http://localhost:5000/ and there it should be. 
