const {app, BrowserWindow} = require("electron");

const appURL = "http://127.0.0.1:8000/"

function ElectronMainMethod(){
    const launchWindow = new BrowserWindow({
        title: "Library Management System",
        width: 777,
        height: 444
    });
    launchWindow.loadURL(appURL);
}

app.whenReady().then(ElectronMainMethod)
