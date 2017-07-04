# FB Graph Timezone Converter
This python module gives Current time for any FB Graph API Timezone response

## Getting Started
clone the repo into your computer and you're good to go. :)

```
git clone https://github.com/harshanas/graphtimezoneconv.git
```

## Installation
1. importing module into python script

```
from graphtimezoneconv import time
```

2. instantiating module

```
timezoneConv = time.timezone()
```

## Usage
### get Current Time for Timezone "5.5"

```
timezoneConv.getcurrenttime("5.5")
```

### get Current Time for Timezone "-3.5"

```
timezoneConv.getcurrenttime("-3.5")
```

