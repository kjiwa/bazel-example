# bazel-example

A sample [https://github.com/google/bazel](Bazel) project that builds a web server and serves a compiled JS application. Use of the following build rules are demonstrated:

* closure_js_binary
* closure_js_library
* closure_stylesheet
* closure_template
* py_binary
* py_library

The project also makes use of the [https://github.com/bottlepy/bottle](Bottle) and [https://github.com/google/python-gflags](GFlags) projects as external dependencies.

Use the following commands to build/run the project:

```bash
$ bazel build hello/...
$ bazel run hello:main -- --port=8080
```
