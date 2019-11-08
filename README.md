# mv_regex

Move files by applying an regular expression. This allows one to partly rename a batch of files.

## Installation

To get these scripts to work one can:

-   Point the `$PATH` to this repository's location, for example by adding the following line to the `~/.bashrc` (or `~/.zshrc`):
  
    ```bash
    export PATH=/path/to/bash_ext:$PATH
    ```

-   'Install' the script:
  
    1.  'Install' the scripts:
  
        ```bash
        cd /path/to/bash_ext
        mkdir build
        cd build
        cmake .. 
        make install
        ```
     
-   'Install' the script in your home folder:
  
    1.  Create a directory to store libraries in the home-folder. For example:
  
        ```bash
        mkdir ~/opt
        ```

    2.  'Install' the bash_ext's scripts. For example:
  
        ```bash
        cd /path/to/bash_ext
        mkdir build
        cd build
        cmake .. -DCMAKE_INSTALL_PREFIX:PATH=$HOME/opt
        make install
        ```
