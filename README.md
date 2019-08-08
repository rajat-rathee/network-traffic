# Network Traffic Tracker
Track added members on your network with scans. View history of all scans ran and pull 
specific information of who was on the network during each scan. There is also a scheduler feature
where you can automatically run scans every 30 minutes.

Built using: Python, Flask, SQLite3, SQLAlchemy 

## Setting Up

1. Download the application directory.
2. Open netscan.py
3. In the valid_mac list add all the mac addresses you want to track.
4. In the valid_names list all the names of people associated with those mac addresses in the order they appear in the valid_mac list.
5. Add sudo password in palceholder if using scheduling feature.
5. Save and close.

## Installing Dependencies and Database Setup
1. Install following dependencies 
```bash
pip install flask
pip install flask_restful
pip install flask_sqlalchemy
pip install subprocess
``` 
2.

## Using the Extension

1. Click on the Southwest logo on your Chrome toolbar.
2. Enter the information asked for in the pop-up.
3. Click submit and your flight will be checked-in for you.
