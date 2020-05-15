#!/bin/bash
cat > ../index.html <<EOF
<html>
<head>
<title>CTF Q2</title>
  <link rel="stylesheet" href="./build/css.css" />
  <link rel="stylesheet" href="./build/vs.css" />
</head>
<body>
EOF
node build.js < ../readme.md >> ../index.html 
cat >> ../index.html <<EOF
</body>
</html>
EOF

