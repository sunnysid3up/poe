# POE
![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)

Path of Exile GraphQL APIs


## Features
- Characters (Classes)
- Ascendancies
- Passive Skills

- Equipment (TBD)
- Gem Skills (TBD)
- League (TBD)
- Quests (TBD)

## Develop
```bash
# Start
docker-compose up --build

# Run test
docker exec -it poe-api bash
python poe/manage.py test content
```


