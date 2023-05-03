!pip install -q condacolab
import condacolab
condacolab.install()

!conda --version
!which conda

!conda create --name py35 python=3.5 
!conda env list
!conda init 

!source /usr/local/bin/activate py35
