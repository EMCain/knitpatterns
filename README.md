## to use: 

* make sure Python 3 is installed 
* run the following terminal commands to set up (once)
```sh
$ virtualenv venv -p `which python3`
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## example 

This example uses the `knpn` function to create a "knit, knit, purl" StitchPattern. 

```python 
In [1]: from stitches import *                                                                           

In [2]: k2p1 = knpn(2, 1)                                                                                

In [3]: k2p1.pattern                                                                                     
Out[3]: [k, k, p]

In [4]: k2p1.name                                                                                        
Out[4]: 'k2p1'

In [5]: k2p1.reverse().pattern                                                                           
Out[5]: [k, p, p]

In [6]: k2p1.reverse().name                                                                              
Out[6]: 'kpp'

In [7]: k2p1.mirror().pattern                                                                            
Out[7]: [p, k, k]

In [8]: k2p1.mirror().name                                                                               
Out[8]: 'pkk'
```
