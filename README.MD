This package is meant to create a GUI (Graphical User Interface) to manually 
mark the start and stop frames for behaviors to be classified.

The GUI was built using [PySide](https://wiki.qt.io/Qt_for_Python) 
so refer to the website if you have any installation issues.

## Installation:
1. Open a terminal
2. Download the repository <code> git clone https://github.com/senakoko/behaviorMarker.git </code>
3. Create a new conda environment <code>conda create -n pcg python=3.7 -y </code>
4. Activate desired conda environment <code> conda activate pcg </code>
5. Navigate to unzipped folder containing requirements.txt.  
6. Run   
<code>
pip install -r requirements.txt  
</code>  

## Running the GUI
Make sure you are in the behaviormarker folder
```commandline
cd behaviormarker
python mainApp.py
```

### Note:
Edit the config.yaml file to match your settings