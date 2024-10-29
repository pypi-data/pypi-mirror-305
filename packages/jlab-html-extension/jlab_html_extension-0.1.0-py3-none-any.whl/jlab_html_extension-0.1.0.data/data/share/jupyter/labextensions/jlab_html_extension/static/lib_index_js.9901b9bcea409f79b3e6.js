"use strict";
(self["webpackChunkjlab_html_extension"] = self["webpackChunkjlab_html_extension"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/docregistry */ "webpack/sharing/consume/default/@jupyterlab/docregistry");
/* harmony import */ var _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__);



/**
 * Initialization data for the jlab_html_extension extension.
 */
const plugin = {
    id: 'jlab_html_extension:plugin',
    description: 'Jupyter Lab extension to ease creating web pages.',
    autoStart: true,
    requires: [_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_0__.ILauncher, _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: (app, launcher, palette) => {
        console.log('JupyterLab extension jlab_html_extension is activated!');
        const new_html_file = 'jlab_html_extension:create-html';
        const new_css_file = 'jlab_html_extension:create-css';
        app.commands.addCommand(new_html_file, {
            label: 'HTML File',
            caption: 'Create a new HTML file',
            iconClass: 'jp-FileIcon',
            execute: () => {
                const model = new _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__.TextModelFactory().createNew();
                model.sharedModel.setSource('<!-- New HTML File -->');
                const widget = app.serviceManager.contents.newUntitled({
                    type: 'file',
                    ext: '.html',
                });
                widget.then(file => {
                    //app.commands.execute('docmanager:open', { path: file.path });
                    app.commands.execute('docmanager:open', { path: file.path, factory: 'Editor' });
                });
            }
        });
        app.commands.addCommand(new_css_file, {
            label: 'CSS File',
            caption: 'Create a new CSS file',
            iconClass: 'jp-FileIcon',
            execute: () => {
                const model = new _jupyterlab_docregistry__WEBPACK_IMPORTED_MODULE_2__.TextModelFactory().createNew();
                model.sharedModel.setSource('<!-- New CSS File -->');
                const widget = app.serviceManager.contents.newUntitled({
                    type: 'file',
                    ext: '.css',
                });
                widget.then(file => {
                    //app.commands.execute('docmanager:open', { path: file.path });
                    app.commands.execute('docmanager:open', { path: file.path, factory: 'Editor' });
                });
            }
        });
        // Add the command to the launcher and command palette
        const category = 'File Operations';
        launcher.add({ command: new_html_file });
        launcher.add({ command: new_css_file });
        palette.addItem({ command: new_html_file, category });
        palette.addItem({ command: new_css_file, category });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.9901b9bcea409f79b3e6.js.map