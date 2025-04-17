const http = require("http");
const port = 3000;
const server = http.createServer((req, res)=>{
    res.end("Node.js con Docker");
});
server.listen(port, ()=>console.log(`Servidor iniciado en el puerto ${port}`));