This project is used for educational purposes. 
 
 ### Installing virtual enviroment
 This project uses pip-tools to manage dependencies,
 in order to setup a virtual environment using pip-tools the following procedure should be followed:

 1. Create a folder for the virtual enviroment.
 
 ```
 mkdir .venv
 ```
 
 2. Install a blank virtual enviroment using python version >3.7.4.

 ```
 python -m venv .venv --prompt [NAME_OF_VIRTUAL_ENV]
 ```

 3. Activate virtual enviroment and install pip-tools

 ```
 source .venv/bin/activate
 pip install pip-tools
 ```
4. Resolve dependencies listed in requirements.in and install packages in virtual enviroment

```
pip-compile
pip-sync
```
5. As you install new packages while working on this project ADD THEM TO requirments.in, not requirments.txt. 
Then repeat step 4 to resolve dependencies and install packages. 


