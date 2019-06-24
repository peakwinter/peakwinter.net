module.exports = {
  serveStatic: ['./dist'],
  serveStaticOptions: {
    extensions: ['html']
  },
  https: false,
  open: false,
  watch: true,
  watchOptions: {
    ignoreInitial: true
  },
  ignore: [],
};