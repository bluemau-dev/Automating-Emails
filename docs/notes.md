# Documentation of Project Notes and Programming Knowledge

# YAML
- Data Serialization Language
- Human Readable and Computationally Powerful
- Configuration Files (Alternative to JSON and XML)
- Focuses on Keys and Values (Spacing and Indentation)
- Supports .yaml or .yml file types
- There are websites to check if your file is correct
or if you need to convert your configuration file to a different one, pretty cool!

* Example:
    '#' are how you start comments
    team: 76ers                                         # String
    city: Philadelphia          
    year_founded: 1946                                  # Int/Float
    is_current_champion: false                          # Boolean
    background: >                                       # Multi-line String
      This team was founded in some place at some time, 
      they are one of the oldest franchises in the NBA
      and one of the only eight (out of 23) to survive
      the league's first decade.
    organization_history: |
      Syracuse Nationals
      1946-1963

      Philadelphia 76ers
      1963-present

    famous_players:                                     # Lists
      - Joel Embiid
      - Allen Iverson
      - Julius Erving
    famous_players_2: [Joel Embiid, Allen Iverson, Julius Erving]

    management_staff:                                   # Dictionaries
      general_manager: Elton Brand
      president: Daryl Morey
      head_coach: Doc Rivers

    famous_players_3:                                   # List of Objects
      - name: Joel Embiid
        number: 21
      - name: Allen Iverson
        number: 3
      - name: Julius Erving
        number: 6
    
# CI/CD Pipelines
Continous Integration + Continuous Deployment...
Automated testing allows dependencies and other issues to be identified
earlier in software development lifecycle, saving time later. 