# TRACOParser

Python (ver. 3.8+) tool that parses output from TRACO/PLUTO and generates CUDA source code. This project's structure is basically divided into two main areas:


**TRACO Parsing**   - All source code that resides in Parser folder, it's main function is analyze code generated by TRACO and generate interface that consists Python objects that other areas of this project can interact with. 
To learn more, visit Wiki pages: 

[Parser structure](https://github.com/PrzemyslawSamsel/TRACOParser/wiki/Parser-library---structure)


[Parser basic usage / examples](https://github.com/PrzemyslawSamsel/TRACOParser/wiki/Parser-library---basic-usage---examples)


**CUDA Generation** - Based on objects generated earlier this area's main focus is to create working CUDA code that can be later compiled. 

