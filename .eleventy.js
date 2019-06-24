const highlight = require('highlight.js');
const glob = require('fast-glob');
const path = require('path');
const markdownIt = require('markdown-it');
const markdownItEmoji = require('markdown-it-emoji');
const markdownItAttrs = require('markdown-it-attrs');
const markdownItFootnote = require('markdown-it-footnote');

module.exports = function(eleventyConfig) {
  eleventyConfig.setDataDeepMerge(true);
  eleventyConfig.setUseGitIgnore(false);

  const files = glob.sync(path.join(process.cwd(), "assets/**/*"));
  const exts = files.map(file => path.extname(file).replace('.', ''));

  const markdownLib = markdownIt({
    html: true,
    highlight(str, lang) {
      if (lang && highlight.getLanguage(lang)) {
        try {
          return highlight.highlight(lang, str).value;
        } catch (__) {}
      }
      return '';
    },
  })
    .use(markdownItEmoji)
    .use(markdownItAttrs)
    .use(markdownItFootnote);
  eleventyConfig.setLibrary('md', markdownLib);
  eleventyConfig.setTemplateFormats(['md', 'pug'].concat(exts));
  eleventyConfig.addPassthroughCopy('files');

  return {
    pathPrefix: "/",
    passthroughFileCopy: true,
    markdownTemplateEngine: "liquid",
    htmlTemplateEngine: "pug",
    dataTemplateEngine: "njk",
    dir: {
      input: ".",
      includes: "_includes",
      data: "_data"
    }
  }
}