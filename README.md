check-workbench
===============

A [CJWorkbench](https://github.com/CJWorkbench/cjworkbench) data source plugin for [Check](https://github.com/meedan/check)

## Usage

- In Check, obtain a new API key for your team
- In Workbench, import custom module https://github.com/meedan/check-workbench
- Start a new workflow
- Add a Check step with configuration "API key" as per above, "API host" = `https://check-api.checkmedia.org`, "Team" = your team's slug

## Development

You need Workbench running locally.

- Clone this repo
- `python ./setup.py test`
- Clone [Workbench](https://github.com/CJWorkbench/cjworkbench) in a sibling directory
- `CACHE_MODULES=false bin/dev start` in Workbench
- `bin/dev develop-module check-workbench` in Workbench
- Open http://localhost:8000 and start a new workflow
- Add a Check step with configuration as per Usage section

Optionally, you may want to use your local Check API:

- Start local Workbench as above
- `NETWORK=cjworkbench_dev docker-compose up` in Check
- Open http://localhost:8000 and start a new workflow
- Add a Check step with configuration "API key" = `dev`, "API host" = `http://api:3000`, "Team" = your team's slug
