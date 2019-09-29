import os
from config import db
from models import Config

# Data to initialize database with
CONFIG = [
    {
      "cpu_request": "string",
      "design_block_desc": "string",
      "design_block_id": "string",
      "job_id": 0,
      "mem_request": "string",
      "project_desc": "string",
      "project_id": "string",
      "project_phase": "string",
      "time_request": "2019-09-28",
      "tool_cmd": "string",
      "tool_used": "string"
    }
]

# Delete database file if it exists currently
# if os.path.exists('testdb1.db'):
#     os.remove('testdb1.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
# for config in CONFIG:
#     c = Config(cpu_request=config['cpu_request'], design_block_desc=config['design_block_desc'], design_block_id=config['design_block_id'],
#                mem_request=config['mem_request'], project_desc=config['project_desc'], project_id=config['project_id'], project_phase=config['project_phase'],
#                tool_cmd=config['tool_cmd'], tool_used=config['tool_used']
#                # , time_request=config['time_request']
#                # , job_id=config['job_id']
#                )
#     db.session.add(c)

db.session.commit()
