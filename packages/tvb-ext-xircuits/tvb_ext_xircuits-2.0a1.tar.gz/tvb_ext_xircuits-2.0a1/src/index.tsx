import React from 'react';
import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin,
  ILayoutRestorer
} from '@jupyterlab/application';
import { IFileBrowserFactory } from '@jupyterlab/filebrowser';
import {
  WidgetTracker,
  ReactWidget,
  IWidgetTracker
} from '@jupyterlab/apputils';
import { ILauncher } from '@jupyterlab/launcher';
import { XircuitsFactory } from './XircuitsFactory';
import Sidebar from './tray_library/Sidebar';
import { IDocumentManager, renameDialog } from '@jupyterlab/docmanager';
import { ITranslator } from '@jupyterlab/translation';
import { Log, logPlugin } from './log/LogPlugin';
import { requestAPI } from './server/handler';
import { OutputPanel } from './kernel/panel';
import { IRenderMimeRegistry } from '@jupyterlab/rendermime';
import { DocumentWidget } from '@jupyterlab/docregistry';
import { runIcon, saveIcon } from '@jupyterlab/ui-components';
import { addNodeActionCommands } from './commands/NodeActionCommands';
import { addLibraryActionCommands } from './commands/LibraryActionCommands';
import { Token } from '@lumino/coreutils';
import { DockLayout } from '@lumino/widgets';
import { xircuitsIcon, componentLibIcon, changeFavicon, xircuitsFaviconLink } from './ui-components/icons';
import { createInitXircuits } from './helpers/CanvasInitializer';
import { addHelpResources } from './helpers/HelpResources';
import type { CommandRegistry } from "@lumino/commands/src";
import type { Signal } from "@lumino/signaling";
import { commandIDs } from "./commands/CommandIDs";
import { IEditorTracker } from '@jupyterlab/fileeditor';
import { IMainMenu } from '@jupyterlab/mainmenu';

const FACTORY = 'Xircuits editor';

// Export a token so other extensions can require it
export const IXircuitsDocTracker = new Token<IWidgetTracker<DocumentWidget>>(
  'xircuitsDocTracker'
);

/**
 * A class that tracks xircuits widgets.
 */
 export interface IXircuitsDocTracker
 extends IWidgetTracker<DocumentWidget> {}

/**
 * Initialization data for the documents extension.
 */
const xircuits: JupyterFrontEndPlugin<void> = {
  id: 'xircuits',
  autoStart: true,
  requires: [
    ILauncher,
    IFileBrowserFactory,
    ILayoutRestorer,
    IRenderMimeRegistry,
    IDocumentManager,
    IMainMenu,
    ITranslator,
    IEditorTracker,
  ],
  provides: IXircuitsDocTracker,
  activate: async (
    app: JupyterFrontEnd,
    launcher: ILauncher,
    browserFactory: IFileBrowserFactory,
    restorer: ILayoutRestorer,
    rendermime: IRenderMimeRegistry,
    docmanager: IDocumentManager,
    mainMenu?: IMainMenu,
    translator?: ITranslator,
    editorTracker?: IEditorTracker,
  ) => {

    console.log('Xircuits is activated!');

    // define MathJax configuration before loading the script
    if (!(window as any).MathJax) {
      (window as any).MathJax = {
        tex: {
          inlineMath: [['$', '$'], ['\\(', '\\)']]
        },
        startup: {
          typeset: false, // DO NOT REMOVE: disables automatic typesetting after loading;
          ready: () => {
            console.log('MathJax is ready.');
            (window as any).MathJax.startup.defaultReady(); // ensure default settings are used in our custom ready method
            (window as any).MathJax.typesetPromise()
              .then(() => {console.log('MathJax typesetting complete.');})
              .catch((err: any) => console.error('MathJax typeset failed: ', err));
          }
        }
      };
    }

    // load MathJax from CDN
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.min.js';
    script.async = true;
    script.onload = () => {console.log('MathJax script loaded successfully.');};
    script.onerror = () => {console.error('Failed to load MathJax.');};
    document.head.appendChild(script);

    // Creating the widget factory to register it so the document manager knows about
    // our new DocumentWidget
    const widgetFactory = new XircuitsFactory({
      name: FACTORY,
      fileTypes: ['xircuits'],
      defaultFor: ['xircuits'],
      app: app,
      shell: app.shell,
      commands: app.commands,
      serviceManager: app.serviceManager
    });

    // register the filetype
    app.docRegistry.addFileType({
      name: 'xircuits',
      displayName: 'Xircuits',
      extensions: ['.xircuits'],
      icon: xircuitsIcon
    });

    // Registering the widget factory
    app.docRegistry.addWidgetFactory(widgetFactory);

    const tracker = new WidgetTracker<DocumentWidget>({
      namespace: "Xircuits Tracker"
    });

    // Add the widget to the tracker when it's created
    widgetFactory.widgetCreated.connect((sender, widget) => {
      // Notify the instance tracker if restore data needs to update.
      void tracker.add(widget);

      // Notify the widget tracker if restore data needs to update
      widget.context.pathChanged.connect(() => {
        void tracker.save(widget);
      });
    });

    // Handle state restoration
    void restorer.restore(tracker, {
      command: commandIDs.openDocManager,
      args: widget => ({
        path: widget.context.path,
        factory: FACTORY
      }),
      name: widget => widget.context.path
    });

    // Creating the sidebar widget for the xai components
    const sidebarWidget = ReactWidget.create(<Sidebar app={app} factory={widgetFactory}/>);
    sidebarWidget.id = 'xircuits-component-sidebar';
    sidebarWidget.title.icon = componentLibIcon;
    sidebarWidget.title.caption = "Xircuits Component Library";

    restorer.add(sidebarWidget, sidebarWidget.id);
    app.shell.add(sidebarWidget, "left");

    // Additional commands for node action
    addNodeActionCommands(app, tracker, translator);

    // Additional commands for chat actions
    addLibraryActionCommands(app, tracker, translator, widgetFactory);

    // Additional main menu options for help resources
    addHelpResources(app, mainMenu, translator);

    // Commands to emit WidgetFactory signals
    const emitSignal = (signal: Signal<unknown, unknown>) =>  (args: unknown) => signal.emit(args);
    const signalConnections: [string, CommandRegistry.ICommandOptions][] = [
      [commandIDs.saveXircuit,
        {label: "Save", icon: saveIcon, execute: emitSignal(widgetFactory.saveXircuitSignal)}],
      [commandIDs.runXircuit,
        {label: "Run Xircuits", icon: runIcon, execute: emitSignal(widgetFactory.runXircuitSignal)}],
      [commandIDs.compileXircuit,
        {execute: emitSignal(widgetFactory.compileXircuitSignal)}],
      [commandIDs.fetchRemoteRunConfig,
        {execute: emitSignal(widgetFactory.fetchRemoteRunConfigSignal)}],
        [commandIDs.lockXircuit,
        {execute: emitSignal(widgetFactory.lockNodeSignal)}],
      [commandIDs.triggerLoadingAnimation,
        {execute: emitSignal(widgetFactory.triggerLoadingAnimationSignal)}],
      [commandIDs.reloadAllNodes,
        {execute: emitSignal(widgetFactory.reloadAllNodesSignal)}],
      [commandIDs.toggleAllLinkAnimation,
        {execute: emitSignal(widgetFactory.toggleAllLinkAnimationSignal)}]
    ]
    signalConnections.forEach(([cmdId, def]) => app.commands.addCommand(cmdId, def))


    // Add a command for creating a new xircuits file.
    app.commands.addCommand(commandIDs.createNewXircuit, {
      label: (args) => (args['isLauncher'] ? 'Xircuits File' : 'Create New Xircuits'),
      icon: xircuitsIcon,
      caption: 'Create a new xircuits file',
      execute: async () => {
        const currentBrowser = browserFactory.tracker.currentWidget;
        if (!currentBrowser) {
          console.error("No active file browser found.");
          return;
        }
        const model = await app.commands
          .execute(commandIDs.newDocManager, {
            path: currentBrowser.model.path,
            type: "file",
            ext: ".xircuits"
          });

          // get init SRD json
          const fileContent = createInitXircuits(app, app.shell);

          // Use the document manager to write to the file
          await app.serviceManager.contents.save(model.path, {
            type: 'file',
            format: 'text',
            content: fileContent
          });

        await app.commands.execute(
          commandIDs.openDocManager,
          {
            path: model.path,
            factory: FACTORY
          }
        );
      }
    });

    async function requestToGenerateCompileFile(path: string, python_paths: any) {
      const data = {
        "outPath": path.split(".xircuits")[0] + ".py",
        "filePath": path,
        "pythonPaths": python_paths
      };

      try {
        return await requestAPI<any>('file/compile', {
          body: JSON.stringify(data),
          method: 'POST',
        });

      } catch (reason) {
        console.error(
          'Error on POST /xircuits/file/compile', data, reason
        );
      }
    }

    app.commands.addCommand(commandIDs.compileFile, {
      execute: async args => {
        const path = tracker.currentWidget.context.path;
        const showOutput = typeof args['showOutput'] === undefined ? false : (args['showOutput'] as boolean);

        const python_paths = {};
        (args['componentList'] === undefined ? [] : args['componentList'] as []).filter(it => it['python_path']).forEach(it => {
          python_paths[it['name']] = it['python_path']
        });

        const request = await requestToGenerateCompileFile(path, python_paths);

        if (request["message"] == "completed") {
          const model_path = path.split(".xircuits")[0] + ".py";
          docmanager.closeFile(model_path);

          if (showOutput) {
            alert(`${model_path} successfully compiled!`);
          }
          if(model_path.startsWith("xai_components/")){
             console.info(`File ${model_path} changed. Reloading components...`);
             await app.commands.execute(commandIDs.refreshComponentList);
          }
        } else {
          console.log(request["message"])
          alert("Failed to generate compiled code. Please check console logs for more details.");
        }
      }
    });

    // Auto-reload components when a component file changes
    editorTracker.widgetAdded.connect((sender, widget) => {
      const context = widget.context;

      if (context.path.endsWith('.py')) {
        context.fileChanged.connect(async () => {
          if(context.path.startsWith("xai_components/")){
            console.info(`File ${context.path} changed. Reloading components...`);
            await app.commands.execute(commandIDs.refreshComponentList);
          }
        });
      }

      if (context.path.endsWith('config.ini')) {
        context.fileChanged.connect(async () => {
          if(context.path.startsWith(".xircuits/")){
            await app.commands.execute(commandIDs.fetchRemoteRunConfig);
          }
        });
      }
    });

    let outputPanel: OutputPanel;
    /**
      * Creates a output panel.
      *
      * @returns The panel
      */
    async function createPanel(): Promise<OutputPanel> {
      let splitMode: DockLayout.InsertMode = 'split-bottom' as DockLayout.InsertMode; // default value

      try {
        const data = await requestAPI<any>('config/split_mode');
          splitMode = data.splitMode as DockLayout.InsertMode;
      } catch (err) {
        console.error('Error fetching split mode from server:', err);
      }

      outputPanel = new OutputPanel(app.serviceManager, rendermime, widgetFactory, translator);
      app.shell.add(outputPanel, 'main', { mode: splitMode });
      return outputPanel;
    }

    // Dispose the output panel when closing browser or tab
    window.addEventListener('beforeunload', function (e) {
      outputPanel.dispose();
    });

    // Execute command and display at output panel
    app.commands.addCommand(commandIDs.executeToOutputPanel, {
      execute: async args => {
        const xircuitsLogger = new Log(app);

        // Create the panel if it does not exist
        if (!outputPanel || outputPanel.isDisposed) {
          await createPanel();
        }

        outputPanel.session.ready.then(async () => {
          const code = args['code'] as string;
          outputPanel.execute(code, xircuitsLogger);
        });
      },
    });

    app.commands.addCommand(commandIDs.copyXircuitsToRoot, {
      label: 'Copy To Root Directory',
      isVisible: () => [...browserFactory.tracker.currentWidget.selectedItems()].length > 0,
      icon: xircuitsIcon,
      execute: async () => {
        const selectedItems = Array.from(browserFactory.tracker.currentWidget.selectedItems());
    
        for (const xircuitsFile of selectedItems) {
          const path = xircuitsFile.path;
          const fileName = path.split('/').pop();
          const rootPath = `/${fileName}`;
    
          try {
            await app.serviceManager.contents.copy(path, rootPath);
            await app.commands.execute('filebrowser:go-to-path', { path: '/' });
    
            // Open the file if needed, then prompt for renaming
            const openedWidget = await app.commands.execute(commandIDs.openDocManager, { path: rootPath, factory: FACTORY });
            const fileContext = docmanager.contextForWidget(openedWidget);
            if (fileContext) {
              await renameDialog(docmanager, fileContext);
            }
          } catch (err) {
            if (err.response && err.response.status === 400) {
              alert(`Error: The file '${fileName}' already exists in the root directory.`);
            } else {
              alert(`Error copying file '${fileName}': ${err.message || err}`);
            }
          }
        }
      }
    });

    app.contextMenu.addItem({
      command: commandIDs.copyXircuitsToRoot,
      selector: '.jp-DirListing-item[data-file-type="xircuits"]',
    });

    app.commands.addCommand(commandIDs.openXircuitsConfiguration, {
      label: 'Open Xircuits Configurations',
      icon: xircuitsIcon,
      execute: async () => {
        const configPath = `.xircuits/config.ini`;
        try {
          // Check if the file exists first
          await app.serviceManager.contents.get(configPath);
          // If we reach here, the file exists, so we can try to open it
          await docmanager.openOrReveal(configPath);
        } catch (error) {
          if (error.response && error.response.status === 404) {
            alert('Xircuits configuration file not found. Check if it exists or enable hidden files when you launch Jupyter Lab.');
          } else {
            alert(`Error accessing Xircuits configuration: ${error.message}`);
          }
        }
      }
    });

    mainMenu.settingsMenu.addGroup([
      {
        command: commandIDs.openXircuitsConfiguration,
      },
    ], -1);

    // Add a launcher item if the launcher is available.
    if (launcher) {
      launcher.add({
        command: commandIDs.createNewXircuit,
        rank: 1,
        args: { isLauncher: true },
        category: 'Other'
      });
    }
  },
};

/**
 * Export the plugins as default.
 */
const plugins: JupyterFrontEndPlugin<any>[] = [
  xircuits,
  logPlugin
];

export default plugins;
