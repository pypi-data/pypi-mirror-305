# A PostgreSQL Database and Python Scripts for Lorcana


All copyrights beyond to their respective owners. i.e. Disney, Ravensburger, etc.  I am an enthusiast, just expanding the playability of the game.  I do not have any relationship with these entities.

To install, use pip install LorcanaPygres

Copy the ENV_EXAMPLE as .env, and modify for your installation.

python(3) create_db_schema.py
python(3) full_db_import.py

You will need to have postgres installed, with the configuration added to the .env.  You will also need to have your initial ravensburger api token available for the first run.  You can get this using MITMProxy, along with the handheld client on an iPhone or Android.  It will be the authentication token passed in the first api call.

# Update - 10/24/2024

Updated db connection handler to refresh after a sql injection.  Updated schema to version 1.0.3.  Rerunning the db create tool now checks if db exists.  If it does, it then checks if it can patch it if needed.  Anyone on version 1.0.2 should run the create db again to get to the latest version.
Prepared db for tcg pricing.

# Update - 10/24/2024

Added tool to take your Dreamborn exported csv, and sort it by the known deck popularity as of most recent import

# Update - 10/23/2024

Update to DB Schema.  If you are on a previous version, either drop/recreate database, or truncate database, and then rerun the create_db_schema.  Future releases are planned to handle db upgrades, without requiring this step.
Refactored some of the tool names.

# Update - 10/19/2024

Complete overhaul of postgres database.  It now uses Ravensburgs actual data.  Scripts are updated to handle this new data source.  Added encrypted to sensitive fields in database.

API is the next item on the agenda.

# Update - 9-25-2024

The lorcana api uses a postgres database, with each entry held as a json.  I pulled a copy of all of its contents, and then created a postgres database with each piece of information in its own relational table.  I used my database visualizer to identify typos and data duplicates, which I subsequently cleaned up.

The card_images folder is empty, as I have that included in the .gitignore for now.  The script to pull down your own copy of all images is in this repo.

The current version of this database includes cards up through Shimmering Skies.  I am currently working on adding the upcoming Azurite Sea release.

### Known issues:
1) Starter deck info is incomplete # As of 10/19/2024 this isnt included at all yet.  Will be added in the near future.
2) Azurite Sea Not included yet

### Planned Additions:
1) FastAPI scripts to host your own api.
2) Discord Bot script to show cards, and open random packs for fun.
3) Scripts to automate the adjustment of cards - i.e. resize, rotate, overlay, etc
