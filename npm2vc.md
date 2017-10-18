How to link from npm to Version Control
===========================

Not all packages on NPMS have information on github. More specifically, some packages
on npm have direc references to github, but that info is not present in NPMS.
Here are some without gh data in npms:
```
db.npms_all.find ({ 'collected.github':{'$exists':false} },{"collected.metadata.name":true,"collected.metadata.repository":true})
{ "_id" : ObjectId("59e0e9f480fe8d0c5f758d53"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git://github.com/angular/material.git" }, "name" : "temp-fork-angular-material" } } }
{ "_id" : ObjectId("59e0e9f580fe8d0c5f758d55"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "https://sigurdvh.visualstudio.com/_git/NodeSample" }, "name" : "dummy-nodesample-2" } } }
{ "_id" : ObjectId("59e0e9f580fe8d0c5f758d56"), "collected" : { "metadata" : { "name" : "mtproto-logger" } } }
{ "_id" : ObjectId("59e0e9f580fe8d0c5f758d57"), "collected" : { "metadata" : { "name" : "krupp" } } }
{ "_id" : ObjectId("59e0e9f680fe8d0c5f758d5a"), "collected" : { "metadata" : { "name" : "typeface-carme" } } }
{ "_id" : ObjectId("59e0e9f880fe8d0c5f758d5e"), "collected" : { "metadata" : { "name" : "node_tests" } } }
{ "_id" : ObjectId("59e0e9f980fe8d0c5f758d63"), "collected" : { "metadata" : { "name" : "fission-typescript" } } }
{ "_id" : ObjectId("59e0e9fa80fe8d0c5f758d66"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git+https://github.com/prettier/prettier.git" }, "name" : "@oigroup/prettier-babylon" } } }
{ "_id" : ObjectId("59e0e9fa80fe8d0c5f758d68"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "http://www.github.com/pogopaule/ember-cli-spinkit.git" }, "name" : "ember-cli-spinkit" } } }
{ "_id" : ObjectId("59e0e9fc80fe8d0c5f758d6f"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git+https://github.com/driftyco/ionic.git" }, "name" : "ionic-angular-mstaml" } } }
{ "_id" : ObjectId("59e0e9fd80fe8d0c5f758d71"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git+https://github.com/tcl00taco/censorify.git" }, "name" : "censorify_arif" } } }
{ "_id" : ObjectId("59e0e9fd80fe8d0c5f758d73"), "collected" : { "metadata" : { "name" : "as-angular-cookies" } } }
{ "_id" : ObjectId("59e0e9fe80fe8d0c5f758d77"), "collected" : { "metadata" : { "name" : "zg-ui" } } }
{ "_id" : ObjectId("59e0e9ff80fe8d0c5f758d7a"), "collected" : { "metadata" : { "name" : "elo-rating" } } }
{ "_id" : ObjectId("59e0ea0080fe8d0c5f758d7b"), "collected" : { "metadata" : { "name" : "object-iteration" } } }
{ "_id" : ObjectId("59e0ea0080fe8d0c5f758d7e"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git://github.com/morishitter/postcss-remove-base/git" }, "name" : "postcss-remove-base" } } }
{ "_id" : ObjectId("59e0ea0180fe8d0c5f758d7f"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git+https://github.com/npm/security-holder.git" }, "name" : "simple.io" } } }
{ "_id" : ObjectId("59e0ea0180fe8d0c5f758d80"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git@github.com/tinglejs/tingle-number-field.git" }, "name" : "tingle-number-field" } } }
{ "_id" : ObjectId("59e0ea0280fe8d0c5f758d84"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "https://www.github.com/DefinitelyTyped/DefinitelyTyped.git" }, "name" : "@types/h2o2" } } }
{ "_id" : ObjectId("59e0ea0380fe8d0c5f758d87"), "collected" : { "metadata" : { "repository" : { "type" : "git", "url" : "git+https://github.com/mytcer/mkfiles.git" }, "name" : "mkfiles" } } }
```


Case where github url is provided but npms does not have gh data:
----------------------------------------------------------------
db.all_abrelsfo.findOne({"name":"temp-fork-angular-material"})
{
        "_id" : ObjectId("59db842be433df005b79825d"),
        "scripts" : {

        },
        "jspm" : {
                "peerDependencies" : {

                },
                "dependencies" : {
                        "angular-animate" : "github:angular/bower-angular-animate@^1.5.3",
                        "css" : "systemjs/plugin-css@^0.1.9",
                        "angular-messages" : "github:angular/bower-angular-messages@^1.5.3",
                        "angular-aria" : "github:angular/bower-angular-aria@^1.5.3",
                        "angular" : "github:angular/bower-angular@^1.5.3"
                },
                "shim" : {
                        "angular-material" : {
                                "deps" : [ ]
                        }
                }
        },
        "maintainers" : [
                "fdiskas <projektas@gmail.com>"
        ],
        "peerDependencies" : {
                "angular-animate" : ">=1.3 <1.6",
                "angular-aria" : ">=1.3 <1.6",
                "angular" : ">=1.3 <1.6"
        },
        "gitHead" : "ec9b476051eef167c9b1522e1943f10545119bbe",
        "main" : "index",
        "format" : "cjs",
        "directories" : {

        },
        "keywords" : [
                "angular",
                "material",
                "browser",
                "client-side"
        ],
        "version" : "1.1.1",
        "licenses" : [
                {
                        "url" : "https://github.com/angular/material/blob/master/LICENSE",
                        "type" : "MIT"
                }
        ],
        "dist-tags" : {
                "latest" : "1.1.1"
        },
        "description" : "> NOTE: THIS IS A TEMPORARY FORK OF ANGULAR MATERIAL. IN 99% OF CASES YOU SHOULD USE THE ORIGINAL PACKAGE. > This version is build from [github.com/angular/material/pull/10550](https://github.com/angular/material/pull/10550) This fixes the issue [#9627](h",
        "dist" : {
                "shasum" : "dfa64383d9dfbc70e427a2d246a83cd6336d55f1",
                "tarball" : "https://registry.npmjs.org/temp-fork-angular-material/-/temp-fork-angular-material-1.1.1.tgz"
        },
        "repository" : {
                "url" : "git://github.com/angular/material.git",
                "type" : "git"
        },
        "homepage" : "https://material.angularjs.org",
        "bugs" : {
                "url" : "https://github.com/angular/material/issues"
        },
        "time" : {
                "1.1.1" : "2017-03-31T13:52:56.984Z",
                "created" : "2017-03-31T13:52:56.984Z",
                "modified" : "2017-03-31T13:52:56.984Z"
        },
        "versions" : [
                "1.1.1"
        ],
        "readmeFilename" : "README.md",
        "name" : "temp-fork-angular-material",
        "registry" : "github"
}
```

Case with no VC
---------------
```
db.all_abrelsfo.findOne({"name":"mtproto-logger"})
{
        "_id" : ObjectId("59db842de433df005b798260"),
        "dist-tags" : {
                "alpha" : "0.1.5",
                "latest" : "0.1.9"
        },
        "description" : "",
        "module" : "es/index.js",
        "versions" : [
                "0.1.0",
                "0.1.1",
                "0.1.2",
                "0.1.3",
                "0.1.4",
                "0.1.5",
                "0.1.6",
                "0.1.7",
                "0.1.8",
                "0.1.9"
        ],
        "maintainers" : [
                "drelliot <ribkatt@gmail.com>"
        ],
        "author" : "Zero Bias",
        "directories" : {

        },
        "license" : "MIT",
        "scripts" : {
                "watch:cjs" : "npm run build:cjs -- --watch",
                "build:cjs" : "cross-env BABEL_ENV=commonjs babel src/ -d lib -s",
                "build" : "npm run build:cjs && npm run build:es",
                "build:es" : "babel src/ -d es -s",
                "prepublish" : "npm run clean && npm run build",
                "test" : "echo \"Error: no test specified\" && exit 1",
                "clean" : "rimraf es/ && rimraf lib/",
                "types" : "flow-copy-source src lib && flow-copy-source src es"
        },
        "dependencies" : {
                "debug" : "^2.6.8",
                "eventemitter2" : "^4.1.2",
                "most" : "^1.7.1",
                "chalk" : "^2.1.0",
                "array-flatten" : "^2.1.1",
                "mtproto-shared" : "^0.1.8"
        },
        "main" : "lib/index.js",
        "jsnext:main" : "es/index.js",
        "time" : {
                "0.1.2" : "2017-05-02T13:00:16.772Z",
                "0.1.9" : "2017-09-24T03:29:45.590Z",
                "0.1.0" : "2017-05-02T08:12:17.541Z",
                "0.1.7" : "2017-07-15T13:33:48.734Z",
                "0.1.5" : "2017-05-17T06:39:51.821Z",
                "0.1.1" : "2017-05-02T10:48:58.209Z",
                "0.1.3" : "2017-05-10T01:54:33.763Z",
                "0.1.4" : "2017-05-11T23:29:41.511Z",
                "created" : "2017-05-02T08:12:17.541Z",
                "0.1.8" : "2017-08-23T16:29:46.850Z",
                "0.1.6" : "2017-06-16T22:48:16.314Z",
                "modified" : "2017-09-24T03:29:45.590Z"
        },
        "readmeFilename" : "",
        "files" : [
                "lib",
                "src",
                "es"
        ],
        "name" : "mtproto-logger",
        "version" : "0.1.9",
        "devDependencies" : {
                "babel-cli" : "^6.26.0",
                "babel-plugin-transform-es2015-modules-commonjs" : "^6.26.0",
                "@types/chalk" : "^0.4.31",
                "flow-copy-source" : "^1.2.1",
                "rimraf" : "^2.6.2",
                "@types/debug" : "0.0.30",
                "babel-plugin-transform-flow-strip-types" : "^6.22.0",
                "cross-env" : "^5.0.5",
                "babel-core" : "^6.26.0",
                "babel-plugin-transform-class-properties" : "^6.24.1"
        },
        "dist" : {
                "tarball" : "https://registry.npmjs.org/mtproto-logger/-/mtproto-logger-0.1.9.tgz",
                "shasum" : "722952e9bd4424bbd9ff2a2cd8b253f4339af13a",
                "integrity" : "sha512-YohXpOVXQuc6DMASbyvLrGevhBZLATh371d3LJaqyuFjcY73C+dpn2tyApgJnJN1mraPEPzPi60BiRONLvZa7g=="
        }
}
```

Case where repo appears to be in fact missing:
--------------------------------------------
db.all_abrelsfo.findOne({"name":"krupp"})
{
        "_id" : ObjectId("59db842ee433df005b798261"),
        "main" : "index.js",
        "dist-tags" : {
                "latest" : "0.0.0"
        },
        "description" : "",
        "dist" : {
                "shasum" : "63eeae0dabe567f373fea41360d6da0a6bfc6d72",
                "tarball" : "https://registry.npmjs.org/krupp/-/krupp-0.0.0.tgz"
        },
        "maintainers" : [
                "fdhadzh <fdhadzh@gmail.com>"
        ],
        "author" : "Fadi Hadzh <fdhadzh@gmail.com> (https://fdhadzh.ninja/)",
        "directories" : {

        },
        "license" : "ISC",
        "scripts" : {
                "test" : "echo \"Error: no test specified\" && exit 1"
        },
        "time" : {
                "created" : "2016-04-11T11:54:19.282Z",
                "0.0.0" : "2016-04-11T11:54:19.282Z",
                "modified" : "2016-04-11T11:54:19.282Z"
        },
        "versions" : [
                "0.0.0"
        ],
        "readmeFilename" : "",
        "name" : "krupp",
        "version" : "0.0.0",
        "keywords" : [ ]
}
```

Case when gh repo exists but is not specified (need to use maintainers/name to find it):
---------------------------------------
```
db.all_abrelsfo.findOne({"name":"object-iteration"})
{
        "_id" : ObjectId("59db8445e433df005b798282"),
        "main" : "build/object-iteration.js",
        "dist-tags" : {
                "latest" : "0.1.2"
        },
        "description" : "iteration methods for plain JavaScript objects implemented in the style of the ES5 array methods",
        "dist" : {
                "shasum" : "bf2227ce8f98b8cd311397d1375950354cfd79de",
                "tarball" : "https://registry.npmjs.org/object-iteration/-/object-iteration-0.1.2.tgz"
        },
        "maintainers" : [
                "vijithassar <vijithassar@yahoo.com>"
        ],
        "author" : "Vijith Assar",
        "directories" : {
                "test" : "test"
        },
        "license" : "MIT",
        "devDependencies" : {
                "mocha" : "^3.2.0",
                "rollup" : "^0.41.6",
                "eslint" : "^3.19.0"
        },
        "scripts" : {
                "postinstall" : "npm run build",
                "build" : "rollup --config",
                "lint" : "eslint --config eslintrc.json source && eslint --config eslintrc.json test",
                "dev" : "rollup --config --watch",
                "prepublish" : "npm run lint && npm run test && npm run build",
                "test" : "mocha",
                "pretest" : "npm run build"
        },
        "gitHead" : "5b29186fa2bbc1f3b331a2cef058a09079989a40",
        "time" : {
                "0.1.2" : "2017-04-28T02:52:53.725Z",
                "0.1.0" : "2017-04-27T16:20:14.632Z",
                "created" : "2017-04-27T16:20:14.632Z",
                "0.1.1" : "2017-04-27T19:03:43.789Z",
                "modified" : "2017-04-28T02:52:53.725Z"
        },
        "module" : "index.js",
        "versions" : [
                "0.1.0",
                "0.1.1",
                "0.1.2"
        ],
        "readmeFilename" : "README.md",
        "name" : "object-iteration",
        "version" : "0.1.2",
        "keywords" : [
                "hashmaps",
                "data",
                "structures"
        ]
}
```
