# Project One: Boulder Logs
Python, HTML, CSS, flask, PostgreSQL

## The Brief

<p>From four briefs I chose the "Travel Bucket List" option as it was the most alike an idea I've been kicking around in my head for a while.</p>
The actual Brief:

> The app should allow the user to track countries and cities they want to visit and those they have visited.
> The user should be able to create and edit countries
> Each country should have one or more cities to visit
> The user should be able to create and delete entries for cities
> The app should allow the user to mark destinations as visited or still to see  

<p>The aim was to create an application that would allow the user to log climbs- much like a person would log places in a bucket list- and mark them as being completed or uncompleted - much like bucket list items are marked as being completed or not, you see how this works. These climbs, or blocs (name for individual boulder climbs because I have focused my application on bouldering specifically) would also need to have a specific boulder that they belong to therefore giving us that relational database.</p>


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
createdb boulders_blocs
```
6. In the root directory of repository files run the following code to create tables:
```bash
psql -d boulders_blocs -f ./db/boulders_blocs.sql
```
6.b. You can check whether or not the database has not only been created but populated by the sql file if you have Postico...
  i. Open Postico and connect to localhost
  ii. At the top of the window select localhost (then you will see the databases)
  iii. Click on the database you've just made: boulders_blocs
  <img width="1062" alt="Screenshot 2023-05-15 at 16 35 51" src="https://github.com/AbiJays/Boulder_Logs/assets/99146064/8b8fbe25-bcb9-4a72-80c6-37261ebc0292">
  iv. You should see two tables
  <img width="1062" alt="Screenshot 2023-05-15 at 16 42 06" src="https://github.com/AbiJays/Boulder_Logs/assets/99146064/c1a02283-b105-40ae-a47a-26a69d421eb6">
  v. Once selected these tables will show the populated data:
<img width="1062" alt="Screenshot 2023-05-15 at 16 31 36" src="https://github.com/AbiJays/Boulder_Logs/assets/99146064/8dfa2640-7546-4d7f-aa92-47a0ffa5f69f">

7. Then run flask within repository's root directory in order to interact with the app.
```
flask run
```
8. You can either click on the terminal link or open http://localhost:5000/ to view.
<img width="1491" alt="Screenshot 2023-05-15 at 16 47 07" src="https://github.com/AbiJays/Boulder_Logs/assets/99146064/85f991f6-3054-476a-ad11-cf45a95b7a1f">
9.  If you can't get yourself to download it however, here it is in all it's glory-ish.
<img width="1023" alt="Screenshot 2023-05-15 at 16 53 06" src="https://github.com/AbiJays/Boulder_Logs/assets/99146064/031caf53-0e90-4358-9231-1844bdd2b3d6">
<img width="1023" alt="Screenshot 2023-05-15 at 16 52 49" src="https://github.com/AbiJays/Boulder_Logs/assets/99146064/1f0be6dd-a322-4fa9-811a-8390d7460943">
<img width="1023" alt="Screenshot 2023-05-15 at 16 52 54" src="https://github.com/AbiJays/Boulder_Logs/assets/99146064/9bbc1dfa-fe53-4229-8533-bf10ef61725c">
