const path = require('path');
const webpack = require('webpack');

module.exports = {
  mode: 'development',
  context: path.join(__dirname, '../client'),
  devtool: 'source-map',
  entry: [
    'webpack-dev-server/client?http://localhost:9000',
    'webpack/hot/only-dev-server',
    './index.js',
  ],
  output: {
    filename: 'bundle.min.js',
    publicPath: 'dist/', // directory where dev-server looks at for bundle
  },
  devServer: {
    contentBase: path.join(__dirname, '../client'),
    compress: true,
    port: 9000,
  },
  module: {
    rules: [{
      test: /\.jsx?$/,
      exclude: /node_modules/,
      enforce: 'pre',
      use: {
        loader: 'babel-loader',
        query: {
          presets: ['env', 'stage-1'],
        },
      },
    },
    {
      test: /\.css$/,
      use: ['style-loader', 'css-loader'],
    },
    {
      test: /\.html$/,
      use: ['html-loader'],
    },
    {
      test: /\.scss$/,
      use: ['style-loader', 'css-loader', 'sass-loader'],
    },
    {
      test: /\.(png|jpg|gif)$/,
      use: [
        {
          loader: 'file-loader',
          options: {},
        },
      ],
    },
    {
      test: /\.(ttf|eot|woff|woff2|svg)(\?v=\d+\.\d+\.\d+)?$/,
      use: [
        {
          loader: 'url-loader',
          options: {},
        },
      ],
    },
    ],
  },
  plugins: [],
};
