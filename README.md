# bazel-example

A sample [Bazel](https://github.com/google/bazel) project that builds a web server and serves a compiled JS application. Uses of the following build rules are demonstrated:

* ```closure_js_binary```
* ```closure_js_library```
* ```closure_stylesheet```
* ```closure_template```
* ```py_binary```
* ```py_library```

The project also makes use of the [Bottle](https://github.com/bottlepy/bottle) and [GFlags](https://github.com/google/python-gflags) projects as external dependencies.

Use the following commands to build/run the project:

```bash
$ bazel build hello/...
$ bazel run hello:main -- --port=8080
```
