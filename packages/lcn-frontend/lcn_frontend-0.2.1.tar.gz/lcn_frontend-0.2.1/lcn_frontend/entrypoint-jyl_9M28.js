
function loadES5() {
  var el = document.createElement('script');
  el.src = '/lcn_static/frontend_es5/entrypoint-q0wpd1i1.js';
  document.body.appendChild(el);
}
if (/.*Version\/(?:11|12)(?:\.\d+)*.*Safari\//.test(navigator.userAgent)) {
    loadES5();
} else {
  try {
    new Function("import('/lcn_static/frontend_latest/entrypoint-jyl_9M28.js')")();
  } catch (err) {
    loadES5();
  }
}
  