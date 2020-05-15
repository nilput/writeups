var hljs = require('highlight.js'); // https://highlightjs.org/
var md = require('markdown-it')({
  highlight: function (str, lang) {
    if (lang && hljs.getLanguage(lang)) {
      try {
        return '<pre class="hljs"><code>' +
               hljs.highlight(lang, str, true).value +
               '</code></pre>';
      } catch (__) {}
    }

    return '<pre class="hljs"><code>' + md.utils.escapeHtml(str) + '</code></pre>';
  }
});
var fs = require('fs');
var data = fs.readFileSync(0, 'utf-8');
var result = md.render(data);
process.stdout.write(result);
