const highlight = require('highlight.js');
const moment = require('moment');
const markdownIt = require('markdown-it');
const markdownItEmoji = require('markdown-it-emoji');
const markdownItAttrs = require('markdown-it-attrs');
const markdownItFootnote = require('markdown-it-footnote');

module.exports = function(eleventyConfig) {
  eleventyConfig.setDataDeepMerge(true);
  eleventyConfig.setUseGitIgnore(false);
  eleventyConfig.addPassthroughCopy('files');
  eleventyConfig.addPassthroughCopy('assets/dist');

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

  return {
    templateFormats: [
      "md",
      "pug"
    ],

    pathPrefix: "/",

    markdownTemplateEngine: "liquid",
    htmlTemplateEngine: "pug",
    dataTemplateEngine: "pug",
    dir: {
      input: ".",
      includes: "_includes",
      data: "_data",
      output: "_site"
    }
  }
}