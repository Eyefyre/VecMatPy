# VecMatPy - Python library for Vector/Matrix maths

##  Getting it

To download VecMatPy, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install scrapeasy
```

## Using it

```Python
from scrapeasy import Website, Page
```

### Creating a 2D vector
To create a 2D Vector, you simply provide an X and a Y value. Ifthe values are left blank, the vector will default to 0,0

```Python
vec = Vector2D(5,7)
vec = Vector2D()
```

### Creating a 3D vector
This is similar to creating a 2D vector, except you must also provide a Z value.

```Python
vec = Vector3D(5,7,2)
vec = Vector3D()
```

License
----

MIT License

Copyright (c) 2018 Joel Barmettler

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
