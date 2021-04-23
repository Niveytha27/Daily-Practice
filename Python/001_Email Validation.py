"""
Rules for validation:
---------------------
There should be only one @ symbol.
There should be at least one period.
Special characters should not come in succession.
User name must not have any special characters except period and underscore.
Username must not start or end with a special character.
Email must not start or end with a special character.
Domain name and Domain extension should be at least two characters long.
Domain name should be alphabetic.
Domain extension can have only period and hyphen as special characters.
Maximum length of the email should be 50 and minimum length should be 8.
Username must have at least one alphabetic character.
There should not be any characters other than a-z, A-Z, 0-9 and [@ . _ -] in the email address.
There should not be any whitespace characters in the email address.
"""

import re

def evaluate_email(email):
  result = ''
  pattern = re.compile(r"((^[a-zA-Z0-9]+)([\._]{1}|[a-zA-Z0-9]+)[a-zA-Z0-9]+[@]{1}([a-zA-Z]{2,}\.[a-zA-Z0-9\.-]{2,}))")
  if re.fullmatch(pattern, email) and len(email) in range(8,51):
    result = 'Valid'
  else:
    result = 'Invalid'
  
  return result

email_list = ['brucewayne@jla.com', 'clark_kent@jla.com', '_jonnjonzz@jla.com', 'batman@jla.lead-mem.co.us', 'dianaprince@jla.com', 'victorstone@jla.c0m', 'billybatson@j.com', 'barryallen@jla.c', 'arthurcurry@atlantis.com', 'johnconstantine@jla.c#.us', 'zatannazatara@j1a.com', 'haljordan.@jla.com', 'oliverqueen@jlacom', 'ray_palmer@jla@us', 'carter&hall@jla.com', 'b@jl.us',  'firestorm_equals_engineer_ronald_raymond_plus_doctor_martin_stein@justiceleagueofamerica.com']
print('Email' + ' ' * 95 + 'Result')
for email in email_list:
    result = evaluate_email(email)
    print(f"{email:100s}{result}")