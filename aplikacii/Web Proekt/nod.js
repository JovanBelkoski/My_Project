const express = require("express");
const app = express();

app.listen(8080, () => {
  console.log("Stranata moze da ja pronajdete na lokacija localhost:8080");
});

app.use(express.static(__dirname));

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/web.html");
});