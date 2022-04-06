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
3/28/2022 8:50:41 PM: https://www.geeksforgeeks.org/python-import-module-from-different-directory/ In atomic_behaviors.py, add agents directory to Python system path.

3/29/2022 9:36:58 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
scenario_runner directory /data/data1/GitHub/carla-simulator3/scenario_runner
CARLA_VER   Docs   LICENSE      metrics_manager.py  no_rendering_mode.py  recording_files scenario_runner.py
Dockerfile  Jenkinsfile  manual_control.py  mkdocs.yml    README.md       requirements.txt  srunner
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 54, in <module>
    import neil_script
ModuleNotFoundError: No module named 'neil_script'
```
3/29/2022 10:30:03 PM: relative import failed
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 55
    from ../neil_script import BasicAgent
           ^
SyntaxError: invalid syntax
```
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
scenario_runner directory /data/data1/GitHub/carla-simulator3/scenario_runner
CARLA_VER   Docs   LICENSE      metrics_manager.py  no_rendering_mode.py  recording_files scenario_runner.py
Dockerfile  Jenkinsfile  manual_control.py  mkdocs.yml    README.md       requirements.txt  srunner
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 55, in <module>
    from ...neil_script import BasicAgent
ModuleNotFoundError: No module named 'srunner.neil_script'
```
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
scenario_runner directory /data/data1/GitHub/carla-simulator3/scenario_runner
CARLA_VER   Docs   LICENSE      metrics_manager.py  no_rendering_mode.py  recording_files scenario_runner.py
Dockerfile  Jenkinsfile  manual_control.py  mkdocs.yml    README.md       requirements.txt  srunner
Traceback (most recent call last):
  File "scenario_runner.py", line 35, in <module>
    from srunner.scenarioconfigs.openscenario_configuration import OpenScenarioConfiguration
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarioconfigs/openscenario_configuration.py", line 24, in <module>
    from srunner.tools.openscenario_parser import OpenScenarioParser, ParameterRef
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/tools/openscenario_parser.py", line 26, in <module>
    from srunner.scenariomanager.scenarioatomics.atomic_behaviors import (TrafficLightStateSetter,
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenarioatomics/atomic_behaviors.py", line 55, in <module>
    from ....neil_script import BasicAgent
ValueError: attempted relative import beyond top-level package
```
3/29/2022 10:35:55 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
scenario_runner directory /data/data1/GitHub/carla-simulator3/scenario_runner
CARLA_VER   Docs   LICENSE      metrics_manager.py  no_rendering_mode.py  recording_files scenario_runner.py
Dockerfile  Jenkinsfile  manual_control.py  mkdocs.yml    README.md       requirements.txt  srunner
Traceback (most recent call last):
  File "scenario_runner.py", line 37, in <module>
    from srunner.scenariomanager.scenario_manager import ScenarioManager
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/scenario_manager.py", line 21, in <module>
    from srunner.scenariomanager.result_writer import ResultOutputProvider
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenariomanager/result_writer.py", line 17, in <module>
    from tabulate import tabulate
ModuleNotFoundError: No module named 'tabulate'
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ pip install tabulate
Collecting tabulate
  Downloading tabulate-0.8.9-py3-none-any.whl (25 kB)
Installing collected packages: tabulate
Successfully installed tabulate-0.8.9
```
3/29/2022 10:39:04 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Configuration for scenario 00_scenario_name cannot be found!
No more scenarios .... Exiting
```
3/30/2022 11:21:35 AM: removed "." from import in basic_agent.py

3/30/2022 11:22:28 AM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Configuration for scenario 00_scenario_name cannot be found!
No more scenarios .... Exiting
```
3/30/2022 1:07:45 PM: writing script to call CarlaUE4.sh, generate_traffic.py, dynamic_weather.py, manual_control.py

3/30/2022 1:40:21 PM: Python Popen (failed)
```
(base) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3$ python neil_script.py 
(base) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3$ 4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
LowLevelFatalError [File:Unknown] [Line: 136] 
Exception thrown: bind: Address already in use
Signal 11 caught.
Malloc Size=65538 LargeMemoryPoolOffset=65554 
CommonUnixCrashHandler: Signal=11
Malloc Size=131160 LargeMemoryPoolOffset=196744 
Malloc Size=131160 LargeMemoryPoolOffset=327928 
Engine crash handling finished; re-raising signal 11 for the default handler. Good bye.
Segmentation fault (core dumped)
ERROR conda.cli.main_run:execute(33): Subprocess for 'conda run ['python', '/data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/examples/generate_traffic.py']' command failed.  (See above for error)

destroying 0 vehicles

destroying 0 walkers

done.

Traceback (most recent call last):
  File "/data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/examples/generate_traffic.py", line 377, in <module>
    main()
  File "/data/data1/GitHub/carla-simulator3/CARLA_0.9.13/PythonAPI/examples/generate_traffic.py", line 165, in main
    world = client.get_world()
RuntimeError: time-out of 10000ms while waiting for the simulator, make sure the simulator is ready and connected to 127.0.0.1:2000
```
3/30/2022 1:49:15 PM: potential solution: https://stackoverflow.com/questions/22656359/bash-shell-script-opening-multiple-terminals-and-executing-distinct-commands 

3/30/2022 1:52:12 PM: TODO: 'screen' in bash script

3/30/2022 2:17:47 PM: instead of "screen," use "tmux": https://tmuxcheatsheet.com/

3/30/2022 2:42:49 PM: tmux (1) does not allow detaching from command line and (2) pyautogui does not detach with shortcut keys; tangentially, the "ls" command within the tmux, called from the Python script does not work: there is unintelligible output.

3/30/2022 2:45:35 PM: can bash script switch tmux sessions? 

3/30/2022 2:56:04 PM: xdotool allows keyboard presses

3/30/2022 4:23:09 PM: paused "writing script to call CarlaUE4.sh, generate_traffic.py, dynamic_weather.py, manual_control.py"

3/30/2022 4:28:32 PM: with CARLA simulator running, scenario_runner.py configuration error persists
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario 00_scenario_name --record recording_files
Configuration for scenario 00_scenario_name cannot be found!
No more scenarios .... Exiting
```

3/31/2022 10:53:25 AM: https://www.google.com/search?q=carla+Configuration+for+scenario+00_scenario_name+cannot+be+found!&rlz=1C1CHBF_enUS856US856&oq=carla+Configuration+for+scenario+00_scenario_name+cannot+be+found!&aqs=chrome..69i57.2534j0j7&sourceid=chrome&ie=UTF-8 > https://github.com/carla-simulator/scenario_runner/issues/338 > https://github.com/carla-simulator/scenario_runner/blob/master/Docs/getting_started.md

3/31/2022 10:59:47 AM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --help
usage: scenario_runner.py [-h] [-v] [--host HOST] [--port PORT]
                          [--timeout TIMEOUT]
                          [--trafficManagerPort TRAFFICMANAGERPORT]
                          [--trafficManagerSeed TRAFFICMANAGERSEED] [--sync]
                          [--list] [--scenario SCENARIO]
                          [--openscenario OPENSCENARIO]
                          [--openscenarioparams OPENSCENARIOPARAMS]
                          [--route ROUTE [ROUTE ...]] [--agent AGENT]
                          [--agentConfig AGENTCONFIG] [--output] [--file]
                          [--junit] [--json] [--outputDir OUTPUTDIR]
                          [--configFile CONFIGFILE]
                          [--additionalScenario ADDITIONALSCENARIO] [--debug]
                          [--reloadWorld] [--record RECORD] [--randomize]
                          [--repetitions REPETITIONS] [--waitForEgo]

CARLA Scenario Runner: Setup, Run and Evaluate scenarios using CARLA
Current version: 0.9.13

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --host HOST           IP of the host server (default: localhost)
  --port PORT           TCP port to listen to (default: 2000)
  --timeout TIMEOUT     Set the CARLA client timeout value in seconds
  --trafficManagerPort TRAFFICMANAGERPORT
                        Port to use for the TrafficManager (default: 8000)
  --trafficManagerSeed TRAFFICMANAGERSEED
                        Seed used by the TrafficManager (default: 0)
  --sync                Forces the simulation to run synchronously
  --list                List all supported scenarios and exit
  --scenario SCENARIO   Name of the scenario to be executed. Use the preposition 'group:' to run all scenarios of one class, e.g. ControlLoss or FollowLeadingVehicle
  --openscenario OPENSCENARIO
                        Provide an OpenSCENARIO definition
  --openscenarioparams OPENSCENARIOPARAMS
                        Overwrited for OpenSCENARIO ParameterDeclaration
  --route ROUTE [ROUTE ...]
                        Run a route as a scenario (input: (route_file,scenario_file,[route id]))
  --agent AGENT         Agent used to execute the scenario. Currently only compatible with route-based scenarios.
  --agentConfig AGENTCONFIG
                        Path to Agent's configuration file
  --output              Provide results on stdout
  --file                Write results into a txt file
  --junit               Write results into a junit file
  --json                Write results into a JSON file
  --outputDir OUTPUTDIR
                        Directory for output files (default: this directory)
  --configFile CONFIGFILE
                        Provide an additional scenario configuration file (*.xml)
  --additionalScenario ADDITIONALSCENARIO
                        Provide additional scenario implementations (*.py)
  --debug               Run with debug output
  --reloadWorld         Reload the CARLA world before starting a scenario (default=True)
  --record RECORD       Path were the files will be saved, relative to SCENARIO_RUNNER_ROOT.
                        Activates the CARLA recording feature and saves to file all the criteria information.
  --randomize           Scenario parameters are randomized
  --repetitions REPETITIONS
                        Number of scenario executions
  --waitForEgo          Connect the scenario to an existing ego vehicle
```
3/31/2022 11:09:55 AM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files
Traceback (most recent call last):
  File "scenario_runner.py", line 607, in main
    result = scenario_runner.run()
  File "scenario_runner.py", line 511, in run
    result = self._run_scenarios()
  File "scenario_runner.py", line 451, in _run_scenarios
    result = self._load_and_run_scenario(config)
  File "scenario_runner.py", line 355, in _load_and_run_scenario
    if not self._load_and_wait_for_world(config.town, config.ego_vehicles):
  File "scenario_runner.py", line 325, in _load_and_wait_for_world
    self.world = self.client.get_world()
RuntimeError: time-out of 10000ms while waiting for the simulator, make sure the simulator is ready and connected to 127.0.0.1:2000
```
3/31/2022 11:16:49 AM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/CARLA_0.9.13$ sh CarlaUE4.sh
4.26.2-0+++UE4+Release-4.26 522 0
Disabling core dumps.
```
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files
The CARLA server uses the wrong map: Town10HD_Opt
This scenario requires to use map: Town01
No more scenarios .... Exiting
```
3/31/2022 11:18:13 AM: list of scenarios: https://github.com/carla-simulator/scenario_runner/blob/master/Docs/list_of_scenarios.md

3/31/2022 11:32:48 AM: scenarios on hard disk: /data/data1/GitHub/carla-simulator3/scenario_runner/srunner/examples/\*.xml

3/31/2022 11:47:29 AM: error from 3/31/2022 11:16:49 AM; TODO: change map in CARLA

3/31/2022 3:04:10 PM: 
```
The CARLA server uses the wrong map: Town10HD_Opt
```
3/31/2022 3:13:36 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --reloadWorld
Neil
Traceback (most recent call last):
  File "scenario_runner.py", line 609, in main
    result = scenario_runner.run()
  File "scenario_runner.py", line 513, in run
    result = self._run_scenarios()
  File "scenario_runner.py", line 453, in _run_scenarios
    result = self._load_and_run_scenario(config)
  File "scenario_runner.py", line 357, in _load_and_run_scenario
    if not self._load_and_wait_for_world(config.town, config.ego_vehicles):
  File "scenario_runner.py", line 309, in _load_and_wait_for_world
    print(client.get_available_maps())
NameError: name 'client' is not defined
```
3/31/2022 3:17:46 PM:
```
print(client.get_available_maps())
```
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --reloadWorld
['/Game/Carla/Maps/Town10HD', '/Game/Carla/Maps/Town04_Opt', '/Game/Carla/Maps/Town01_Opt', '/Game/Carla/Maps/Town01', '/Game/Carla/Maps/Town02', '/Game/Carla/Maps/Town04', '/Game/Carla/Maps/Town03_Opt', '/Game/Carla/Maps/Town10HD_Opt', '/Game/Carla/Maps/Town02_Opt', '/Game/Carla/Maps/Town05_Opt', '/Game/Carla/Maps/Town03', '/Game/Carla/Maps/Town05']
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 398, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 370
ERROR: failed to destroy actor 370 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/1/2022 12:13:29 AM: TODO:find "Game/Carla/Maps" directory

4/1/2022 12:24:57 AM: maybe use the following directory for Town01: /data/data1/GitHub/carla-simulator3/CARLA_0.9.13/CarlaUE4/Content/Carla/Maps. Relevant file for Town01 should be Maps/Town01.\*; I don't know the correct file extention to use of the availabile Town01.* files.

4/1/2022 12:34:51 AM: TODO: find config file; how to change town in config file

4/1/2022 12:39:35 AM: (re: find config file) try to use xml from "3/31/2022 11:32:48 AM" tag

4/1/2022 11:49:16 AM: changed FollowLeadingVehicle.xml map from Town01 to Town10HD_Opt
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 47
ERROR: failed to destroy actor 47 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 49
ERROR: failed to destroy actor 49 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/1/2022 11:55:24 AM: 
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml 
The CARLA server uses the wrong map: Town10HD_Opt
This scenario requires to use map: Town01
The CARLA server uses the wrong map: Town10HD_Opt
This scenario requires to use map: Town01
No more scenarios .... Exiting
```
4/1/2022 11:59:12 AM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 224
ERROR: failed to destroy actor 224 : unable to destroy actor: not found 
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 399
ERROR: failed to destroy actor 399 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/1/2022 12:02:12 PM: opened CARLA simulator window; error from 4/1/2022 11:59:12 AM persists. manual_control.py shows Town01.
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml 
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 803
ERROR: failed to destroy actor 803 : unable to destroy actor: not found 
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 805
ERROR: failed to destroy actor 805 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 980
ERROR: failed to destroy actor 980 : unable to destroy actor: not found 
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 1155
ERROR: failed to destroy actor 1155 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/1/2022 12:06:50 PM: start CARLA simulator > manual_control.py > python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml 
The CARLA server uses the wrong map: Town10HD_Opt
This scenario requires to use map: Town01
The CARLA server uses the wrong map: Town10HD_Opt
This scenario requires to use map: Town01
No more scenarios .... Exiting
```
4/1/2022 12:08:56 PM: start CARLA simulator > manual_control.py > ...

4/1/2022 11:10:55 PM: start CARLA simulator > manual_control.py > python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml --reloadWorld
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 203
ERROR: failed to destroy actor 203 : unable to destroy actor: not found 
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 400, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 378
ERROR: failed to destroy actor 378 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/1/2022 11:22:20 PM: Town01 loads by using "--configFile srunner/examples/FollowLeadingVehicle.xml"; this is visible when manual_control.py is after scenario_runner.py
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml
_load_and_run_scenario Town01
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 401, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 380
ERROR: failed to destroy actor 380 : unable to destroy actor: not found 
_load_and_run_scenario Town01
Preparing scenario: FollowLeadingVehicle_1
The scenario cannot be loaded
Traceback (most recent call last):
  File "scenario_runner.py", line 401, in _load_and_run_scenario
    self._args.debug)
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 78, in __init__
    criteria_enable=criteria_enable)
  File "/data/data1/GitHub/carla-simulator3/scenario_runner/srunner/scenarios/basic_scenario.py", line 64, in __init__
    behavior = self._create_behavior()
  File ".//srunner/scenarios/follow_leading_vehicle.py", line 113, in _create_behavior
    policy=py_trees.common.ParallelPolicy.SUCCESS_ON_ONE)
AttributeError: type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
type object 'ParallelPolicy' has no attribute 'SUCCESS_ON_ONE'
Destroying ego vehicle 382
ERROR: failed to destroy actor 382 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/1/2022 11:35:49 PM: https://github.com/carla-simulator/scenario_runner/issues/23 > downgrade py-trees 2.1.6 to 0.8.3

4/1/2022 11:42:22 PM: TODO: log and criteria files: scenario_runner.py creates log file (empty) and does not create criteria file

4/1/2022 11:44:44 PM: TODO: backup carla-simulator3 environment to yml file

4/4/2022 4:28:20 PM: back up environment to carla-simulator3-2022-04-04-1626.yml

4/4/2022 4:33:57 PM: log and criteria files: https://carla-scenariorunner.readthedocs.io/en/latest/getting_started/ > check CARLA_ROOT added to Python path

4/4/2022 4:49:24 PM: scratchpad:
```
export CARLA_ROOT=/data/data1/GitHub/carla-simulator3
export PYTHONPATH=$PYTHONPATH:${CARLA_ROOT}/PythonAPI/carla/dist/carla-0.9.13-py3.7-linux-x86_64.egg:${CARLA_ROOT}/PythonAPI/carla/agents:${CARLA_ROOT}/PythonAPI/carla

(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ printenv PYTHONPATH
:/data/data1/GitHub/carla-simulator3/PythonAPI/carla/dist/carla-0.9.13-py3.7-linux-x86_64.egg
:/data/data1/GitHub/carla-simulator3/PythonAPI/carla/agents
:/data/data1/GitHub/carla-simulator3/PythonAPI/carla
```
4/4/2022 4:55:44 PM:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
ScenarioManager: Running scenario FollowVehicle
Not all scenario tests were successful
Please run with --output for further information
Destroying ego vehicle 197
ERROR: failed to destroy actor 197 : unable to destroy actor: not found 
Preparing scenario: FollowLeadingVehicle_1
ScenarioManager: Running scenario FollowVehicle
Not all scenario tests were successful
Please run with --output for further information
Destroying ego vehicle 379
ERROR: failed to destroy actor 379 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/5/2022 1:19:11 AM: "ERROR: failed to destroy actor 197 : unable to destroy actor: not found" > https://github.com/carla-simulator/scenario_runner/issues/852 > error is more like a warning

4/5/2022 1:21:25 AM: TODO: log and criteria files: scenario_runner.py creates log file (empty) and does not create criteria file: 

https://carla-scenariorunner.readthedocs.io/en/latest/metrics_module/#how-to-use-the-metrics-module: 1. A CARLA recording (.log) — Contains simulation data per frame. To know more about this, read the recorder docs.: https://carla.readthedocs.io/en/latest/adv_recorder/

4/5/2022 11:41:54 AM: TODO: 
https://carla.readthedocs.io/en/0.9.13/adv_recorder/ > "client.start_recorder("/home/carla/recording01.log")"

4/5/2022 11:43:16 AM: TODO: change .gitignore to include all \*.py files.

4/6/2022 12:26:41 PM: pause: "change .gitignore to include all \*.py files."

4/6/2022 12:35:41 PM: specify config file:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --configFile srunner/examples/FollowLeadingVehicle.xml --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
Neil got here
ScenarioManager: Running scenario FollowVehicle
Not all scenario tests were successful
Please run with --output for further information
Destroying ego vehicle 555
ERROR: failed to destroy actor 555 : unable to destroy actor: not found 
Preparing scenario: FollowLeadingVehicle_1
Neil got here
ScenarioManager: Running scenario FollowVehicle
Not all scenario tests were successful
Please run with --output for further information
Destroying ego vehicle 731
ERROR: failed to destroy actor 731 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/6/2022 12:37:35 PM: omit config file:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
Neil got here
ScenarioManager: Running scenario FollowVehicle
Not all scenario tests were successful
Please run with --output for further information
Destroying ego vehicle 907
ERROR: failed to destroy actor 907 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/6/2022 12:43:17 PM: run with --output flag:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --reloadWorld --output
Preparing scenario: FollowLeadingVehicle_1
Neil got here
ScenarioManager: Running scenario FollowVehicle

 ======= Results of Scenario: FollowVehicle ---- TIMEOUT =======

 > Ego vehicles:
Actor(id=1083, type=vehicle.lincoln.mkz_2017); 

 > Other actors:
Actor(id=1084, type=vehicle.nissan.patrol); 

 > Simulation Information
╒═════════════════════════════════╤═════════════════════╕
│ Start Time                      │ 2022-04-06 12:43:48 │
├─────────────────────────────────┼─────────────────────┤
│ End Time                        │ 2022-04-06 12:44:48 │
├─────────────────────────────────┼─────────────────────┤
│ Duration (System Time)          │ 60.02s              │
├─────────────────────────────────┼─────────────────────┤
│ Duration (Game Time)            │ 60.01s              │
├─────────────────────────────────┼─────────────────────┤
│ Ratio (System Time / Game Time) │ 1.0s                │
╘═════════════════════════════════╧═════════════════════╛

 > Criteria Information
╒════════════════════════════╤══════════════════════╤═════════╤══════════════╤════════════════╕
│ Actor                      │ Criterion            │ Result  │ Actual Value │ Expected Value │
├────────────────────────────┼──────────────────────┼─────────┼──────────────┼────────────────┤
│ lincoln.mkz_2017 (id=1083) │ CollisionTest (Req.) │ SUCCESS │ 0            │ 0              │
├────────────────────────────┼──────────────────────┼─────────┼──────────────┼────────────────┤
│                            │ Timeout (Req.)       │ FAILURE │ 60.01        │ 60             │
├────────────────────────────┼──────────────────────┼─────────┼──────────────┼────────────────┤
│                            │ GLOBAL RESULT        │ TIMEOUT │              │                │
╘════════════════════════════╧══════════════════════╧═════════╧══════════════╧════════════════╛
 ===============================================================

Not all scenario tests were successful
Destroying ego vehicle 1083
ERROR: failed to destroy actor 1083 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/6/2022 12:50:24 PM: print recorder_name:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
Neil got here
.//recording_files/FollowLeadingVehicle_1.log
Neil left here
ScenarioManager: Running scenario FollowVehicle
Not all scenario tests were successful
Please run with --output for further information
Destroying ego vehicle 1259
ERROR: failed to destroy actor 1259 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
4/6/2022 12:54:34 PM: print working directory:
```
(carla-simulator3) nsambhu@SAMBHU19:/data/data1/GitHub/carla-simulator3/scenario_runner$ python scenario_runner.py --scenario FollowLeadingVehicle_1 --record recording_files --reloadWorld
Preparing scenario: FollowLeadingVehicle_1
Neil got here
current directory /data/data1/GitHub/carla-simulator3/scenario_runner
recorder_name .//recording_files/FollowLeadingVehicle_1.log
Neil left here
ScenarioManager: Running scenario FollowVehicle
Not all scenario tests were successful
Please run with --output for further information
Destroying ego vehicle 1435
ERROR: failed to destroy actor 1435 : unable to destroy actor: not found 
No more scenarios .... Exiting
```
