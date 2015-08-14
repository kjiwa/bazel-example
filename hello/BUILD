load("/tools/build_rules/closure/closure_js_binary", "closure_js_binary")
load("/tools/build_rules/closure/closure_js_library", "closure_js_library")
load("/tools/build_rules/closure/closure_stylesheet_library", "closure_stylesheet_library")
load("/tools/build_rules/closure/closure_template_library", "closure_template_library")

py_binary(
    name = "main",
    srcs = ["__main__.py"],
    main = "__main__.py",
    deps = [
        "@bottle//:bottle",
        "@python_gflags//:python_gflags",
        ":server",
    ],
)

py_library(
    name = "server",
    srcs = ["server.py"],
    data = [
        "index.html",
        ":hello_combined.js",
        ":styles_combined.css",
    ],
    deps = ["@bottle//:bottle"],
)

closure_js_binary(
    name = "hello",
    main = "hello",
    visibility = ["//crimsonglow:__subpackages__"],
    deps = [":js"],
)

closure_js_library(
    name = "js",
    srcs = glob(["**/*.js"]),
    deps = [
        "@closure_library//:closure_library",
        "@closure_templates//:closure_templates_js",
        ":styles",
        ":templates",
    ],
)

closure_stylesheet_library(
    name = "styles",
    srcs = ["hello.gss"],
    deps = ["@closure_library//:closure_library_css"],
)

closure_template_library(
    name = "templates",
    srcs = ["hello.soy"],
)
