//import { uuid4 } from "./utils";

var socket;

function socketIOinit() {

    console.log(`Document domain: ${document.domain}:${location.port}`)
    socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('connect', function() {
        console.log('Websocket connected');
    });

    socket.on('dataFromServer', function(data) {
        var jStr = JSON.stringify(data);
        var jObj = JSON.parse(jStr);
        console.log(jObj.datetime + ' ' + jObj.field1 + ' ' + jObj.requestSid);
        var oldData = document.getElementById("contentFromServer").value;
        var newData = '(' + jObj.datetime + ') received: ' + jObj.field1 + ' ' + jObj.requestSid;
        document.getElementById("contentFromServer").innerHTML = newData + '\n' + oldData; 
    });

    socket.on('daemonProcess', function(data) {
        var jStr = JSON.stringify(data);
        var jObj = JSON.parse(jStr);
        console.log(jObj.datetime + ' ' + jObj.name + ' ' + jObj.action + ' ' + jObj.dateMs + ' ' + jObj.requestSid);
        var oldData = document.getElementById("contentFromServer").value;
        var newData = '(' + jObj.datetime + ') received: ' + jObj.name + ' ' + jObj.action + ' ' + jObj.requestSid;
        document.getElementById("contentFromServer").innerHTML = newData + '\n' + oldData; 
    });
}

function clearData() {
    var empty = "";
    document.getElementById("contentFromServer").innerHTML = empty;
}
   
function dataToServer(broadcasting) {
    var data = document.getElementById("contentToServer").value;
    socket.emit('dataToServer', {broadcasting: broadcasting, field1: data});
}

function startDaemon() {
    socket.emit('handleDaemon', {name: '1', action: 'START'});
}

function stopDaemon() {
    socket.emit('handleDaemon', {name: '1', action: 'STOP'});
}