var load_library = function(lib, version) {
  // use cdnjs
  var base = "https://cdnjs.cloudflare.com/ajax/libs/"
  var url = base + lib + '/' + version + '/' + lib + '.min.js'
  
  var script = document.createElement("script");
  script.src = url;
  document.body.appendChild(script);
}
