const glob = require("glob");
const Path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const WebpackAssetsManifest = require("webpack-assets-manifest");
const { VueLoaderPlugin } = require('vue-loader');

// var WebpackObfuscator = require('webpack-obfuscator'); //Descomentar esse trecho para obfuscar

const getEntryObject = () => {
  const entries = {};
  glob.sync(Path.join(__dirname, "../src/application/*.js")).forEach((path) => {
    const name = Path.basename(path, ".js");
    entries[name] = path;
  });
  return entries;
};

module.exports = {
  entry: getEntryObject(),
  output: {
    path: Path.join(__dirname, "../build"),
    filename: "js/[name].js",
    publicPath: "/static/",
    assetModuleFilename: "[path][name][ext]",
  },
  optimization: {
    splitChunks: {
      chunks: "all",
    },

    runtimeChunk: "single",
  },
  plugins: [
    new CleanWebpackPlugin(),
    new VueLoaderPlugin(),
    new CopyWebpackPlugin({
      patterns: [
        { from: Path.resolve(__dirname, "../vendors"), to: "vendors" },
      ],
    }),
    //  new WebpackObfuscator ({
    //   rotateStringArray: true
    // }, ['excluded_bundle_name.vue']), //Descomentar esse trecho para obfuscar
    new WebpackAssetsManifest({
      entrypoints: true,
      output: "manifest.json",
      writeToDisk: true,
      publicPath: true,
    }),
  ],
  resolve: {
    alias: {
      "~": Path.resolve(__dirname, "../src"),
    },
  },
  module: {
    rules: [
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: "javascript/auto",
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
        type: "asset",
      },
      {
        test: /\.vue$/,
        loader: "vue-loader",
      },
      //  {
      //   test: /\.vue$/,
      //   exclude: [ 
      //       Path.resolve(__dirname, 'excluded_file_name.vue') 
      //   ],
      //   enforce: 'post',
      //   use: { 
      //       loader: WebpackObfuscator.loader, 
      //       options: {
      //           rotateStringArray: true
      //       }
      //   }
      // },
    ],
  },
};
