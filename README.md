# carla-simulator3
3/6/2022 10:07 PM: CARLA simulator on C000134 in USF ENB 221

3/9/2022 12:26 PM: example message

3/9/2022 1:45 PM: downgrade from Python 3.8.12 to 3.7:

https://github.com/carla-simulator/carla/issues/1466#issuecomment-522797557

/home/nsambhu/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/carla/carla-0.9.13-py3.7-linux-x86_64.egg

TODO: back up Python 3.8.12 environment to carla-simulator3.yml and carla-simulator3-2022-03-09-1352.yml

3/10/2022 10:00 PM: downgrade from Python 3.8.12 to 3.7.11 complete

3/10/2022 10:02 PM: successfully installed carla python module (https://github.com/carla-simulator/carla/issues/1466#issuecomment-522797557) for generate_traffic.py script

3/10/2022 10:13 PM: created environments directory; backed up Python 3.7.11 environment to carla-simulator3-2022-03-10-2210.yml

3/10/2022 10:31 PM: CARLA 0.9.13 autopilot is jerky for cars with multiple gears. Tesla Cybertruck is smoother than the gas car. Autopilot drives very slowly. SDC stops abruptly when approaching a car from behind, regardless of initial following distance: I see the SDC jerk back after every full stop.

3/24/2022 5:34 PM: 
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 32, in <module>
    from agents.navigation.basic_agent import BasicAgent
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/__init__.py", line 22, in <module>
    from . import scripts
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/__init__.py", line 21, in <module>
    from . import train
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/train.py", line 33, in <module>
    from agents.scripts import configs
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/configs.py", line 26, in <module>
    from agents.scripts import networks
  File "/home/nsambhu/anaconda3/envs/carla-simulator3/lib/python3.7/site-packages/agents/scripts/networks.py", line 30, in <module>
    tfd = tf.contrib.distributions
AttributeError: module 'tensorflow' has no attribute 'contrib'
```
3/24/2022 5:53:33 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/scenario_runner$ python -V
Python 3.7.11
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/scenario_runner$ python
Python 3.7.11 (default, Jul 27 2021, 14:32:16) 
[GCC 7.5.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow as tf
>>> print(tf.__version__)
2.8.0
```
3/24/2022 6:22:11 PM: 
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/scenario_runner$ conda list agents
# packages in environment at /home/nsambhu/anaconda3/envs/carla-simulator3:
#
# Name                    Version                   Build  Channel
agents                    1.4.0                    pypi_0    pypi
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/scenario_runner$ conda remove agents
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are missing from the target environment:
  - agents
```
copied (1) /home/nsambhu/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/carla/agents to (2) /home/nsambhu/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics

AttributeError persists.

3/25/2022 11:51:58 AM: Create environment from *.yml:
```
conda create --name bio-env --file bio-env.yml
```
3/25/2022 2:09:05 PM: install from requirements file:
```
conda install --file requirements.txt
```
```
  - xmlschema==1.0.18
  - simple-watchdog-timer
  - py-trees==0.8.3
  - opencv-python==4.2.0.32
```
3/25/2022 2:23:07 PM: 
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 33, in <module>
    import carla
ModuleNotFoundError: No module named 'carla'
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ pip3 install carla
Collecting carla
  Downloading carla-0.9.13-cp37-cp37m-manylinux_2_27_x86_64.whl (29.7 MB)
     |████████████████████████████████| 29.7 MB 7.3 MB/s 
Installing collected packages: carla
Successfully installed carla-0.9.13
```
3/25/2022 2:23:48 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 25, in <module>
    from srunner.scenariomanager.weather_sim import Weather
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/weather_sim.py", line 18, in <module>
    import ephem
ModuleNotFoundError: No module named 'ephem'
```
3/25/2022 2:26:22 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 29, in <module>
    import networkx
ModuleNotFoundError: No module named 'networkx'
```
3/25/2022 2:30:40 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 32, in <module>
    from agents.navigation.basic_agent import BasicAgent
ModuleNotFoundError: No module named 'agents'
```
3/25/2022 2:33:28 PM: in /data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics, rename "agents" to ".agents"

3/25/2022 2:50:00 PM: carla-simulator3 environment is setup for scenario_runner; back up environment to carla-simulator3-2022-03-25-1450.yml
```
conda env export > environments/carla-simulator3-2022-03-25-1450.yml
```
3/27/2022 11:50 AM: atomic_behaviors.py imports relative to the scenarioatomics directory. The current working directory when calling atomic_behaviors.py is the scenario_runner directory. 

3/27/2022 10:49:42 PM: working on imports for atomic_behaviors.py
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
scenario_runner directory /data/data1/GitHub/carla-simulator3/scenario_runner
carla directory /data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/carla
carla directory /data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/carla
press enter to continue
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 46, in <module>
    from agents.navigation.basic_agent import BasicAgent
ModuleNotFoundError: No module named 'agents'
```
3/28/2022 9:48:31 AM: working on imports for atomic_behaviors.py
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
scenario_runner directory /data/data1/GitHub/carla-simulator3/scenario_runner
carla directory /data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics
carla directory /data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics
agents  atomic_behaviors.py  atomic_criteria.py  atomic_trigger_conditions.py  __init__.py  neil_script.py  __pycache__
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 51, in <module>
    from .agents.navigation.basic_agent import BasicAgent
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/agents/navigation/basic_agent.py", line 16, in <module>
    from agents.navigation.local_planner import LocalPlanner
ModuleNotFoundError: No module named 'agents'
```
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
scenario_runner directory /data/data1/GitHub/carla-simulator3/scenario_runner
carla directory /data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics
carla directory /data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics
agents  atomic_behaviors.py  atomic_criteria.py  atomic_trigger_conditions.py  __init__.py  neil_script.py  __pycache__
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 51, in <module>
    from .agents.navigation.basic_agent import BasicAgent
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/agents/navigation/basic_agent.py", line 16, in <module>
    from .agents.navigation.local_planner import LocalPlanner
ModuleNotFoundError: No module named 'srunner.scenariomanager.scenarioatomics.agents.navigation.agents'
```