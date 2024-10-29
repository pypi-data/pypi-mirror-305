import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { ILauncher } from '@jupyterlab/launcher';
import { ICommandPalette } from '@jupyterlab/apputils';
import { TextModelFactory } from '@jupyterlab/docregistry';

/**
 * Initialization data for the jlab_html_extension extension.
 */

const plugin: JupyterFrontEndPlugin<void> = {
  id: 'jlab_html_extension:plugin',
  description: 'Jupyter Lab extension to ease creating web pages.',
  autoStart: true,
  requires: [ILauncher, ICommandPalette], // Ensure dependencies are listed
  activate: (app: JupyterFrontEnd, launcher: ILauncher, palette: ICommandPalette) => {
    console.log('JupyterLab extension jlab_html_extension is activated!');
    const new_html_file = 'jlab_html_extension:create-html';
    const new_css_file = 'jlab_html_extension:create-css';

    app.commands.addCommand(new_html_file, {
      label: 'HTML File',
      caption: 'Create a new HTML file',
      iconClass: 'jp-FileIcon',
      execute: () => {
        const model = new TextModelFactory().createNew();
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
        const model = new TextModelFactory().createNew();
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

export default plugin;