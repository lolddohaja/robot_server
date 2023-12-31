# rmf_api_msgs

Collection of json message schemas which bridges the C++ and python components of RMF to the web interface

# Usage

Compile with [colcon](https://colcon.readthedocs.io/en/released/) is recommended

```bash
colcon build --packages-select rmf_api_msgs
source install/setup.bash
```

Subsequently, to access the schemas, the user just needs to include/import the cpp header or py module into their source code.

1. C++ example:

```cpp
#include <rmf_api_msgs/schemas/task_state.hpp>

nlohmann::json schema = rmf_api_msgs::schemas::task_state
```

2. Python example:

```py
from rmf_api_msgs import schemas

# get schema
schema = schemas.task_state()
```

# Python data model generation

To generate the data models based on the schemas, install `datamodel-code-generator`

```bash
pip3 install datamodel-code-generator
```

Recompile with [colcon](https://colcon.readthedocs.io/en/released/)

```bash
colcon build --packages-select rmf_api_msgs
source install/setup.bash
```

The generated data models can then be accessed and used for development,

```py
from rmf_api_msgs.models import task_state

# create task_state model
booking = task_state.Booking(id = "id0001")
task_state = task_state.TaskState(booking = booking)
```
